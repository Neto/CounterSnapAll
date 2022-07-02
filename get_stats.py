from tokenize import String
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from datetime import datetime
from bs4 import BeautifulSoup
import sqlite3
import requests
import instaloader

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
s = Service('/Users/neto/Dropbox/ARDUINO/CounterSnapAll/geckodriver')
driver = webdriver.Firefox(service=s, options=options)
driver.implicitly_wait(10)

#BRASIL

#EMail
cookies = {
    '_hjFirstSeen': '1',
    '_hjSession_2716062': 'eyJpZCI6ImMzNTA1NjUxLTcxZjItNDIxNi1hOThmLTVkYzM5OTY1YjYwNiIsImNyZWF0ZWQiOjE2NTY3MjEzMzg0NTksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_gid': 'GA1.3.2102463956.1656721339',
    'split': '%7B%22xp_ab_test%22%3A%22variant%22%2C%22caterpie_activation_strategies%22%3A%22control%22%7D',
    '_hjSession_863034': 'eyJpZCI6IjIwMzBkYTQ0LWVhMWQtNDVjMy05ZGZmLTA4ZTFkYWI1ZjVhOSIsImNyZWF0ZWQiOjE2NTY3MjEzNTA1MDEsImluU2FtcGxlIjpmYWxzZX0=',
    'NPS_efd9b1a6_last_seen': '1656721351288',
    'ajs_user_id': '682938',
    'ajs_anonymous_id': 'e9b242cf-df33-48d7-88e9-69443910ebf3',
    'ajs_group_id': '434927',
    '_hjCachedUserAttributes': 'eyJhdHRyaWJ1dGVzIjp7IkNvdW50cnlfSVBzdGFjayI6IkJSIiwiYWNjb3VudF9pZCI6IjQzNDkyNyIsImNvdW50cnlfY29kZSI6IkJSIiwiZW1haWwiOiJwZWRyb0BzcGlub2ZmLmRpZ2l0YWwiLCJsYW5ndWFnZSI6InB0LUJSIiwicGxhbiI6IlBybyIsInJvbGUiOiJBRE1JTiJ9LCJ1c2VySWQiOiI2ODI5MzgifQ==',
    'intercom-id-hq3qq4eb': '0cb31ad4-f8c7-48c3-bb60-f33578d1e461',
    'intercom-session-hq3qq4eb': '',
    'drift_aid': 'c4c145b9-e410-4aee-9da7-e34f9e8ae0e0',
    'driftt_aid': 'c4c145b9-e410-4aee-9da7-e34f9e8ae0e0',
    'drift_eid': '682938',
    '_hjSessionUser_863034': 'eyJpZCI6ImExOTM4MTg4LWVkOWEtNTgyYy04NzAxLTVmMjM4OTM4MGQ4ZCIsImNyZWF0ZWQiOjE2NTY3MjEzNDkwNTcsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjDonePolls': '761636',
    'NPS_efd9b1a6_throttle': '1656765840939',
    '_hjSessionUser_2716062': 'eyJpZCI6IjQyNTYzNTNmLTM2ODUtNWI2My04NTZlLTZmY2FlOTJhNzZjNSIsImNyZWF0ZWQiOjE2NTY3MjEzMzc4MjgsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga': 'GA1.3.1848593568.1656721339',
    '__rdsid': 'a77be6c07ef120b3ac61413a590b5aa9',
    'ak_bmsc': '379D2CCF2F3A6DB5365EC49C75DC26CC~000000000000000000000000000000~YAAQd81YaFqm0Y6BAQAAjwp0vBCnKMZKVV9CfalE8fGVV1cs1uARZyfApOsWTEza72qgcE3N/mLKpkEMfrrF6Hnzf/7r60EK+b44uWbJgs8LrZnSovreGuBopo5jSDd1CZ3E35HVHmZ3UlSg/YbuaLrwTL4GS6BUW088cKqTaIYUrRbrX+SPjnlNcjJtHWuzlxNKFwun7qvZ3T6+TPok5Nsw8j39EhQgSDeLL0Zv+GitMVKAx4IgBcOrbjqxJDnPQ9a4rGfAYoXTxCc2gwN188mGvaEHqZ2wCRP8v4Wdv+UX5CqPnS1DADI/dl8vSyVC4yJp5Eh82sycqe6HDc2X/DtR4PGTBGmTHpmcG42Ftyud3rQHJh/DFJgekU9LLMShfF5dXlnsd3Vs4RJryQi7ANPemsovE9ndM6+YVNBi294=',
    '_ga_GYGJG4ZD5K': 'GS1.1.1656721338.1.1.1656724131.0',
    '_hjIncludedInPageviewSample': '1',
    '_hjIncludedInSessionSample': '0',
    'cto_bundle': 'mY-RGl9teVhaek5yNU5XMFp5dHQySEY5aTJuejY2MkVwc1pmdEtLME9GYmlyJTJCJTJGbjA2amhVcG5vZ3dGWTUxWkppdFhEa1dFMEM3WEwzNVREN2UzZnROZHpsYlpxbUxVaSUyRkJmU3Z1b1VneWtaY2lmeUFiRkdDRHZGeGFLM25tOVlVQnZlcXlBUmp6VlphJTJCVHpFRnhEaWE0OGZicnhlN1FRbkdCeUVHbUVmUDJFYnl6MCUzRA',
    'drift_campaign_refresh': 'f028dbc3-dc6e-4dd3-abcc-a2ab975bb894',
    'bm_sv': '5579FDAA592DBE08216F7FA95BA7D206~YAAQjs1YaG+IuJeBAQAAgd51vBC7YLDkiDXKEgP3qH9xge8ZB+FVJzqAax32BHjxJLc1UvGMLbF8cibCeqVSrSojiOWTEsS2gJxcgxu4INoxqR2js1Op60lmzg2n1Jqm/jXcnCkqkXetvgkXhCwGWZbkKDDaopfBych17r8tJSzKJwUnygikQutVoBdfrjR5UPxkl8gX6URTUqh3CujceDh2yA7l7N/XyTmEJnbpqcsPSQW3+ia21jQcjtouw6b6kRsuqI4vMg==~1',
    '_uetsid': '10b954c0f99d11ec923ce1ad64c2ab4d',
    '_uetvid': '10ba2a40f99d11ec8f3d8b11afd138b5',
    '_dd_s': 'rum=0&expire=1656725148039',
  }

headers = {
    'authority': 'app.rdstation.com.br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"36d306794f7299d08723e098affc3045"',
    'referer': 'https://app.rdstation.com.br/nova-segmentacao',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
  }

params = {
    'segmentation_list': '6496060',
  }

response = requests.get('https://app.rdstation.com.br/leads', params=params, cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

infos_selector = soup.find_all('div', class_='col-xs-5')
for info_selector in infos_selector:
    right_div = info_selector.find('span', class_='btn-height-sm')
    if right_div:
      email_info = right_div.get_text()
      email_number = email_info.split('.')[0]
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
youtube_milL = youtube_countL
youtube_decL = youtube_countL
youtube_countL = youtube_decL + ""

# Get Twitter followers
driver.get('https://twitter.com/snapdragon_BRA')
twitter_count = driver.find_element(By.CSS_SELECTOR,'a[href="/snapdragon_BRA/followers"] > span > span').text

# Get Instagram followers BR e LATAM at the same time to avoid Instagram block

L = instaloader.Instaloader()
user = "nasinternaspod"
password = "SpinW_2021"
L.login(user, password)
profile = instaloader.Profile.from_username(L.context, "snapdragon_brasil")
profile2 = instaloader.Profile.from_username(L.context, "snapdragon_latam")

instaBR_mil = str(profile.followers)[:2]
instaBR_dec = str(profile.followers)[2]
instagram_count = instaBR_mil + "." + instaBR_dec + "K"

instaLT_mil = str(profile2.followers)[:1]
instaLT_dec = str(profile2.followers)[1]
instagram_countL = instaLT_mil + "." + instaLT_dec + "K"


#LATAM 

# Get Twitter followers LATAM
driver.get('https://twitter.com/snapdragon_LAT')
twitter_countL = driver.find_element(By.CSS_SELECTOR,'a[href="/snapdragon_LAT/followers"] > span > span').text


# Close webdriver
driver.close()

emailNumber = float(email_count.split('K')[0])
youtubeBrNumber = float(youtube_count.split('K')[0])
youtubeLNumber = float(youtube_countL)

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
