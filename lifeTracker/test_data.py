from lifeTracker.data_store import DataStore
import contants as const
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
if __name__ == '__main__':
    ds = DataStore()
    #
    ds.upsertMetric({"metric": "Workout","user": "MrG","metric_type": const.bool,"description": "Workout?","allowed_values": None,"enabled": 1 , "dimension" : const.health, "green": 4, "red": 2, "tracking_period": 7})
    ds.upsertMetric({"metric": "#Drinks","user": "MrG","metric_type": const.num,"description": "# Drinks today","allowed_values": None,"enabled": 1 , "dimension" : const.health , "green" : 2 , "red" : 4, "tracking_period" : 7})
    ds.upsertMetric({"metric": "Tech Learning","user": "MrG","metric_type": const.hr,"description": "# Hours on tech learning","allowed_values": None,"enabled": 1 , "dimension" : const.personal_growth , "green": 14, "red": 8, "tracking_period": 7})
    ds.upsertMetric({"metric": "Sex Learning","user": "MrG","metric_type": const.hr,"description": "# Hours on sex learning","allowed_values": None,"enabled": 1 , "dimension" : const.personal_growth , "green": 8, "red": 4, "tracking_period": 30})

    ds.upsertMetric({"metric": "TimeWithMax","user": "MrG","metric_type": const.hr,"description": "Time with Max?","allowed_values": None,"enabled": 1 , "dimension" : const.family_matters , "green": 4, "red": 2, "tracking_period": 7})
    ds.upsertMetric({"metric": "Time With Candy","user": "MrG","metric_type": const.hr,"description": "Time with Candy?","allowed_values": None,"enabled": 1 , "dimension" : const.family_matters , "green": 4, "red": 2, "tracking_period": 7})

    ds.upsertMetric({"metric": "Sex", "user": "MrG", "metric_type": const.num, "description": "#Sex",
                     "allowed_values": None, "enabled": 1, "dimension": const.sex, "green": 30, "red": 20, "tracking_period": 30})
    ds.upsertMetric({"metric": "Date Night", "user": "MrG", "metric_type": const.num, "description": "Is it a Date Night",
                     "allowed_values": None, "enabled": 1, "dimension": const.sex, "green": 2, "red": 0, "tracking_period": 30})
    ds.upsertMetric({"metric": "Meetings", "user": "MrG", "metric_type": const.hr, "description": "Time spent in Meetings",
                     "allowed_values": None, "enabled": 1, "dimension": const.professional_growth, "green": 5, "red": 10, "tracking_period": 7})
    ds.upsertMetric(
        {"metric": "Investment Knowledge", "user": "MrG", "metric_type": const.hr, "description": "Time spent on managing investments",
         "allowed_values": None, "enabled": 1, "dimension": const.wealth, "green": 4, "red": 2, "tracking_period": 7})

    # create tracker data
    end = datetime.today().date()
    recent_start = end - timedelta(days=20)
    half_start = end - timedelta(days=90)
    quarter_start = end - timedelta(days=45)
    start = end - timedelta(days=180)

    df = pd.DataFrame()
    df['date'] = pd.date_range(recent_start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "Investment Knowledge"
    df['value'] = np.random.randint(0,3, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='replace' , index=False)

    df = pd.DataFrame()
    df['date'] = pd.date_range(start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "Meetings"
    df['value'] = np.random.randint(0, 3, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)

    df = pd.DataFrame()
    df['date'] = pd.date_range(quarter_start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "Date Night"
    df['value'] = np.random.randint(0, 1, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)

    df = pd.DataFrame()
    df['date'] = pd.date_range(half_start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "Sex"
    df['value'] = np.random.randint(0, 2, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)

    df = pd.DataFrame()
    df['date'] = pd.date_range(half_start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "Time With Candy"
    df['value'] = np.random.randint(0, 2, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)

    df = pd.DataFrame()
    df['date'] = pd.date_range(half_start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "TimeWithMax"
    df['value'] = np.random.randint(0, 2, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)

    df = pd.DataFrame()
    df['date'] = pd.date_range(half_start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "Sex Learning"
    df['value'] = np.random.randint(0, 2, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)

    df = pd.DataFrame()
    df['date'] = pd.date_range(start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "Tech Learning"
    df['value'] = np.random.randint(1, 5, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)

    df = pd.DataFrame()
    df['date'] = pd.date_range(start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "#Drinks"
    df['value'] = np.random.randint(0, 2, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)

    df = pd.DataFrame()
    df['date'] = pd.date_range(start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "Workout"
    df['value'] = np.random.randint(0, 2, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)


    df = pd.DataFrame()
    df['date'] = pd.date_range(start, end, freq='d')
    df['user'] = "MrG"
    df['metric'] = "tracker_tracker"
    df['value'] = np.random.randint(0, 2, size=len(df))
    df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)

    ds.createUser("MrG" , "12345" , "MrG")
    ds.createUser("bubbles", "12345", "bubbles")
