import sqlalchemy as db
import pandas as pd
from pandas.core.common import flatten
from sqlalchemy.exc import IntegrityError


# SQL Engine
class DataStore:
    db_engine = db.create_engine(
        "sqlite:///data_entry.db", connect_args={"check_same_thread": False}
    )
    connection = db_engine.connect()
    metadata = db.MetaData()

    MetricTable = db.Table(
        "metrics",
        metadata,
        db.Column("user", db.String(20), primary_key=True),
        db.Column("metric", db.String(99), primary_key=True),
        db.Column("metric_type", db.String(19)),
        db.Column("description", db.String(254)),
        db.Column("allowed_values", db.String(254)),
        db.Column("enabled", db.Boolean),
    )

    TrackerData = db.Table(
        "tracker_data",
        metadata,
        db.Column("user", db.String(20), primary_key=True),
        db.Column("metric", db.String(99), primary_key=True),
        db.Column("date", db.DATE, primary_key=True),
        db.Column("value", db.String(19)),
    )
    metadata.create_all(db_engine)

    def upsertMetric(self, metric_entry):
        try:
            self.db_engine.execute(self.MetricTable.insert().values(metric_entry))
        except IntegrityError:
            self.db_engine.execute(
                self.MetricTable.update().where(self.MetricTable.columns.metric == metric_entry['metric'],
                                                self.MetricTable.columns.user == metric_entry['user']).where().values(
                    metric_entry))

    def getAllMetricNames(self, user):
        df = pd.read_sql_query("select metric from metrics where user = ?", self.connection, params=[user])
        list = []
        for value in df.values:
            list.append(value[0])
        return list

    def getMetric(self, metric, user):
        if not metric:
            return
        df = pd.read_sql_query("select * from metrics where metric =? and user =?",
                               self.connection, params=[metric, user])
        return df.values[0]

    def getAllMetrics(self, user):
        df = pd.read_sql_query("select * from metrics where user = ?", self.connection, params=[user])
        return df.values

    def upsertMetricTracker(self, date, user, metric_name, metric_value):
        try:
            self.db_engine.execute(self.TrackerData.insert().values([user, metric_name, date, metric_value]))
        except IntegrityError:
            self.db_engine.execute(
                self.TrackerData.update().where(self.TrackerData.columns.metric == metric_name,
                                                self.TrackerData.columns.date == date, self.TrackerData.user == user)
                .values({'value': metric_value}))

    def getTrackerForGivenDate(self, user, selected_date, metric_name):
        params = tuple(flatten((user, selected_date, metric_name)))
        df = pd.read_sql_query("select value from tracker_data where user = ? and date = ? and  metric = ?", self.connection,
                               params=params)
        return df.values
