from data_store import DataStore
import contants as const
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
if __name__ == '__main__':
    ds = DataStore()

    #MrG
    #health Metrics
    ds.upsertMetric({"metric": "#Coffee Shots","description": "#Coffee Shots","metric_type": const.num, "green": 30, "red": 40, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "#Nocotine Tabs","description": "#Nocotine Tabs", "metric_type": const.num, "green": 20, "red": 30, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Morning Supplements","description": "Morning Supplements", "metric_type": const.bool, "green": 7, "red": 5, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Night Supplements","description": "Night Supplements", "metric_type": const.bool, "green": 7, "red": 5, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Post lunch Supplements","description": "Post lunch Supplements", "metric_type": const.bool, "green": 7, "red": 5, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "IF Schedule","description": "IF Schedule", "metric_type": const.bool, "green": 7, "red": 5, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Mindfulness","description": "Mindfulness", "metric_type": const.bool, "green": 1, "red": -1, "dimension": const.health, "tracking_period": 7, "user": "MrG", "enabled": 1})

    #Time Management
    ds.upsertMetric({"metric": "Workout","description": "Workout", "metric_type": const.hr, "green": 7, "red": 5, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Office Work","description": "Office Work", "metric_type": const.hr, "green": 25, "red": 15, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Tech Learning","description": "Tech Learning", "metric_type": const.hr, "green": 12, "red": 6, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Personal Learning","description": "Personal Learning", "metric_type": const.hr, "green": 12, "red": 6, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Sleep","description": "Sleep", "metric_type": const.hr, "green": 42, "red": 40, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Book Reading","description": "Book Reading", "metric_type": const.hr, "green": 6, "red": 4, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "G-Zone Plan","description": "G-Zone Plan", "metric_type": const.hr, "green": 3, "red": 1, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "G-Zone Time","description": "G-Zone Time", "metric_type": const.hr, "green": 10, "red": 6, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Time With Candy","description": "Time With Candy", "metric_type": const.hr, "green": 3, "red": 1, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Time With Max","description": "Time With Max", "metric_type": const.hr, "green": 3, "red": 1, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Tech Lesson 4 bubbles","description": "Tech Lesson 4 bubbles", "metric_type": const.hr, "green": 3, "red": 1, "dimension": const.tm, "tracking_period": 7, "user": "MrG", "enabled": 1})

    #Office
    ds.upsertMetric({"metric": "1-on-1","description": "1-on-1", "metric_type": const.num, "green": 1, "red": .7, "dimension": const.professional_growth, "tracking_period": 7, "user": "MrG", "enabled": 1})

    #Personal
    ds.upsertMetric({"metric": "Family Outing","description": "Family Outing", "metric_type": const.bool, "green": 4, "red": 2, "dimension": const.personal_growth, "tracking_period": 30, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Movie Sunday","description": "Movie Sunday", "metric_type": const.bool, "green": 4, "red": 2, "dimension": const.personal_growth, "tracking_period": 30, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Date Night","description": "Date Night", "metric_type": const.bool, "green": 4, "red": 2, "dimension": const.personal_growth, "tracking_period": 30, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Movie Night with bubbles","description": "Movie Night with bubbles", "metric_type": const.bool, "green": 4, "red": 2, "dimension": const.personal_growth, "tracking_period": 30, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Journal","description": "Journal", "metric_type": const.bool, "green": 7, "red": 6, "dimension": const.personal_growth, "tracking_period": 30, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Daily Plan","description": "Daily Plan", "metric_type": const.bool, "green": 7, "red": 6, "dimension": const.personal_growth, "tracking_period": 30, "user": "MrG", "enabled": 1})

    #Expenses
    ds.upsertMetric({"metric": "Food-OrderIn","description": "Food-OrderIn", "metric_type": const.num, "green": 5000, "red": 10000, "dimension": const.expenses, "tracking_period": 30, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Restaurant","description": "Restaurant", "metric_type": const.num, "green": 15000, "red": 25000, "dimension": const.expenses, "tracking_period": 30, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Personal","description": "Personal", "metric_type": const.num, "green": 5000, "red": 15000, "dimension": const.expenses, "tracking_period": 30, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Misc","description": "Misc", "metric_type": const.num, "green": 5000, "red": 10000, "dimension": const.expenses, "tracking_period": 30, "user": "MrG", "enabled": 1})

    #Habits
    ds.upsertMetric({"metric": "Smoking","description": "Smoking", "metric_type": const.bool, "green": 0, "red": 2, "dimension": const.habits, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Alcohol","description": "Alcohol", "metric_type": const.bool, "green": 0, "red": 2, "dimension": const.habits, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Sugar","description": "Sugar", "metric_type": const.bool, "green": 1, "red": 3, "dimension": const.habits, "tracking_period": 7, "user": "MrG", "enabled": 1})
    ds.upsertMetric({"metric": "Junk Food","description": "Junk Food", "metric_type": const.bool, "green": 1, "red": 3, "dimension": const.habits, "tracking_period": 7, "user": "MrG", "enabled": 1})






    # #bubbles
    # #health Metrics
    # ds.upsertMetric(
    #     {"metric": "Workout","description": "Workout", "description": "Worked Out Today?", "metric_type": const.bool, "green": 4, "red": 2,
    #      "dimension": const.health, "tracking_period": 7, "user": "bubbles", "enabled": 1})
    # ds.upsertMetric(
    #     {"metric": "Intermittent Fasting","description": "Intermittent Fasting", "description": "Were you able to follow intermittent fasting schedule?",
    #      "metric_type": const.bool, "green": 6, "red": 4, "dimension": const.health, "tracking_period": 7,
    #      "user": "bubbles", "enabled": 1})
    # ds.upsertMetric(
    #     {"metric": "Skincare Routine","description": "Skincare Routine", "description": "Did you follow skincare routine?",
    #      "metric_type": const.bool, "green": 6, "red": 4, "dimension": const.health, "tracking_period": 7,
    #      "user": "bubbles", "enabled": 1})
    # ds.upsertMetric(
    #     {"metric": "Bath Routine","description": "Bath Routine", "description": "Did you follow bath routine?",
    #      "metric_type": const.bool, "green": 5, "red": 3, "dimension": const.health, "tracking_period": 7,
    #      "user": "bubbles", "enabled": 1})
    # ds.upsertMetric({"metric": "Sugar Consumption","description": "Sugar Consumption", "description": "Did you consume sugary treats today?",
    #                  "metric_type": const.bool, "green": 1, "red": 3, "dimension": const.health, "tracking_period": 7,
    #                  "user": "bubbles", "enabled": 1})
    # ds.upsertMetric(
    #     {"metric": "Junk Food","description": "Junk Food", "description": "Did you eat unhealthy Junk Food Today?", "metric_type": const.bool,
    #      "green": 1, "red": 3, "dimension": const.health, "tracking_period": 7, "user": "bubbles", "enabled": 1})
    # ds.upsertMetric({"metric": "Morning Supplements","description": "Morning Supplements", "description": "Have you taken morning supplements?",
    #                  "metric_type": const.bool, "green": 7, "red": 5, "dimension": const.health, "tracking_period": 7,
    #                  "user": "bubbles", "enabled": 1})
    # ds.upsertMetric(
    #     {"metric": "Night Supplements","description": "Night Supplements", "description": "Have you taken night supplements?", "metric_type": const.bool,
    #      "green": 7, "red": 5, "dimension": const.health, "tracking_period": 7, "user": "bubbles", "enabled": 1})
    # ds.upsertMetric(
    #     {"metric": "Sleep","description": "Sleep", "description": "How many hours of sleep did you get yesterday?", "metric_type": const.hr,
    #      "green": 49, "red": 40, "dimension": const.health, "tracking_period": 7, "user": "bubbles", "enabled": 1})
    #
    #
    #
    #
    #
    # # personal growth
    # ds.upsertMetric(
    #     {"metric": "House Chores","description": "House Chores", "description": "Any time spent on household chores today?", "metric_type": const.hr,
    #      "green": 14, "red": 20, "dimension": const.personal_growth, "tracking_period": 7, "user": "bubbles",
    #      "enabled": 1})
    # ds.upsertMetric({"metric": "Tech Learning","description": "Tech Learning", "description": "How many hours you spent on new tech learning today?",
    #                  "metric_type": const.hr, "green": 21, "red": 14, "dimension": const.personal_growth,
    #                  "tracking_period": 7, "user": "bubbles", "enabled": 1})
    # ds.upsertMetric({"metric": "MrG Learning Tasks","description": "MrG Learning Tasks", "description": "Did you spend any time on learning task given by MrG?",
    #                  "metric_type": const.hr, "green": 4, "red": 2, "dimension": const.personal_growth,
    #                  "tracking_period": 7, "user": "bubbles", "enabled": 1})
    #
    # ds.upsertMetric(
    #     {"metric": "Time Wastage","description": "Time Wastage", "description": "Did you waste any time today?", "metric_type": const.hr, "green": 4,
    #      "red": 7, "dimension": const.personal_growth, "tracking_period": 7, "user": "bubbles", "enabled": 1})
    # ds.upsertMetric(
    #     {"metric": "Reflection","description": "Reflection", "description": "Daily Reflection?", "metric_type": const.bool, "green": 7,
    #      "red": 5, "dimension": const.personal_growth, "tracking_period": 7, "user": "bubbles", "enabled": 1})
    # ds.upsertMetric(
    #     {"metric": "Planning","description": "Planning", "description": "Did you plan for the day today?", "metric_type": const.bool, "green": 7,
    #      "red": 5, "dimension": const.personal_growth, "tracking_period": 7, "user": "bubbles", "enabled": 1})
    # ds.upsertMetric(
    #     {"metric": "Mindfulness","description": "Mindfulness", "description": "Did you practise mindfulness today?", "metric_type": const.bool,
    #      "green": 5, "red": 2, "dimension": const.personal_growth, "tracking_period": 7, "user": "bubbles",
    #      "enabled": 1})
    #
    # # professional
    # ds.upsertMetric(
    #     {"metric": "Meetings","description": "Meetings", "description": "How much time spent on Office Meetings today?", "metric_type": const.hr,
    #      "green": 10, "red": 15, "dimension": const.professional_growth, "tracking_period": 7, "user": "bubbles",
    #      "enabled": 1})
    # ds.upsertMetric(
    #     {"metric": "Office Work","description": "Office Work", "description": "How much time spent on real office work?", "metric_type": const.hr,
    #      "green": 14, "red": 7, "dimension": const.professional_growth, "tracking_period": 7, "user": "bubbles",
    #      "enabled": 1})
    #
    # # Expenses
    #
    #
    # ds.upsertMetric({"metric": "Personal Expenses","description": "Personal Expenses", "description": "How much money did you spend on personal expenses?",
    #                  "metric_type": const.num, "green": 2000, "red": 5000, "dimension": const.expenses,
    #                  "tracking_period": 31, "user": "bubbles", "enabled": 1, "allowed_values": 5000})
    # ds.upsertMetric({"metric": "Skincare Product Expenses","description": "Skincare Product Expenses", "description": "How much money did you spend on skincare products?",
    #                  "metric_type": const.num, "green": 2000, "red": 5000, "dimension": const.expenses,
    #                  "tracking_period": 31, "user": "bubbles", "enabled": 1, "allowed_values": 5000})
    # ds.upsertMetric({"metric": "Cosmetic Expenses","description": "Cosmetic Expenses", "description": "How much money did you spend on cosmetics?",
    #                  "metric_type": const.num, "green": 2000, "red": 5000, "dimension": const.expenses,
    #                  "tracking_period": 31, "user": "bubbles", "enabled": 1, "allowed_values": 5000})
    # ds.upsertMetric({"metric": "Clothes Purchase","description": "Clothes Purchase", "description": "How much money did you spend on buying clothes?",
    #                  "metric_type": const.num, "green": 2000, "red": 5000, "dimension": const.expenses,
    #                  "tracking_period": 31, "user": "bubbles", "enabled": 1, "allowed_values": 5000})
    # ds.upsertMetric({"metric": "Kids Expenses","description": "Kids Expenses", "description": "How much money did you spend on kids?",
    #                  "metric_type": const.num, "green": 2000, "red": 5000, "dimension": const.expenses,
    #                  "tracking_period": 31, "user": "bubbles", "enabled": 1, "allowed_values": 5000})
    # ds.upsertMetric({"metric": "Flowers","description": "Flowers", "description": "How much money did you spend on flowers?",
    #                  "metric_type": const.num, "green": 2000, "red": 5000, "dimension": const.expenses,
    #                  "tracking_period": 31, "user": "bubbles", "enabled": 1, "allowed_values": 5000})
    # ds.upsertMetric({"metric": "Personal Grooming Expenses","description": "Personal Grooming Expenses", "description": "How much money did you spend on personal grooming(Salon etc)?",
    #                  "metric_type": const.num, "green": 2000, "red": 5000, "dimension": const.expenses,
    #                  "tracking_period": 31, "user": "bubbles", "enabled": 1, "allowed_values": 5000})
    # ds.upsertMetric({"metric": "Hair/Skin Treatments", "description": "How much money did you spend on hair & skin treatments?",
    #                  "metric_type": const.num, "green": 2000, "red": 5000, "dimension": const.expenses,
    #                  "tracking_period": 31, "user": "bubbles", "enabled": 1, "allowed_values": 5000})

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
    # df.to_sql('tracker_data', ds.db_engine, if_exists='append' , index=False)
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
