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
s = Service('/Users/neto/ARDUINO/CounterSnapAll/geckodriver')
driver = webdriver.Firefox(service=s, options=options)
driver.implicitly_wait(10)

#BRASIL

#EMail
cookies = {
    '_gid': 'GA1.3.841158784.1657081595',
    'NPS_efd9b1a6_last_seen': '1657081628591',
    'intercom-id-hq3qq4eb': 'e5043f4d-96ed-4f4e-b632-499a74d25eb2',
    'drift_aid': 'a0fe3ffd-3efa-4b45-8109-155e76b47eb0',
    'driftt_aid': 'a0fe3ffd-3efa-4b45-8109-155e76b47eb0',
    '_hjSessionUser_863034': 'eyJpZCI6ImE3NDdhZTkwLTc4MjgtNTUyZS04NGFjLWM4YTM2OTIyM2M3OSIsImNyZWF0ZWQiOjE2NTcwODE2Mjc3MjYsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSessionUser_2716062': 'eyJpZCI6IjY4MzkzNTZkLWYwYzItNWZlZi04NjA5LTE0ZDYyYjlmYzA4NSIsImNyZWF0ZWQiOjE2NTcwODE1OTU3NzAsImV4aXN0aW5nIjp0cnVlfQ==',
    'NPS_efd9b1a6_throttle': '1657169408358',
    'split': '%7B%22xp_ab_test%22%3A%22variant%22%2C%22caterpie_activation_strategies%22%3A%22control%22%7D',
    'ajs_group_id': '434927',
    'ak_bmsc': '0BF3ACAD0076809F86172A695EAAC455~000000000000000000000000000000~YAAQ1boXAlxjBquBAQAAS0nM1hCEi0sqdVy53x1CdNIZ18nMT/OXvBWXz75DnXJ2xMO+AHg4wTsMtipeO/eEsuLYvDnDRrSDXJz/8ZfmzqsoNSrv/PGnlXQbg/6YWmMw2bALeXgcuCuqwCqV9oz5wc6Eb05b46JcqyayszE6QfcEhruan4kKOAXFgU4JzIrlpBGYCGXizV3jjcG6uVi88E5d0+m4Wxpyf3RNh39qgT8UTSNS8aHipAMMYnVV05TtFszDVUJmnC6UJbJrQABsVZieYSJw94nxleRTjQM355DrCxRtIrnr99azQ3ABfmJv/HegDcwHvKmoe2/R0cWCBDxY7QDXqImKPi0T8SdGayee7sK2g5xXtfSzqJuU+nA7VjpqT4qyVG0VZW4aox+bMw==',
    '_hjSession_2716062': 'eyJpZCI6ImRlZjlkYWJjLWI0YjktNDAzMi04NjA4LTI3MzVjNzI2ZWU5NyIsImNyZWF0ZWQiOjE2NTcxNjYxMjE4NDksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_gac_UA-17276574-1': '1.1657126111.%25252525252528not%25252525252520set%25252525252529',
    '_gat_UA-17276574-1': '1',
    '_ga': 'GA1.1.1486625735.1657081595',
    '__rdsid': 'ef0ef4c4e015e6e4bcc92900efcc7e71',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_863034': 'eyJpZCI6IjgwMjIxOTdlLTE3NWUtNGM0NS04MTNhLThiNjFiNGFkNTVmZiIsImNyZWF0ZWQiOjE2NTcxNjYzMTc0NTYsImluU2FtcGxlIjpmYWxzZX0=',
    'ajs_user_id': '697398',
    'ajs_anonymous_id': '2e1316f6-da5f-4f8b-bbd3-cdf64038e530',
    '_hjCachedUserAttributes': 'eyJhdHRyaWJ1dGVzIjp7IkNvdW50cnlfSVBzdGFjayI6IkJSIiwiYWNjb3VudF9pZCI6IjQzNDkyNyIsImNvdW50cnlfY29kZSI6IkJSIiwiZW1haWwiOiJuZXRvQHNwaW5vZmYuZGlnaXRhbCIsImxhbmd1YWdlIjoicHQtQlIiLCJwbGFuIjoiUHJvIiwicm9sZSI6IkFETUlOIn0sInVzZXJJZCI6IjY5NzM5OCJ9',
    'drift_campaign_refresh': '3f6ecd9b-12f9-4c73-b3ea-01d0e5f4be1d',
    'cto_bundle': 'GoVtFV9MS05nTzFUYVB4NmI5NFRWaU56Vk5oVXM5WDk1SlAlMkJGNWZwJTJCT2VCN2liSW85MlVMTGg3Ym5LdzRzNFVpOFFGcHJHQXlNRSUyRnNad3hZNFJmcDhMQTZpTDgxZ1NZOFZWejRrTlZLTkpPTG5BcVJSWDh0dmZyS29yaUc2Sk5DaFFNRXJHZ3ZFYlJieEZmUkwxR09abjN2VVJxTTVsZWp0ZnByMXozaE5mWG92NzAlM0Q',
    'drift_eid': '697398',
    '_uetsid': 'e5ef2030fce311ecb53bedaab331166c',
    '_uetvid': 'e5ef5cc0fce311ecac2e85d56bbe46fb',
    'bm_sv': 'FA5E34C6951A177F40713EF66FDA4FEA~YAAQFaLSvZ7y7sKBAQAASm7P1hDvXoD/44SSjhB60ID8LFOClb2xT5DibKvLmygYsu7XVnZqkgmH5wGbCJzwKOMe0dNAf4w2XFeP2mJTe3TSe/wzLHocZSRpRqV4rG5S/n1G1ehu42Yawn4U9IYm7wgcNKIT+Dh+Furh67nX/ZToSswzRGU3WyqKT07+u7MTWSE8RCb7v8yFPwR7bI9IjHuLZ1QaQ042nGDycAe3366fjvtUbzALwJhJRJPyE8Fz8aifhXv9JA==~1',
    'intercom-session-hq3qq4eb': 'NTdNbmNxTVlPQi81czYyazlBRjhpaWlkWnVMeFdjdVJoQjVnNG0xaFU2Q1M3WllMT3FwYmthQVI5VmVUMHdmUC0tUVJMaXZoUit4T2hWcFZwSXNaTTgzQT09--c09eaf7a7ea2f4b18640f757c66faa140e52ceff',
    '_ga_GYGJG4ZD5K': 'GS1.1.1657166122.3.1.1657166329.0',
    '_dd_s': 'rum=0&expire=1657167226448',
}

headers = {
    'authority': 'app.rdstation.com.br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gid=GA1.3.841158784.1657081595; NPS_efd9b1a6_last_seen=1657081628591; intercom-id-hq3qq4eb=e5043f4d-96ed-4f4e-b632-499a74d25eb2; drift_aid=a0fe3ffd-3efa-4b45-8109-155e76b47eb0; driftt_aid=a0fe3ffd-3efa-4b45-8109-155e76b47eb0; _hjSessionUser_863034=eyJpZCI6ImE3NDdhZTkwLTc4MjgtNTUyZS04NGFjLWM4YTM2OTIyM2M3OSIsImNyZWF0ZWQiOjE2NTcwODE2Mjc3MjYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_2716062=eyJpZCI6IjY4MzkzNTZkLWYwYzItNWZlZi04NjA5LTE0ZDYyYjlmYzA4NSIsImNyZWF0ZWQiOjE2NTcwODE1OTU3NzAsImV4aXN0aW5nIjp0cnVlfQ==; NPS_efd9b1a6_throttle=1657169408358; split=%7B%22xp_ab_test%22%3A%22variant%22%2C%22caterpie_activation_strategies%22%3A%22control%22%7D; ajs_group_id=434927; ak_bmsc=0BF3ACAD0076809F86172A695EAAC455~000000000000000000000000000000~YAAQ1boXAlxjBquBAQAAS0nM1hCEi0sqdVy53x1CdNIZ18nMT/OXvBWXz75DnXJ2xMO+AHg4wTsMtipeO/eEsuLYvDnDRrSDXJz/8ZfmzqsoNSrv/PGnlXQbg/6YWmMw2bALeXgcuCuqwCqV9oz5wc6Eb05b46JcqyayszE6QfcEhruan4kKOAXFgU4JzIrlpBGYCGXizV3jjcG6uVi88E5d0+m4Wxpyf3RNh39qgT8UTSNS8aHipAMMYnVV05TtFszDVUJmnC6UJbJrQABsVZieYSJw94nxleRTjQM355DrCxRtIrnr99azQ3ABfmJv/HegDcwHvKmoe2/R0cWCBDxY7QDXqImKPi0T8SdGayee7sK2g5xXtfSzqJuU+nA7VjpqT4qyVG0VZW4aox+bMw==; _hjSession_2716062=eyJpZCI6ImRlZjlkYWJjLWI0YjktNDAzMi04NjA4LTI3MzVjNzI2ZWU5NyIsImNyZWF0ZWQiOjE2NTcxNjYxMjE4NDksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gac_UA-17276574-1=1.1657126111.%25252525252528not%25252525252520set%25252525252529; _gat_UA-17276574-1=1; _ga=GA1.1.1486625735.1657081595; __rdsid=ef0ef4c4e015e6e4bcc92900efcc7e71; _hjIncludedInSessionSample=0; _hjSession_863034=eyJpZCI6IjgwMjIxOTdlLTE3NWUtNGM0NS04MTNhLThiNjFiNGFkNTVmZiIsImNyZWF0ZWQiOjE2NTcxNjYzMTc0NTYsImluU2FtcGxlIjpmYWxzZX0=; ajs_user_id=697398; ajs_anonymous_id=2e1316f6-da5f-4f8b-bbd3-cdf64038e530; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7IkNvdW50cnlfSVBzdGFjayI6IkJSIiwiYWNjb3VudF9pZCI6IjQzNDkyNyIsImNvdW50cnlfY29kZSI6IkJSIiwiZW1haWwiOiJuZXRvQHNwaW5vZmYuZGlnaXRhbCIsImxhbmd1YWdlIjoicHQtQlIiLCJwbGFuIjoiUHJvIiwicm9sZSI6IkFETUlOIn0sInVzZXJJZCI6IjY5NzM5OCJ9; drift_campaign_refresh=3f6ecd9b-12f9-4c73-b3ea-01d0e5f4be1d; cto_bundle=GoVtFV9MS05nTzFUYVB4NmI5NFRWaU56Vk5oVXM5WDk1SlAlMkJGNWZwJTJCT2VCN2liSW85MlVMTGg3Ym5LdzRzNFVpOFFGcHJHQXlNRSUyRnNad3hZNFJmcDhMQTZpTDgxZ1NZOFZWejRrTlZLTkpPTG5BcVJSWDh0dmZyS29yaUc2Sk5DaFFNRXJHZ3ZFYlJieEZmUkwxR09abjN2VVJxTTVsZWp0ZnByMXozaE5mWG92NzAlM0Q; drift_eid=697398; _uetsid=e5ef2030fce311ecb53bedaab331166c; _uetvid=e5ef5cc0fce311ecac2e85d56bbe46fb; bm_sv=FA5E34C6951A177F40713EF66FDA4FEA~YAAQFaLSvZ7y7sKBAQAASm7P1hDvXoD/44SSjhB60ID8LFOClb2xT5DibKvLmygYsu7XVnZqkgmH5wGbCJzwKOMe0dNAf4w2XFeP2mJTe3TSe/wzLHocZSRpRqV4rG5S/n1G1ehu42Yawn4U9IYm7wgcNKIT+Dh+Furh67nX/ZToSswzRGU3WyqKT07+u7MTWSE8RCb7v8yFPwR7bI9IjHuLZ1QaQ042nGDycAe3366fjvtUbzALwJhJRJPyE8Fz8aifhXv9JA==~1; intercom-session-hq3qq4eb=NTdNbmNxTVlPQi81czYyazlBRjhpaWlkWnVMeFdjdVJoQjVnNG0xaFU2Q1M3WllMT3FwYmthQVI5VmVUMHdmUC0tUVJMaXZoUit4T2hWcFZwSXNaTTgzQT09--c09eaf7a7ea2f4b18640f757c66faa140e52ceff; _ga_GYGJG4ZD5K=GS1.1.1657166122.3.1.1657166329.0; _dd_s=rum=0&expire=1657167226448',
    'if-none-match': 'W/"3bc8f9bfdaa3c3b7832f57bd79312697"',
    'referer': 'https://app.rdstation.com.br/nova-segmentacao',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
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
#user = "neto_netohouse"
#password = "061231NetoHouse"
#L.login(user, password)
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
