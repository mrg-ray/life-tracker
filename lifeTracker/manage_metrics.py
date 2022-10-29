import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
from flask_login import current_user

from lifeTracker.trackerapp import app
from lifeTracker.data_store import DataStore
import lifeTracker.contants as const
ds=DataStore()


def format_options(options):
    list=[]
    for option in options:
        list.append({'label':html.Span(option, style={'font-size': 15, 'margin-right': 20 , 'margin-left': 3}) , 'value' : option})
    return list


metric_layout = html.Div(
    [
        html.Div(
            [
                html.P(
                    "Show Disabled Metrics:",
                    className="input__heading",
                ),
                daq.BooleanSwitch(id='show-disabled', on=False),
            ],
            className="input__container",
        ),
        html.Div(
            [
                html.P(
                    "Life Dimension:",
                    className="input__heading",
                ),
                dcc.Dropdown(
                    id="life-dimension",
                    options=[
                        {"label": i, "value": i}
                        for i in [
                            const.health,
                            const.personal_growth,
                            const.family_matters,
                            const.professional_growth,
                            const.sex,
                            const.wealth
                        ]
                    ],
                    value="",
                    placeholder="Select Dimension Type",
                    className="",
                ),
            ],
            className="dropdown__container",
        ),
        html.Div(
            [
                dcc.RadioItems(id='selected_metric', value='', inline=True),
            ],
            className="input__container",
        ),
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
                            const.hr,
                            const.bool,
                            const.num,
                            const.enum
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
                    "Green Level : ",
                    className="input__heading",
                ),
                dcc.Input(
                    id="green-level",
                    placeholder="Mean threshold for metric status in green",
                    className="metric__input",
                ),
            ],
            className="input__container",
        ),
        html.Div(
            [
                html.P(
                    "Red Level : ",
                    className="input__heading",
                ),
                dcc.Input(
                    id="red-level",
                    placeholder="Mean threshold for metric status in red",
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
        html.Div(
            id="alert"
        ),
    ],
    className="container__1",

)

@app.callback(
    Output("selected_metric","options"),
    Input("life-dimension", "value"),
    State("show-disabled", "on")
)
def load_options(dimension , on):
    return format_options(ds.getAllMetricNames(current_user.name, dimension, on))

@app.callback(
    Output("metric", "value"),
    Output("metric-type", "value"),
    Output("description", "value"),
    Output("allowed-values", "value"),
    Output("enabled", "on"),
    Output("green-level", "value"),
    Output("red-level", "value"),
    Input("selected_metric", "value"),
    prevent_initial_call=True
)
def select_metric_to_update(value):
    user = current_user.name
    metricData = ds.getMetric(value, user)
    if metricData is None:
        return None, None, None, None, None, None, None
    print(metricData)
    return metricData[1], metricData[2], metricData[3], metricData[4], metricData[5], metricData[7] , metricData[8]


@app.callback(
    Output("alert", "children"),
    Output("selected_metric", "value"),
    Input("submit-metric", "n_clicks"),
    State("metric", "value"),
    State("metric-type", "value"),
    State("description", "value"),
    State("allowed-values", "value"),
    State("enabled", "on"),
    State("life-dimension" , "value"),
    State("green-level", "value"),
    State("red-level", "value"),
    prevent_initial_call=True
)
def add_metric_to_db(n_clicks, metric, metric_type, description, allowed_values, enabled , dimension, green, red):
    user = current_user.name
    if not n_clicks:
        return '', ''
    if metric is None or len(metric) == 0:
        return dbc.Alert(
            "Metric Name Cannot be blank",
            id="alert-auto",
            is_open=True,
            duration=4000,
        ), ''
    if metric_type is None or len(metric_type) == 0:
        return dbc.Alert(
            "Metric Type Cannot be blank",
            id="alert-auto",
            is_open=True,
            duration=4000,
        ), ''
    if metric_type == 'Enum':
        values = allowed_values.split(",")
        if len(values) < 2:
            return dbc.Alert(
                "Invalid allowed values for Enum Type",
                id="alert-auto",
                is_open=True,
                duration=4000,
            ), ''
    else:
        if metric_type != 'Boolean':
            if len(allowed_values) > 0 and not allowed_values.isnumeric():
                return dbc.Alert(
                    "Maximum Value for number field should be a number",
                    id="alert-auto",
                    is_open=True,
                    duration=4000,
                ), ''
    print(n_clicks)

    metric_entry = {
        "metric": metric,
        "user": user,
        "metric_type": metric_type,
        "description": description,
        "allowed_values": allowed_values,
        "enabled": enabled,
        "dimension" : dimension,
        "green" : green,
        "red" : red
    }
    insert_entry = ds.upsertMetric(metric_entry)
    return dbc.Alert(
        "Metric updated successfully!",
        id="alert-auto",
        is_open=True,
        duration=4000,
    ), ''
