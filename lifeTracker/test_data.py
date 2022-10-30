from data_store import DataStore
import contants as const
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
if __name__ == '__main__':
    ds = DataStore()

    #health Metrics
    ds.upsertMetric({"metric": "Workout", "description": "Worked Out Today?", "metric_type": const.bool, "green": 4, "red": 2, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Intermittent Fasting", "description": "Were you able to follow intermittent fasting schedule?", "metric_type": const.bool, "green": 6, "red": 4, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "#Drinks", "description": "How many alcoholic drinks you had today?", "metric_type": const.num, "green": 2, "red": 4, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "#Smokes", "description": "Did you smoke today How many?", "metric_type": const.num, "green": 0, "red": 3, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Sugar Consumption", "description": "Did you consume sugary treats today?", "metric_type": const.bool, "green": 1, "red": 3, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Junk Food", "description": "Did you eat unhealthy Junk Food Today?", "metric_type": const.bool, "green": 1, "red": 3, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Morning Supplements", "description": "Have you taken morning supplements?", "metric_type": const.bool, "green": 7, "red": 5, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Night Supplements", "description": "Have you taken night supplements?", "metric_type": const.bool, "green": 7, "red": 5, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Sleep", "description": "How many hours of sleep did you get last night?", "metric_type": const.hr, "green": 49, "red": 40, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})

    #Family Matters
    ds.upsertMetric({"metric": "Time With Kids", "description": "How much quality time did you spend with kids today?", "metric_type": const.hr, "green": 14, "red": 7, "dimension": const.family_matters, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Talk with Max", "description": "Did you talk to Max regarding his day/progress?", "metric_type": const.bool, "green": 6, "red": 4, "dimension": const.family_matters, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Candy's Homework", "description": "Did you help Candy with her studies today?", "metric_type": const.bool, "green": 6, "red": 4, "dimension": const.family_matters, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Time With bubbles", "description": "How much quality time you spent with bubbles today?", "metric_type": const.hr, "green": 21, "red": 14, "dimension": const.family_matters, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "House Chores", "description": "Any time spent on household chores today?", "metric_type": const.hr, "green": 7, "red": 10, "dimension": const.family_matters, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Family Fun", "description": "Any family fun (Outing, dinner, games) today?", "metric_type": const.bool, "green": 5, "red": 3, "dimension": const.family_matters, "tracking_period": 31, "user": "MrG", "enabled": 1})

    #personal growth
    ds.upsertMetric({"metric": "Tech Learning", "description": "How many hours you spent on new tech learning today?", "metric_type": const.hr, "green": 21, "red": 14, "dimension": const.personal_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Sex Learning", "description": "Did you spend any time on learning about sex?", "metric_type": const.hr, "green": 5, "red": 2, "dimension": const.personal_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Mind Nourishment", "description": "How much time you spent on nourishing your mind today(TED/books/podcast)?", "metric_type": const.hr, "green": 14, "red": 7, "dimension": const.personal_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Time Wastage", "description": "Did you waste any time today?", "metric_type": const.hr, "green": 4, "red": 7, "dimension": const.personal_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Journal", "description": "Did you write journal today?", "metric_type": const.bool, "green": 7, "red": 5, "dimension": const.personal_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Planning", "description": "Did you plan for the day today?", "metric_type": const.bool, "green": 7, "red": 5, "dimension": const.personal_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Mindfulness", "description": "Did you practise mindfullness today?", "metric_type": const.bool, "green": 5, "red": 2, "dimension": const.personal_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Book", "description": "Did you finish any book today?", "metric_type": const.bool, "green": 3, "red": 1, "dimension": const.personal_growth, "tracking_period": 31, "user": "MrG", "enabled": 1})

    #Sex-life
    ds.upsertMetric({"metric": "#Sex", "description": "How many times you made love today?", "metric_type": const.num, "green": 30, "red": 20, "dimension": const.sex, "tracking_period": 31, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Shower With bubbles", "description": "Did you take shower with bubbles today?", "metric_type": const.num, "green": 4, "red": 2, "dimension": const.sex, "tracking_period": 31, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Date Night", "description": "Was it a date night(movies, formal dinner, late night drive)?", "metric_type": const.num, "green": 3, "red": 1, "dimension": const.sex, "tracking_period": 31, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Scene", "description": "Did you plan and carried out any sex session scene today", "metric_type": const.num, "green": 2, "red": 0, "dimension": const.sex, "tracking_period": 31, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "#Sex Message", "description": "How many naughty messages you sent to bubbles today", "metric_type": const.num, "green": 15, "red": 10, "dimension": const.sex, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "#Cum On", "description": "How many time did you make bubbles cum today?", "metric_type": const.num, "green": 30, "red": 20, "dimension": const.sex, "tracking_period": 7, "user": "MrG", "enabled": 1})

    #professional
    ds.upsertMetric({"metric": "Meetings", "description": "How much time spent on Office Meetings today?", "metric_type": const.hr, "green": 10, "red": 15, "dimension": const.personal_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Team Management", "description": "How much time spent on people management today?", "metric_type": const.hr, "green": 7, "red": 10, "dimension": const.personal_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Deep Work", "description": "How much time spent on real office work?", "metric_type": const.hr, "green": 14, "red": 7, "dimension": const.personal_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})

    #Wealth
    ds.upsertMetric({"metric": "Food Expenses", "description": "How much money did you spend on food today?", "metric_type": const.num, "green": 10000, "red": 20000, "dimension": const.wealth, "tracking_period": 31, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Drinks Expenses", "description": "How much money did you spend on drinks today?", "metric_type": const.num, "green": 5000, "red": 10000, "dimension": const.wealth, "tracking_period": 31, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Personal Expenses", "description": "How much money did you spend on personal expenses?", "metric_type": const.num, "green": 10000, "red": 20000, "dimension": const.wealth, "tracking_period": 31, "user": "MrG", "enabled": 1})

    # create tracker data
    # end = datetime.today().date()
    # recent_start = end - timedelta(days=20)
    # half_start = end - timedelta(days=90)
    # quarter_start = end - timedelta(days=45)
    # start = end - timedelta(days=180)
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(recent_start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "Investment Knowledge"
    # df['value'] = np.random.randint(0,3, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='replace' , index=False)
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "Meetings"
    # df['value'] = np.random.randint(0, 3, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(quarter_start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "Date Night"
    # df['value'] = np.random.randint(0, 1, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(half_start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "Sex"
    # df['value'] = np.random.randint(0, 2, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(half_start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "Time With Candy"
    # df['value'] = np.random.randint(0, 2, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(half_start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "TimeWithMax"
    # df['value'] = np.random.randint(0, 2, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(half_start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "Sex Learning"
    # df['value'] = np.random.randint(0, 2, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "Tech Learning"
    # df['value'] = np.random.randint(1, 5, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "#Drinks"
    # df['value'] = np.random.randint(0, 2, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "Workout"
    # df['value'] = np.random.randint(0, 2, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)
    #
    #
    # df = pd.DataFrame()
    # df['date'] = pd.date_range(start, end, freq='d')
    # df['user'] = "MrG"
    # df['metric'] = "tracker_tracker"
    # df['value'] = np.random.randint(0, 2, size=len(df))
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append', index=False)

    ds.createUser("MrG" , "12345" , "MrG")
    ds.createUser("bubbles", "12345", "bubbles")
