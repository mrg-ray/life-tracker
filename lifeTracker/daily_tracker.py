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
        value = self.ds.getTrackerForGivenDate(user , selected_date , metric[1])
        if metric[2] == 'Hour' or metric[2] == 'Minute' or metric[2] == 'Number':
            if value:
                value = int(value[0])
            else:
                value = 0
            return html.Div(
                [
                    dbc.Label(metric[1], html_for="Submit"),
                    dcc.Slider(id=metric[1], min=0, max=int(metric[4]), step=1, value=value, className="metric_value"),
                ],
                className="mb-3",
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
                    metricValue = item.get("value")
                    print(metricValue)
                    dateObj = datetime.strptime(selected_date, '%Y-%m-%d')
                    self.ds.upsertMetricTracker(dateObj, user, metricName, metricValue)
        return
