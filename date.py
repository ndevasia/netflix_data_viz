import re, datetime
import pandas as pd

filepath = "C://Users/ndevasia/projects/netflix_data_viz/data/NetflixViewingHistory.csv"

def get_day_of_week(day):
	day_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
	return day_map[day]

data = pd.read_csv(filepath)
days_of_week = []
for i, j in data.iterrows(): #i is index of row, j.Title = title of show, j.Date = date of show watched
	date = j.Date
	month, day, year = date.split("/") #month, day ,year
	weekday_index = datetime.datetime(int(year), int(month), int(day)).weekday()
	weekday = get_day_of_week(weekday_index)
	days_of_week.append(weekday)


data["Day of Week"] = days_of_week
data.to_csv("data/NetflixViewingHistory.csv", index = False)