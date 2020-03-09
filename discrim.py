import pandas as pd
import numpy as np

df = pd.read_csv('data/NetflixViewingHistory.csv')
titles = df["Title"]
dates = df["Date"]
new_col = []
i = 0
titles = titles
while i < len(titles):
    dup = False
    try:
        if titles[i][:titles[i].index(":")] == titles[i+1][:titles[i+1].index(":")]:
            i += 1
            dup = True
            continue

    except (ValueError, IndexError, KeyError):
        pass



    title = titles[i]
    if ":" in title:
        title = title[:title.index(":")]
    who = input(f"Who watched {title} on {dates[i]}?:  ")
    new_col.extend([who]*(i-len(new_col)+1))
    i += 1
if dup:
    title = titles[len(titles)-1]
    if ":" in title:
        title = title[:title.index(":")]
    who = input(f"Who watched {title} on {dates[len(dates)-1]}?:  ")
    new_col.extend([who]*(len(titles)-len(new_col)))


names = {'B':'Both', "N": "Nisha", "E": 'Erik'}

df['User'] = [names[i] for i in new_col] + ['NA']*( len(dates)-len(new_col))
df.to_csv('data/NetflixViewingHistory.csv', index=False)



# df["Viewer"] = ""
# df.to_csv('NetflixViewingHistory.csv', index=False)
