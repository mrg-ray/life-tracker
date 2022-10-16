from datetime import date, datetime, timedelta

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc

from lifeTracker.data_store import DataStore

from lifeTracker import trackerapp
from trackerapp import app
from dash.dependencies import Input, Output, State

ds = DataStore()

def format_options(options):
    list=[]
    for option in options:
        list.append({'label':html.Span(option, style={'font-size': 15, 'margin-right': 20 , 'margin-left': 3}) , 'value' : option})
    return list
def createView(metric, user, selected_date):
    label = html.P(
        metric[3] + " :",
        className="input__heading",
    )
    value = ds.getTrackerForGivenDate(user, selected_date, metric[1])
    metric_input = None
    if metric[2] == 'Hour' or metric[2] == 'Minute' or metric[2] == 'Number':
        if value:
            value = int(value[0])
        else:
            value = 0
        metric_input = dcc.Slider(id=metric[1], min=0, max=int(metric[4]), step=1, value=value,
                                  className="metric_value")
    if metric[2] == 'Boolean':
        if value:
            value = bool(value[0])
        else:
            value = False
        metric_input = daq.BooleanSwitch(id=metric[1], on=value, className="metric_value")
    if metric[2] == 'Enum':
        if value:
            value = value[0][0]
        else:
            value = ''
        metric_input = dcc.RadioItems(id=metric[1], options=format_options(metric[4].split(",")), className="metric_value",
                                      value=value, inline=True)
    return html.Div(
        [label, metric_input],
        className="input__container container__1",
    )


def genform(user, selected_date):
    elements = []
    metrics = ds.getAllMetrics(user)
    for metric in metrics.values:
        elements.append(createView(metric, user, selected_date))
    return elements


def addTrackerData(user, selected_date, values):
    for value in values:
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
                ds.upsertMetricTracker(selected_date, user, metricName, metricValue)
    return


tracker_form = html.Div([
    html.Div(
        dcc.DatePickerSingle(
            id='tracker-date',
            min_date_allowed=date.today() - timedelta(days=7),
            max_date_allowed=date.today(),
            initial_visible_month=date.today(),
            # display_format='MMMM y, DD',
            date=date.today(),
            className="input__date"

        ),
    ),
    html.Div(id="daily-data-form",
             children=genform(trackerapp.user, date.today().strftime('%Y-%m-%d')),
             ),
    html.Div([html.Button("Submit", id="daily-tracker-submit", n_clicks=0,
                          className="submit__button")]),
    html.Div(id="alert-tracker-update")
    ],

    className="container__1"
)

@app.callback(
    Output("daily-data-form", "children"),
    Input("tracker-date", "date")
)
def load_daily_tracker(tracker_date):
    if not tracker_date:
        return
    # selected_date = datetime.strptime(tracker_date, '%Y-%m-%d')
    return genform(trackerapp.user, tracker_date)


@app.callback(
    Output("alert-tracker-update", "children"),
    Input("daily-tracker-submit", "n_clicks"),
    State("daily-data-form", "children"),
    State("tracker-date", "date")
)
def update_daily_tracker(n_clicks, values, tracker_date):
    if values and n_clicks > 0:
        addTrackerData(trackerapp.user, tracker_date, values)
    return dbc.Alert(
        "Tracker Data  Added",
        id="alert-auto",
        is_open=True,
        duration=4000,
    )





