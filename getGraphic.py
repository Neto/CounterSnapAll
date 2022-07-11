import sqlite3
from turtle import clear
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy
from datetime import date, datetime


con = sqlite3.connect('followers.db')
cur = con.cursor()

  # Create an empty list for the records
records = []

    # Get all records
all_stats = cur.execute('SELECT * FROM monthly_stats ORDER BY date DESC').fetchall()

    # Create an object ("dictionary" in Python) for each record
for item in all_stats:
    dt = datetime.fromtimestamp(item[0])
    record = {
        'date': dt.strftime('%-d %b'), # Format the date
        'emailC': item[1].split('K')[0],
        'youtube': item[2].split('K')[0],
        'youtubeL': item[3].split('K')[0],
        'twitter': item[4].split('K')[0],
        'instagram': item[5].split('K')[0],
        'twitterL': item[6].split('K')[0],
        'instagramL': item[7].split('K')[0],
        'total': item[8].split('K')[0]
      }

    records.append(record)

grapf1 = pd.DataFrame.from_dict(records)




plt.plot(grapf1.date,grapf1.total)
plt.title("Snapdragon Followers Growth - Brazil and Latam")
ax = plt.gca()
every_nth = 4
for n, label in enumerate(ax.yaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
every_nth2 = 3
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth2 != 0:
        label.set_visible(False)

ax.invert_xaxis()
ax.invert_yaxis()
ax.set_facecolor('black')

plt.show()







      