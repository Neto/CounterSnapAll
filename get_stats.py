from time import sleep
from tokenize import String
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from datetime import date, datetime
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from turtle import clear
import sqlite3
import instaloader
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




def save_data(emailC, youtube, youtubeL, twitter, instagram, twitterL, instagramL, total):

  # Prepare data for saving
  record = {
    'date': int(datetime.now().strftime('%s')),
    'emailC': emailC,
    'youtube': youtube,
    'youtubeL': youtubeL,
    'twitter': twitter,
    'instagram': instagram,
    'twitterL': twitterL,
    'instagramL': instagramL,
    'total':total
  }

  # Connect to the database
  con = sqlite3.connect('followers.db')
  cur = con.cursor()

  cur.execute('''
    CREATE TABLE IF NOT EXISTS monthly_stats (
      date INTEGER, emailC TEXT, youtube TEXT, youtubeL TEXT, twitter TEXT, instagram TEXT, twitterL TEXT, instagramL TEXT, total TEXT
    )
  ''')

  insert = cur.execute(
    'INSERT INTO monthly_stats VALUES (%s,"%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
      record['date'], record['emailC'],record['youtube'], record['youtubeL'],record['twitter'], record['instagram'], record['twitterL'], record['instagramL'], record['total']
    )
  )

  con.commit()
  con.close()

# BROWSER AUTOMATION

# Setup webdriver
options = Options()
options.add_argument('--headless')
s = Service('/Users/neto/ARDUINO/CounterSnapAll/geckodriver')
driver = webdriver.Firefox(service=s, options=options)
driver.implicitly_wait(10)

#BRASIL

with sync_playwright() as p:
    browser = p.chromium.launch(headless = True, slow_mo=50)
    page = browser.new_page()
    page.goto('https://app.rdstation.com.br/leads?segmentation_list=6496060')
    page.fill('input#email','neto@spinoff.digital')
    page.fill('input#password','061231(RDStation)')
    page.click('button[type=submit]')
    page.is_visible('div.leads_crm')
    html = page.inner_html('#content')
    soup = BeautifulSoup(html,'html.parser')   
    infos_selector = soup.find_all('div', class_='col-xs-5')
    for info_selector in infos_selector:
        right_div = info_selector.find('span', class_='btn-height-sm')
        if right_div:
            email_info = right_div.get_text()
            emailNoSpape = email_info.split('\n          ')[1]
            email_number = emailNoSpape.split('.')[0]
            email_decimal = (email_info.split('.')[1])[0]
            email_count = email_number + "." + email_decimal + "K"
            
#YouTube
driver.get('https://www.youtube.com/c/SnapdragonBrasil')
youtube_count = driver.find_element(By.ID,'subscriber-count').text.split(' ')[0]
youtube_mil = youtube_count.split('.')[0]
youtube_dec = (youtube_count.split('.')[1])[0]
youtube_count = youtube_mil + "." + youtube_dec + "K"

#YouTubeL
driver.get('https://www.youtube.com/c/SnapdragonLatam')
youtube_countL = driver.find_element(By.ID,'subscriber-count').text.split(' ')[0]
youtube_milL = youtube_countL.split('.')[0]
youtube_decL = (youtube_countL.split('.')[1])[0]
youtube_countL = youtube_milL + "." + youtube_decL + "K"

# Get Twitter followers
driver.get('https://twitter.com/snapdragon_BRA')
twitter_count = driver.find_element(By.CSS_SELECTOR,'a[href="/snapdragon_BRA/followers"] > span > span').text

# Get Instagram followers BR e LATAM at the same time to avoid Instagram block

L = instaloader.Instaloader()
#user = "neto_netohouse"
#password = "061231NetoHouse"
#L.login(user, password)
profile = instaloader.Profile.from_username(L.context, "snapdragon_brasil")
profile2 = instaloader.Profile.from_username(L.context, "snapdragon_latam")

instaBR_mil = str(profile.followers)[:2]
instaBR_dec = str(profile.followers)[2]
instagram_count = instaBR_mil + "." + instaBR_dec + "K"

instaLT_mil = str(profile2.followers)[:2]
instaLT_dec = str(profile2.followers)[2]
instagram_countL = instaLT_mil + "." + instaLT_dec + "K"

#LATAM 

# Get Twitter followers LATAM
driver.get('https://twitter.com/snapdragon_LAT')
twitter_countL = driver.find_element(By.CSS_SELECTOR,'a[href="/snapdragon_LAT/followers"] > span > span').text

# Close webdriver
sleep(5)
driver.close()

emailNumber = float(email_count.split('K')[0])
youtubeBrNumber = float(youtube_count.split('K')[0])
youtubeLNumber = float(youtube_countL.split('K')[0])

twitterBrNumber = float(twitter_count.split('K')[0])
twitterLtNumber = float(twitter_countL.split('K')[0]) 

instaBrNumber = float(instagram_count.split('K')[0])
instagram_count = str(instaBrNumber) + "K"

instaLtNumber = float(instagram_countL.split('K')[0])
instagram_countL = str(instaLtNumber) + "K"

totalFF = emailNumber + youtubeBrNumber + (youtubeLNumber/1000) + instaBrNumber + twitterBrNumber + instaLtNumber + twitterLtNumber
totalFF = round(totalFF,1)
totalFFS = str(totalFF) + "K"

# Save the data
save_data(email_count, youtube_count, youtube_countL, twitter_count, instagram_count, twitter_countL, instagram_countL, totalFFS)


#SAVE GRAPHIC
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
every_nth = 3
for n, label in enumerate(ax.yaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
every_nth2 = 3
for n, label2 in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth2 != 0:
        label2.set_visible(False)

ax.invert_xaxis()
ax.invert_yaxis()
ax.set_facecolor('white')

plt.savefig('/Library/WebServer/Documents/Spinoff/graphic.png')