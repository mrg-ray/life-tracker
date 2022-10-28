import dash_core_components as dcc
import dash_html_components as html

# Import Bootstrap components
import dash_bootstrap_components as dbc

from flask_login import current_user

from lifeTracker.data_store import DataStore

from dash.dependencies import Input, Output, State

from lifeTracker.trackerapp import app
import plotly.express as px
import pandas as pd
ds = DataStore()


menuSlider = html.Div(
    [
        dbc.Row(
            dbc.Col(
                dcc.Slider(
                    id="period-slider",
                    min=1,
                    max=24,
                    step=1,
                    tooltip={"always_visible": False, "placement": "bottom"},
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    style={"font-size": "16px", "opacity": "70%"},
                    children="Select the time range for report (In Weeks)",
                )
            )
        ),
    ],
    className="era-slider",
)


# Layout for Team Analysis page
def genTimeMetricsGraphs():
    pass


def genBooleanMetricGraphs():
    pass


def genEnumMetricsGraph():
    pass
@app.callback(
    Output("time-pie", "figure"),
    Input("period-slider", "value")
)
def baseData(value):
    user = current_user.name
    tracker = ds.loadTrackerData(user)
    metrics = ds.getAllMetrics(user)
    joined_data = pd.merge(tracker, metrics, left_on=['metric', 'user'], right_on=['metric', 'user'], how='left')
    joined_data = joined_data.filter('metric_type' == "Hour")
    fig = px.pie(joined_data, values='value', names='metric', hole=.3)
    return fig


baseReportLayout = html.Div(
    [
        dbc.Row(dbc.Col(html.H3(children="Time Share"))),
        # Display Championship titles in datatable
        dbc.Row(dbc.Col(html.H4(children="Pitching Performance"))),
        dbc.Row(
            [
                # Pie Chart, % of Completed Games, Shutouts, and Saves of Total Games played
                dbc.Col(dcc.Graph(id="time-pie", config={"displayModeBar": False})),
                # Line graph of K/BB ratio with ERA bubbles
                dbc.Col(dcc.Graph(id="time-bar", config={"displayModeBar": False}))
            ],
        ),
        html.Div(id="time-graphs", children=genTimeMetricsGraphs()),
        html.Div(id="bool-graphs", children=genBooleanMetricGraphs()),
        html.Div(id="enum-graphs", children=genEnumMetricsGraph())
    ],
    className="app-page",
)

# @app.callback(
#     Output("time-graphs", "value"),
#     #Output("time-bar", "value"),
#     #Output("description", "value"),
#     #Output("allowed-values", "value"),
#     #Output("enabled", "on"),
#     Input("selected_metric", "value"),
# )
# def select_metric_to_update(value):
#
#     metricData = ds.getMetric(value, user)
#     if metricData is None:
#         return None, None, None, None, None
#     print(metricData)
#     return metricData[1], metricData[2], metricData[3], metricData[4], metricData[5]
