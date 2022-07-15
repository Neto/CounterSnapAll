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

grTot = grapf1.total
grEm = grapf1.emailC
grYB = grapf1.youtube
grYL = grapf1.youtubeL
grTB = grapf1.twitter
grTL = grapf1.twitterL
grIB = grapf1.instagram
grIL = grapf1.instagramL

plt.plot(grapf1.date,grapf1.grYB)
plt.plot(grapf1.date,grapf1.grYL)
plt.plot(grapf1.date,grapf1.grTB)
plt.plot(grapf1.date,grapf1.grTL)
plt.plot(grapf1.date,grapf1.grIB)
plt.plot(grapf1.date,grapf1.grIL)
plt.plot(grapf1.date,grTot)


# TOTAL
ax = plt.gca()
plt.title("Snapdragon Followers TOTAL - Brazil & Latam")
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


#plt.show()







      