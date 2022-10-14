from datetime import datetime, timedelta
import re
from textwrap import dedent
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc
from datetime import date

from dash.dependencies import Input, Output, State
from data_store import DataStore
from daily_tracker import DailyTracker

user = "mrg"
app = dash.Dash(__name__)
server = app.server
ds = DataStore()
dt = DailyTracker()
app.config.suppress_callback_exceptions = False

app.layout = html.Div(
    [
        html.Div(
            [
                html.Img(src="assets/dash-logo.png", className="app__logo"),
                html.H4("Life Tracker", className="header__text"),
            ],
            className="app__header",
        ),
        html.Div(
            [
                dcc.Tabs(
                    id="tabs",
                    value="life-tracker",
                    children=[
                        dcc.Tab(
                            id="manage-metrics",
                            label="Manage Metrics",
                            value="manage-metrics",
                            children=[
                                html.Div(
                                    [
                                        dcc.RadioItems(id='selected_metric', options=ds.getAllMetricNames(user),
                                                       value='', inline=True),
                                        html.Div(
                                            [
                                                html.P(
                                                    "Metric:",
                                                    className="input__heading",
                                                ),
                                                dcc.Input(
                                                    id="metric",
                                                    placeholder="Metric Name",
                                                    className="metric__input",
                                                ),
                                            ],
                                            className="input__container",
                                        ),
                                        html.Div(
                                            [
                                                html.P(
                                                    "Metric Type:",
                                                    className="input__heading",
                                                ),
                                                dcc.Dropdown(
                                                    id="metric-type",
                                                    options=[
                                                        {"label": i, "value": i}
                                                        for i in [
                                                            "Hour",
                                                            "Minute",
                                                            "Number",
                                                            "Enum",
                                                            "Boolean"
                                                        ]
                                                    ],
                                                    value="Hour",
                                                    placeholder="Select Metric Type",
                                                    className="",
                                                ),
                                            ],
                                            className="dropdown__container",
                                        ),
                                        html.Div(
                                            [
                                                html.P(
                                                    "Description : ",
                                                    className="input__heading",
                                                ),
                                                dcc.Input(
                                                    id="description",
                                                    placeholder="Description for Metric",
                                                    className="metric__input",
                                                ),
                                            ],
                                            className="input__container",
                                        ),
                                        html.Div(
                                            [
                                                html.P(
                                                    "Allowed Values:",
                                                    className="input__heading",
                                                ),
                                                dcc.Input(
                                                    id="allowed-values",
                                                    value="",
                                                    placeholder="Comma separated values for enum, maximum allowed value for "
                                                                "num/hour/minute (minimum is assumed to be 0)",
                                                    className="metric__input",
                                                ),
                                            ],
                                            className="input__container",
                                        ),
                                        html.Div(
                                            [
                                                html.P(
                                                    "Enabled:",
                                                    className="input__heading",
                                                ),
                                                daq.BooleanSwitch(id='enabled', on=False),
                                            ],
                                            className="input__container",
                                        ),
                                        html.Div(
                                            [
                                                html.Button(
                                                    "Update Metric",
                                                    id="submit-metric",
                                                    n_clicks=0,
                                                    className="submit__button",
                                                )
                                            ]
                                        ),
                                    ],
                                    className="container__1",
                                )
                            ],
                        ),
                        dcc.Tab(
                            id="enter-data",
                            label="Fill Daily Data",
                            value="enter-data",
                            children=[
                                html.Div([
                                    html.Div(
                                        dcc.DatePickerSingle(
                                            id='tracker-date',
                                            min_date_allowed=date.today() - timedelta(days=7),
                                            max_date_allowed=date.today(),
                                            initial_visible_month=date.today(),
                                            #display_format='MMMM y, DD',
                                            date=date.today(),
                                            className="input__date"

                                        ),
                                    ),
                                    html.Form(id="daily-data-form",
                                              children=dt.genform(user, date.today().strftime('%Y-%m-%d')),
                                              className="container__1", ),
                                    html.Div([html.Button("Submit", id="daily-tracker-submit", n_clicks=0,
                                                          className="submit__button")])
                                ],
                                className="container__1")
                            ])
                    ],
                )
            ],
            className="tabs__container",
        ),
        html.Div(
            id="alert"
        ),
        html.Div(
            id="alert-tracker-update"
        )
    ],
    className="app__container",
)


@app.callback(
    Output("daily-data-form", "children"),
    Input("tracker-date", "date")
)
def load_daily_tracker(tracker_date):
    if not tracker_date:
        return
    # selected_date = datetime.strptime(tracker_date, '%Y-%m-%d')
    return dt.genform(user, tracker_date)


@app.callback(
    Output("alert-tracker-update", "children"),
    Input("daily-tracker-submit", "n_clicks"),
    State("daily-data-form", "children"),
    State("tracker-date", "date")
)
def update_daily_tracker(n_clicks, values, tracker_date):
    if not values:
        return
    if n_clicks > 0:
        dt.addTrackerData(user, tracker_date, values)
    return


@app.callback(
    Output("metric", "value"),
    Output("metric-type", "value"),
    Output("description", "value"),
    Output("allowed-values", "value"),
    Output("enabled", "on"),
    Input("selected_metric", "value"),
)
def select_metric_to_update(value):
    metricData = ds.getMetric(value, user)
    if metricData is None:
        return None, None, None, None, None
    print(metricData)
    return metricData[1], metricData[2], metricData[3], metricData[4], metricData[5]


@app.callback(
    Output("alert", "children"),
    Input("submit-metric", "n_clicks"),
    State("metric", "value"),
    State("metric-type", "value"),
    State("description", "value"),
    State("allowed-values", "value"),
    State("enabled", "on")
)
def add_metric_to_db(n_clicks, metric, metric_type, description, allowed_values, enabled):
    if metric is None or len(metric) == 0:
        return dbc.Alert(
            "Metric Name Cannot be blank",
            id="alert-auto",
            is_open=True,
            duration=4000,
        )
    if metric_type is None or len(metric_type) == 0:
        return dbc.Alert(
            "Metric Type Cannot be blank",
            id="alert-auto",
            is_open=True,
            duration=4000,
        )
    if metric_type == 'Enum':
        values = allowed_values.split(",")
        if len(values) < 2:
            return dbc.Alert(
                "Invalid allowed values for Enum Type",
                id="alert-auto",
                is_open=True,
                duration=4000,
            )
    else:
        if metric_type != 'bool':
            if len(allowed_values) > 0 and not allowed_values.isnumeric():
                return dbc.Alert(
                    "Maximum Value for number field should be a number",
                    id="alert-auto",
                    is_open=True,
                    duration=4000,
                )
    print(n_clicks)

    metric_entry = {
        "metric": metric,
        "user": user,
        "metric_type": metric_type,
        "description": description,
        "allowed_values": allowed_values,
        "enabled": enabled,
    }
    insert_entry = ds.upsertMetric(metric_entry)
    return dbc.Alert(
        "Metric updated successfully!",
        id="alert-auto",
        is_open=True,
        duration=4000,
    )


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_ui=True, dev_tools_props_check=True)
