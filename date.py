import re, datetime
import pandas as pd

filepath = "C://Users/ndevasia/projects/netflix_data_viz/data/NetflixViewingHistory.csv"

day_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
month_map = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

data = pd.read_csv(filepath)
days_of_week = []
weekday_dict = {}
month_dict = {}
year_dict = {}
avg_dict = {}

for i, j in data.iterrows(): #i is index of row, j.Title = title of show, j.Date = date of show watched
	date = j.Date
	month, day, year = date.split("/") #month, day ,year
	weekday_index = datetime.datetime(int(year), int(month), int(day)).weekday()
	weekday = day_map[weekday_index]
	days_of_week.append(weekday)

	try:
		weekday_dict[weekday] += 1
	except:
		weekday_dict[weekday] = 1

	try:
		month_dict[int(month)] += 1
	except:
		month_dict[int(month)] = 1

	try:
		year_dict[int(year)] += 1
	except:
		year_dict[int(year)] = 1
		
year_begin = datetime.date(2020, 1, 1)
today = datetime.date.today()
days_in_2020 = (today - year_begin).days
#maybe unhardcode this
avg_dict = {2018: year_dict[2018]/365, 2019: year_dict[2019]/365, 2020:year_dict[2020]/days_in_2020}
data["Day of Week"] = days_of_week
data.to_csv("data/NetflixViewingHistory.csv", index = False)