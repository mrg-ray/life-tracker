from datetime import date, datetime, timedelta

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc
from flask_login import current_user

from lifeTracker.data_store import DataStore

from lifeTracker.trackerapp import app
from dash.dependencies import Input, Output, State
import lifeTracker.contants as const

ds = DataStore()


def format_options(options):
    list = []
    for option in options:
        list.append({'label': html.Span(option, style={'font-size': 15, 'margin-right': 20, 'margin-left': 3}),
                     'value': option})
    return list


def createView(metric, user, selected_date):
    label = html.P(
        metric[3] + " :",
        className="input__heading",
    )
    value = ds.getTrackerForGivenDate(user, selected_date, metric[1])
    metric_input = None
    if metric[2] == const.hr or metric[2] == const.num:
        if value:
            value = float(value)
        else:
            value = 0
        if metric[4]:
            max = float(metric[4])
        else:
            max = 100000
        if max <= 10:
            metric_input = dcc.Slider(id=metric[1], min=0, max=max, step=1, value=value,
                                      className="metric_value")
        else:
            metric_input = dcc.Input(id=metric[1], type="number", placeholder="Number", value=value, min=0, max=max,
                                     className="metric_value")
    if metric[2] == 'Boolean':
        if value:
            value = bool(int(value))
        else:
            value = False
        metric_input = daq.BooleanSwitch(id=metric[1], on=value, className="metric_value")
    if metric[2] == 'Enum':
        if value:
            value = value[0][0]
        else:
            value = ''
        metric_input = dcc.RadioItems(id=metric[1], options=format_options(metric[4].split(",")),
                                      className="metric_value",
                                      value=value, inline=True)
    return html.Div(
        [label, metric_input],
        className="input__container container__1",
    )


def genform(user, selected_date):
    tabs = []
    metrics = ds.getAllMetrics(user)
    dimensions = metrics.dimension.unique()
    for dim in dimensions:
        sub_metrics = metrics[metrics.dimension == dim]
        elements = []
        for metric in sub_metrics.values:
            elements.append(createView(metric, user, selected_date))
        tab = dcc.Tab(label=dim, value=dim, children=elements)
        tabs.append(tab)
    return tabs


def addTrackerData(user, selected_date, values):
    data = {}
    for tab in values:
        for value in tab.get("props").get("children"):
            for entry in value.get("props").get("children"):
                item = entry.get("props")
                if item.get("className") == "metric_value":
                    metricName = item.get("id")
                    metric = ds.getMetric(user=user, metric=metricName)
                    if metric[2] == 'Boolean':
                        metricValue = item.get("on")
                    else:
                        metricValue = item.get("value")
                    print(metricValue)
                    if metricValue is None:
                        raise Exception("Value for Metric " + metricName + " is Null.")
                    data[metricName] = metricValue
    for key in data.keys():
        ds.upsertMetricTracker(selected_date, user, key, data.get(key))
    ds.upsertMetricTracker(selected_date, user, "tracker_tracker", 1)
    return


tracker_form = html.Div([
    html.Div(
        dcc.DatePickerSingle(
            id='tracker-date',
            min_date_allowed=date.today() - timedelta(days=30),
            initial_visible_month=date.today(),
            # display_format='MMMM y, DD',
            date=date.today(),
            className="input__date"
        ),
        className="center"
    ),
    dcc.Tabs(id="daily-data-form", children=[]),
    html.Div(children=[
        html.Div([html.Button("Submit", id="daily-tracker-submit", n_clicks=0,
                              className="submit__button")])
    ],
        className="center"
    ),
    html.Div(id="alert-tracker-update")
],

    className="container__1"
)


@app.callback(
    Output("daily-data-form", "children"),
    Input("tracker-date", "date")
)
def load_daily_tracker(tracker_date):
    user = current_user.name
    if not tracker_date:
        tracker_date = date.today().strftime('%Y-%m-%d')
    # selected_date = datetime.strptime(tracker_date, '%Y-%m-%d')
    return genform(user, tracker_date)


@app.callback(
    Output("alert-tracker-update", "children"),
    Input("daily-tracker-submit", "n_clicks"),
    State("daily-data-form", "children"),
    State("tracker-date", "date")
)
def update_daily_tracker(n_clicks, values, tracker_date):
    user = current_user.name
    if values and n_clicks > 0:
        addTrackerData(user, tracker_date, values)
        return dbc.Alert(
            "Tracker Data  Added",
            id="alert-auto",
            is_open=True,
            duration=4000,
        )
    return ''
