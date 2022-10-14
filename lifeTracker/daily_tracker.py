from datetime import date, datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc

from lifeTracker.data_store import DataStore


class DailyTracker:
    ds = DataStore()

    def createView(self, metric, user, selected_date):
        label = html.P(
                        metric[3]+" :",
                        className="input__heading",
                    )
        value = self.ds.getTrackerForGivenDate(user , selected_date , metric[1])
        metric_input=None
        if metric[2] == 'Hour' or metric[2] == 'Minute' or metric[2] == 'Number':
            if value:
                value = int(value[0])
            else:
                value = 0
            metric_input=dcc.Slider(id=metric[1], min=0, max=int(metric[4]), step=1, value=value, className="metric_value")
        if metric[2] == 'Boolean':
            if value:
                value = bool(value[0])
            else:
                value = False
            metric_input=daq.BooleanSwitch(id=metric[1], on=value, className="metric_value")
        if metric[2] == 'Enum':
            if value:
                value = value[0]
            else:
                value = None
            metric_input=dcc.RadioItems(id=metric[1], options=metric[4].split(","), className="metric_value",
                                        value='', inline=True)
        return html.Div(
            [label , metric_input],
            className="input__container",
        )

    def genform(self, user, selected_date):
        elements = []
        metrics = self.ds.getAllMetrics(user)
        for metric in metrics:
            elements.append(self.createView(metric, user, selected_date))
        return elements

    def addTrackerData(self, user, selected_date, values):
        for value in values:
            for entry in value.get("props").get("children"):
                item = entry.get("props")
                if item.get("className") == "metric_value":
                    metricName = item.get("id")
                    metric = self.ds.getMetric(user=user, metric=metricName)
                    if metric[2] == 'Boolean':
                        metricValue = item.get("on")
                    else:
                        metricValue = item.get("value")
                    print(metricValue)
                    self.ds.upsertMetricTracker(selected_date, user, metricName, metricValue)
        return
