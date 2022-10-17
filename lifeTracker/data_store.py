from datetime import datetime

import sqlalchemy as db
import pandas as pd
from pandas.core.common import flatten
from sqlalchemy.exc import IntegrityError

db_url = "sqlite:///data_entry.db"



# SQL Engine
class DataStore:


    db_engine = db.create_engine(
        db_url, connect_args={"check_same_thread": False}
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

    Users = db.Table(
        "users",
        metadata,
        db.Column("id",db.Integer, primary_key=True),
        db.Column("username",db.String(15), unique=True, nullable=False),
        db.Column("email",db.String(50), unique=True),
        db.Column("password",db.String(80)),
    )

    metadata.create_all(db_engine)

    def getUserByName(self , username):
        df = pd.read_sql_query("select * from users where username = ?", self.connection, params=[username])
        return df.values

    def getUserById(self , id):
        df = pd.read_sql_query("select * from users where id = ?", self.connection, params=[id])
        return df.values
    def upsertMetric(self, metric_entry):
        try:
            self.db_engine.execute(self.MetricTable.insert().values(metric_entry))
        except IntegrityError:
            self.db_engine.execute(
                self.MetricTable.update().where(self.MetricTable.columns.metric == metric_entry['metric'],
                                                self.MetricTable.columns.user == metric_entry['user']).values(
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
        return df

    def upsertMetricTracker(self, date, user, metric_name, metric_value):
        try:
            dateObj = datetime.strptime(date, '%Y-%m-%d')
            self.db_engine.execute(self.TrackerData.insert().values([user, metric_name, dateObj, metric_value]))
        except IntegrityError:
            self.db_engine.execute(
                self.TrackerData.update().where(self.TrackerData.columns.metric == metric_name,
                                                self.TrackerData.columns.date == date,
                                                self.TrackerData.columns.user == user)
                .values({'value': metric_value}))

    def getTrackerForGivenDate(self, user, selected_date, metric_name):
        params = tuple(flatten((user, selected_date, metric_name)))
        df = pd.read_sql_query("select value from tracker_data where user = ? and date = ? and  metric = ?",
                               self.connection,
                               params=params)
        return df.values

    def getAllValuesForEnum(self, user, param):
        df = pd.read_sql_query("select allowed_values from metrics where user = ? and metric = ?", self.connection,
                               params=[user, param])
        return df.values[0].split(",")

    def loadTrackerData(self, user):
        return pd.read_sql_query("select * from tracker_data where user = ?", self.connection,
                                 params=[user])

    def createUser(self, username, password, email):
        try:
            self.db_engine.execute(self.Users.insert().values([{"username":username, "password":password, "email":email}]))
        except IntegrityError:
            self.db_engine.execute(
                self.Users.update().where(self.Users.columns.username == username)
                .values({'password': password}))