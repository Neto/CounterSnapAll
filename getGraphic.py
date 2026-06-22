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

grEm = grapf1.emailC
grYB = grapf1.youtube
grYL = grapf1.youtubeL
grTB = grapf1.twitter
grTL = grapf1.twitterL
grIB = grapf1.instagram
grIL = grapf1.instagramL
grT = grapf1.total

# EMAIL
plt.clf()
plt.title("Snapdragon Followers Email - Brazil")
plt.plot(grapf1.date,grapf1.emailC)
ax = plt.gca()
every_nth = 2
for n, label in enumerate(ax.yaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
every_nth2 = 5
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth2 != 0:
        label.set_visible(False)
ax.invert_xaxis()
ax.invert_yaxis()
ax.set_facecolor('white')
plt.savefig('/Library/WebServer/Documents/Spinoff/graphicEm.png')

# YOUTUBE BR
plt.clf()
plt.title("Snapdragon Followers YouTube - Brazil")
plt.plot(grapf1.date,grYB)
ax = plt.gca()
every_nth = 2
for n, label in enumerate(ax.yaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
every_nth2 = 5
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth2 != 0:
        label.set_visible(False)
ax.invert_xaxis()
ax.invert_yaxis()
ax.set_facecolor('white')
plt.savefig('/Library/WebServer/Documents/Spinoff/graphicYB.png')

# YOUTUBE LT
plt.clf()
plt.title("Snapdragon Followers Youtube - Latam")
plt.plot(grapf1.date,grYL)
ax = plt.gca()
every_nth = 2
for n, label in enumerate(ax.yaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
every_nth2 = 5
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth2 != 0:
        label.set_visible(False)
ax.invert_xaxis()
ax.invert_yaxis()
ax.set_facecolor('white')
plt.savefig('/Library/WebServer/Documents/Spinoff/graphicYL.png')



# TWITTER BR
plt.clf()
plt.title("Snapdragon Followers Twitter - Brazil")
plt.plot(grapf1.date,grTB)
ax = plt.gca()
every_nth = 2
for n, label in enumerate(ax.yaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
every_nth2 = 5
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth2 != 0:
        label.set_visible(False)
ax.invert_xaxis()
ax.invert_yaxis()
ax.set_facecolor('white')
plt.savefig('/Library/WebServer/Documents/Spinoff/graphicTB.png')

# EMAIL
plt.clf()
plt.title("Snapdragon Followers Twitter - Latam")
plt.plot(grapf1.date,grTL)
ax = plt.gca()
every_nth = 2
for n, label in enumerate(ax.yaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
every_nth2 = 5
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth2 != 0:
        label.set_visible(False)
ax.invert_xaxis()
ax.invert_yaxis()
ax.set_facecolor('white')
plt.savefig('/Library/WebServer/Documents/Spinoff/graphicTL.png')

# INSTAGRAM BR
plt.clf()
plt.title("Snapdragon Followers Instagram - Brazil")
plt.plot(grapf1.date,grIB)
ax = plt.gca()
every_nth = 2
for n, label in enumerate(ax.yaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
every_nth2 = 5
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth2 != 0:
        label.set_visible(False)
ax.invert_xaxis()
ax.invert_yaxis()
ax.set_facecolor('white')
plt.savefig('/Library/WebServer/Documents/Spinoff/graphicIB.png')

# INSTAGRAM LT
plt.clf()
plt.title("Snapdragon Followers Instagram - Latam")
plt.plot(grapf1.date,grIL)
ax = plt.gca()
every_nth = 2
for n, label in enumerate(ax.yaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
every_nth2 = 5
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth2 != 0:
        label.set_visible(False)
ax.invert_xaxis()
ax.invert_yaxis()
ax.set_facecolor('white')
plt.savefig('/Library/WebServer/Documents/Spinoff/graphicIL.png')


# TOTAL
plt.clf()
plt.title("Snapdragon Followers Total - Brazil & Latam")
plt.plot(grapf1.date,grT)
ax = plt.gca()
every_nth = 2
for n, label in enumerate(ax.yaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
every_nth2 = 5
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth2 != 0:
        label.set_visible(False)
ax.invert_xaxis()
ax.invert_yaxis()
ax.set_facecolor('white')
plt.savefig('/Library/WebServer/Documents/Spinoff/graphicT.png')


#plt.show()







      