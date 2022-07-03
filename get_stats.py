from time import sleep
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
    '_gid': 'GA1.3.2102463956.1656721339',
    'split': '%7B%22xp_ab_test%22%3A%22variant%22%2C%22caterpie_activation_strategies%22%3A%22control%22%7D',
    'NPS_efd9b1a6_last_seen': '1656721351288',
    'ajs_user_id': '682938',
    'ajs_anonymous_id': 'e9b242cf-df33-48d7-88e9-69443910ebf3',
    'ajs_group_id': '434927',
    'intercom-id-hq3qq4eb': '0cb31ad4-f8c7-48c3-bb60-f33578d1e461',
    'intercom-session-hq3qq4eb': '',
    'drift_aid': 'c4c145b9-e410-4aee-9da7-e34f9e8ae0e0',
    'driftt_aid': 'c4c145b9-e410-4aee-9da7-e34f9e8ae0e0',
    '_hjSessionUser_863034': 'eyJpZCI6ImExOTM4MTg4LWVkOWEtNTgyYy04NzAxLTVmMjM4OTM4MGQ4ZCIsImNyZWF0ZWQiOjE2NTY3MjEzNDkwNTcsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjDonePolls': '761636',
    '_hjSessionUser_2716062': 'eyJpZCI6IjQyNTYzNTNmLTM2ODUtNWI2My04NTZlLTZmY2FlOTJhNzZjNSIsImNyZWF0ZWQiOjE2NTY3MjEzMzc4MjgsImV4aXN0aW5nIjp0cnVlfQ==',
    'cto_bundle': 'mY-RGl9teVhaek5yNU5XMFp5dHQySEY5aTJuejY2MkVwc1pmdEtLME9GYmlyJTJCJTJGbjA2amhVcG5vZ3dGWTUxWkppdFhEa1dFMEM3WEwzNVREN2UzZnROZHpsYlpxbUxVaSUyRkJmU3Z1b1VneWtaY2lmeUFiRkdDRHZGeGFLM25tOVlVQnZlcXlBUmp6VlphJTJCVHpFRnhEaWE0OGZicnhlN1FRbkdCeUVHbUVmUDJFYnl6MCUzRA',
    '_ga': 'GA1.3.1848593568.1656721339',
    '_gac_UA-17276574-1': '1.1656874415.%2528not%2520set%2529',
    '_hjSession_2716062': 'eyJpZCI6ImFkYjYzMDM2LWYxYjMtNGU4ZS1hNTQ2LWU4MDVmNDI5NTViMyIsImNyZWF0ZWQiOjE2NTY4NzQ0MTUzNDAsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_ga_GYGJG4ZD5K': 'GS1.1.1656874415.3.1.1656874436.0',
    'drift_campaign_refresh': '16bd79a3-2fb9-4e09-b0b9-46486bd28f54',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_863034': 'eyJpZCI6Ijc5MmRjOTRhLTZjMmEtNGNmZC1iMjI0LWQyMWVkNDQ1NGQ4YiIsImNyZWF0ZWQiOjE2NTY4NzQ0Mzg3NTksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjIncludedInPageviewSample': '1',
    '_hjCachedUserAttributes': 'eyJhdHRyaWJ1dGVzIjp7IkNvdW50cnlfSVBzdGFjayI6IkJSIiwiYWNjb3VudF9pZCI6IjQzNDkyNyIsImNvdW50cnlfY29kZSI6IkJSIiwiZW1haWwiOiJwZWRyb0BzcGlub2ZmLmRpZ2l0YWwiLCJsYW5ndWFnZSI6InB0LUJSIiwicGxhbiI6IlBybyIsInJvbGUiOiJBRE1JTiJ9LCJ1c2VySWQiOiI2ODI5MzgifQ==',
    'drift_eid': '682938',
    '__rdsid': '3669fb099db2e20f6547694d8a0f9c3d',
    'ak_bmsc': 'B2850360D4DA9992897D11F670CCBF20~000000000000000000000000000000~YAAQUtPPF3sCo6eBAQAAsAJqxRCJcX0Qi+eNJoMwD05/Vun0BBUUC8JH0rNbOHN4X8sTE3K7Y7nMSMfP4Xyedx7PmUDxpMgoocdoc4605H1FV0+OfVN5IJYFiXdj/Tj6cDIkEPp9DvMBm3CbH0f+qU7nsg/MJYJewoFpGqzeKbw2si1pzMR35C+tAG9+91C8mCVLwiGUZAmgCd8scKZ0XDhpKoEZMViBtlZkc7IEskj1Pvzz/pY/7K9PFeTNsys9kt+Uby2iJ0t/+7HxBwIr6584Q4u41fdIjvT5pr4biqkNFigOIdfYR0nfeJM6SiMffjPYuoZ/Yvy3lKWNtSJ5pfnS3+hEpmsM3nL+CIscMDfz/tjIsGxmV4qafsj/Cr1E73tQm0DHG3XAIC52qMAMvdXowtUBe9kanRuS6u1fZw==',
    'bm_sv': '4B9464FE0D385BAC2F98AABF43BB8BF1~YAAQUtPPF7cFo6eBAQAAnxRqxRDmS/kOZNtgjxdBqqqNfiEKi1WGgsQ1ld1P6Fng5B3IUQcgEBM8zDyNAJUbVrMaKsm0xCytRY/gh7BksXBknPxmobn4Y2iI0pZpBQn4GfX68uMVtQmYddIbAsvrDoJDrRsxNygfD6pkSV01RhRu5LkDu8yckt5mNF3qW0CZWjsYqkHFl34qQBh2fBd5Pvx2UUjICqBc110xg+nrRa0vkOf8iTgl8HmAGSvny7wFLydtkuVXjg==~1',
    '_uetsid': '10b954c0f99d11ec923ce1ad64c2ab4d',
    '_uetvid': '10ba2a40f99d11ec8f3d8b11afd138b5',
    '_dd_s': 'rum=0&expire=1656875550605',
}

headers = {
    'authority': 'app.rdstation.com.br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gid=GA1.3.2102463956.1656721339; split=%7B%22xp_ab_test%22%3A%22variant%22%2C%22caterpie_activation_strategies%22%3A%22control%22%7D; NPS_efd9b1a6_last_seen=1656721351288; ajs_user_id=682938; ajs_anonymous_id=e9b242cf-df33-48d7-88e9-69443910ebf3; ajs_group_id=434927; intercom-id-hq3qq4eb=0cb31ad4-f8c7-48c3-bb60-f33578d1e461; intercom-session-hq3qq4eb=; drift_aid=c4c145b9-e410-4aee-9da7-e34f9e8ae0e0; driftt_aid=c4c145b9-e410-4aee-9da7-e34f9e8ae0e0; _hjSessionUser_863034=eyJpZCI6ImExOTM4MTg4LWVkOWEtNTgyYy04NzAxLTVmMjM4OTM4MGQ4ZCIsImNyZWF0ZWQiOjE2NTY3MjEzNDkwNTcsImV4aXN0aW5nIjp0cnVlfQ==; _hjDonePolls=761636; _hjSessionUser_2716062=eyJpZCI6IjQyNTYzNTNmLTM2ODUtNWI2My04NTZlLTZmY2FlOTJhNzZjNSIsImNyZWF0ZWQiOjE2NTY3MjEzMzc4MjgsImV4aXN0aW5nIjp0cnVlfQ==; cto_bundle=mY-RGl9teVhaek5yNU5XMFp5dHQySEY5aTJuejY2MkVwc1pmdEtLME9GYmlyJTJCJTJGbjA2amhVcG5vZ3dGWTUxWkppdFhEa1dFMEM3WEwzNVREN2UzZnROZHpsYlpxbUxVaSUyRkJmU3Z1b1VneWtaY2lmeUFiRkdDRHZGeGFLM25tOVlVQnZlcXlBUmp6VlphJTJCVHpFRnhEaWE0OGZicnhlN1FRbkdCeUVHbUVmUDJFYnl6MCUzRA; _ga=GA1.3.1848593568.1656721339; _gac_UA-17276574-1=1.1656874415.%2528not%2520set%2529; _hjSession_2716062=eyJpZCI6ImFkYjYzMDM2LWYxYjMtNGU4ZS1hNTQ2LWU4MDVmNDI5NTViMyIsImNyZWF0ZWQiOjE2NTY4NzQ0MTUzNDAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga_GYGJG4ZD5K=GS1.1.1656874415.3.1.1656874436.0; drift_campaign_refresh=16bd79a3-2fb9-4e09-b0b9-46486bd28f54; _hjIncludedInSessionSample=0; _hjSession_863034=eyJpZCI6Ijc5MmRjOTRhLTZjMmEtNGNmZC1iMjI0LWQyMWVkNDQ1NGQ4YiIsImNyZWF0ZWQiOjE2NTY4NzQ0Mzg3NTksImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7IkNvdW50cnlfSVBzdGFjayI6IkJSIiwiYWNjb3VudF9pZCI6IjQzNDkyNyIsImNvdW50cnlfY29kZSI6IkJSIiwiZW1haWwiOiJwZWRyb0BzcGlub2ZmLmRpZ2l0YWwiLCJsYW5ndWFnZSI6InB0LUJSIiwicGxhbiI6IlBybyIsInJvbGUiOiJBRE1JTiJ9LCJ1c2VySWQiOiI2ODI5MzgifQ==; drift_eid=682938; __rdsid=3669fb099db2e20f6547694d8a0f9c3d; ak_bmsc=B2850360D4DA9992897D11F670CCBF20~000000000000000000000000000000~YAAQUtPPF3sCo6eBAQAAsAJqxRCJcX0Qi+eNJoMwD05/Vun0BBUUC8JH0rNbOHN4X8sTE3K7Y7nMSMfP4Xyedx7PmUDxpMgoocdoc4605H1FV0+OfVN5IJYFiXdj/Tj6cDIkEPp9DvMBm3CbH0f+qU7nsg/MJYJewoFpGqzeKbw2si1pzMR35C+tAG9+91C8mCVLwiGUZAmgCd8scKZ0XDhpKoEZMViBtlZkc7IEskj1Pvzz/pY/7K9PFeTNsys9kt+Uby2iJ0t/+7HxBwIr6584Q4u41fdIjvT5pr4biqkNFigOIdfYR0nfeJM6SiMffjPYuoZ/Yvy3lKWNtSJ5pfnS3+hEpmsM3nL+CIscMDfz/tjIsGxmV4qafsj/Cr1E73tQm0DHG3XAIC52qMAMvdXowtUBe9kanRuS6u1fZw==; bm_sv=4B9464FE0D385BAC2F98AABF43BB8BF1~YAAQUtPPF7cFo6eBAQAAnxRqxRDmS/kOZNtgjxdBqqqNfiEKi1WGgsQ1ld1P6Fng5B3IUQcgEBM8zDyNAJUbVrMaKsm0xCytRY/gh7BksXBknPxmobn4Y2iI0pZpBQn4GfX68uMVtQmYddIbAsvrDoJDrRsxNygfD6pkSV01RhRu5LkDu8yckt5mNF3qW0CZWjsYqkHFl34qQBh2fBd5Pvx2UUjICqBc110xg+nrRa0vkOf8iTgl8HmAGSvny7wFLydtkuVXjg==~1; _uetsid=10b954c0f99d11ec923ce1ad64c2ab4d; _uetvid=10ba2a40f99d11ec8f3d8b11afd138b5; _dd_s=rum=0&expire=1656875550605',
    'if-none-match': 'W/"00ab3d3e36f82748eb5cf63fb0e3dba4"',
    'referer': 'https://accounts.rdstation.com.br/?affiliate_id=%28not%20set%29&email_signup_account=false&exist_account=false&gclid=%28not%20set%29&lmdsid=%28not%20set%29&locale=pt-BR&redirect_to=https%3A%2F%2Fapp.rdstation.com.br%2Fauth%2Fcallback&referrer=%28not%20set%29&show_signup_account=false&signup_final_step=false&trial_origin=%28not%20set%29&utm_campaign=%28not%20set%29&utm_medium=%28not%20set%29&utm_source=%28not%20set%29&utm_term=%28not%20set%29&xtra=%28not%20set%29',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
}

params = {
    'segmentation_list': '6496060',
}

response = requests.get('https://app.rdstation.com.br/leads', params=params, cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

email_number = ""

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
youtube_milL = youtube_countL
youtube_decL = youtube_countL
youtube_countL = youtube_decL + ""

# Get Twitter followers
driver.get('https://twitter.com/snapdragon_BRA')
twitter_count = driver.find_element(By.CSS_SELECTOR,'a[href="/snapdragon_BRA/followers"] > span > span').text

# Get Instagram followers BR e LATAM at the same time to avoid Instagram block

L = instaloader.Instaloader()
user = "noise@neto.house"
password = "noise(2020)"
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
sleep(5)
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
