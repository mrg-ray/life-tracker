from datetime import date, timedelta, datetime
import dash_daq as daq
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
import contants as const

ds = DataStore()

menuSlider = html.Div([
    dbc.Row(
        dcc.DatePickerRange(
            id='date-range',
            max_date_allowed=date.today(),
            initial_visible_month=date.today() - timedelta(days=30),
            end_date=date.today(),
            start_date=date.today() - timedelta(days=30),
        )
    )],
    className="date-range",
)


def metric_display(name, data, score, total, duration):
    weekly_series = data.groupby(pd.Grouper(freq='W', key='date'))['value'].sum()
    weekly_data = pd.DataFrame()
    weekly_data['date'] = weekly_series.index
    weekly_data['value'] = weekly_series.values
    # weekly_data['date'] = weekly_data.index
    cols = []
    perf = str(total) + " / " + str(duration)
    if score == 2:
        metric_status = "status-green"
    elif score == 0:
        metric_status = "status-red"
    elif score == 1:
        metric_status = "status-yellow"
    info = dbc.Col([
        html.Div([
            dbc.Row(dbc.Col(html.H3(children=name))),
            dbc.Row(dbc.Col(html.H4(children="Performance:" + perf))),
            dbc.Row(dbc.Col(html.H4(children="Expected: 100%")))
        ],
            className="metric-performance "
        ),
    ])
    cols.append(info)
    fig = px.bar(weekly_data, x='date', y='value')
    cols.append(dbc.Col(dcc.Graph(config={"displayModeBar": False}, figure=fig)))
    # return cols
    return html.Div(dbc.Row(children=cols), className=metric_status)


def tracker_health(start, end):
    data = ds.loadTrackerDataByName(current_user.name, "tracker_tracker", start, end)
    data['date'] = pd.to_datetime(data['date'])
    total = data.shape[0]
    d1 = datetime.strptime(start, "%Y-%m-%d")
    d2 = datetime.strptime(end, "%Y-%m-%d")
    duration = (d2 - d1).days
    perf = total / duration
    if perf < .9:
        score = 0
    elif perf < 1:
        score = 1
    else:
        score = 2
    return metric_display("Tracker Health", data, score, total, duration)


baseReportLayout = html.Div([
    dcc.Tabs(id="reports-tab", value="dimension-report", children=[
        dcc.Tab(label="Metric Health", value="dimension-report", id="dimension-report"),
        dcc.Tab(label="Time Management", value="time-management")
    ]),
    html.Div(id="report-content", className="app-page")
])


def time_management(user, start_date, end_date):
    rows = []
    tracker = ds.loadTrackerData(user, start_date, end_date)
    time_data = tracker[tracker['metric_type'] == const.hr]
    fig = px.sunburst(time_data, path=['dimension', 'metric'], values='value')
    fig.layout.height = 600
    rows.append(dbc.Row([dcc.Graph(id="time-burst", config={"displayModeBar": True}, figure=fig)]))
    rows.append(dbc.Row(id="tracker-health", children=tracker_health(start_date, end_date)))
    return rows


def dimension_report(user, start_date, end_date):
    rows = []
    data = ds.loadTrackerData(user, start_date, end_date)
    data['date'] = pd.to_datetime(data['date'])
    metric_agg = metric_perf(data)
    dim_data = dimension_perf(metric_agg)
    cols = []
    rows.append(dbc.Row(cols))
    i = 0
    for index, dimension in dim_data.iterrows():
        scaled_dim = dimension['value'] * (100 / dimension['total'])
        if i % 2 == 0:
            cols = []
            rows.append(dbc.Row(cols))
        gauge = daq.Gauge(
            color={"gradient": True, "ranges": {"red": [0, 60], "yellow": [60, 80], "green": [80, 100]}},
            value=scaled_dim,
            label=index,
            max=100,
            min=0,
        )
        cols.append(dbc.Col(gauge))
        i += 1
    return rows


@app.callback(
    Output("report-content", "children"),
    Input("reports-tab", "value"),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date')
)
def baseData(tab, start_date, end_date):
    user = current_user.name
    if tab == "time-management":
        return time_management(user, start_date, end_date)
    if tab == "dimension-report":
        return dimension_report(user, start_date, end_date)


def score_metric(perf, green, red):
    if green > red:
        # positive metric
        if perf >= green:
            return 2
        elif perf <= red:
            return 0
        else:
            return 1
    else:
        # negetive metric
        if perf <= green:
            return 2
        elif perf >= red:
            return 0
        else:
            return 1


def metric_perf(data):
    metric_agg = data.groupby('metric').agg(
        total=('value', sum),
        duration=("date", lambda x: (max(x) - min(x)).days),
        green=('green', max),
        red=('red', max),
        period=('tracking_period', max),
        dimension=('dimension', max)
    )
    metric_agg['perf'] = metric_agg['total'] / (metric_agg['duration'] / metric_agg['period'])
    metric_agg['score'] = metric_agg.apply(lambda x: score_metric(x['perf'], x['green'], x['red']), axis=1)
    return metric_agg


def dimension_perf(data):
    agg = data.groupby('dimension').agg(
        value=('score', sum),
        total=('score', "count")
    )
    agg['total'] = agg['total'] * 2
    return agg


if __name__ == '__main__':
    ds = DataStore()
    data = ds.loadTrackerData("MrG", '2022-01-01', '2022-10-30')
    data['date'] = pd.to_datetime(data['date'])
    metric_agg = metric_perf(data)
    dim_agg = dimension_perf(metric_agg)
    print(metric_agg)
    print(dim_agg)
