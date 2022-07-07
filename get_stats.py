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
    'split': '%7B%22xp_ab_test%22%3A%22variant%22%2C%22caterpie_activation_strategies%22%3A%22control%22%7D',
    'ajs_group_id': '434927',
    'ajs_user_id': '697398',
    'ajs_anonymous_id': '2e1316f6-da5f-4f8b-bbd3-cdf64038e530',
    'cto_bundle': 'GoVtFV9MS05nTzFUYVB4NmI5NFRWaU56Vk5oVXM5WDk1SlAlMkJGNWZwJTJCT2VCN2liSW85MlVMTGg3Ym5LdzRzNFVpOFFGcHJHQXlNRSUyRnNad3hZNFJmcDhMQTZpTDgxZ1NZOFZWejRrTlZLTkpPTG5BcVJSWDh0dmZyS29yaUc2Sk5DaFFNRXJHZ3ZFYlJieEZmUkwxR09abjN2VVJxTTVsZWp0ZnByMXozaE5mWG92NzAlM0Q',
    '__rdsid': 'b71963fb2d396e768b93304090f445a6',
    '_ga': 'GA1.3.1486625735.1657081595',
    '_gac_UA-17276574-1': '1.1657219555.%2528not%2520set%2529',
    '_ga_GYGJG4ZD5K': 'GS1.1.1657219555.4.1.1657219589.0',
    '_hjCachedUserAttributes': 'eyJhdHRyaWJ1dGVzIjp7IkNvdW50cnlfSVBzdGFjayI6IkJSIiwiYWNjb3VudF9pZCI6IjQzNDkyNyIsImNvdW50cnlfY29kZSI6IkJSIiwiZW1haWwiOiJuZXRvQHNwaW5vZmYuZGlnaXRhbCIsImxhbmd1YWdlIjoicHQtQlIiLCJwbGFuIjoiUHJvIiwicm9sZSI6IkFETUlOIn0sInVzZXJJZCI6IjY5NzM5OCJ9',
    'drift_eid': '697398',
    'ak_bmsc': '10F6F829779C60943AF90FF238F6D4C0~000000000000000000000000000000~YAAQVv4pFzR+p7CBAQAAYqSP2hAw0O9X5Fq2x2AxBGV9Sq2tb8DpC1q4Cv4XflqEDg+9Pi2hBvucrkqydn0UoIng0XvvmLjnQDmGPOptUvwecCPGRg5WuM0u2LC2u1MCfQrY+CVNGsW0JzWn7sNQk5beysPmnCISRQOFq+YhZRUgUQTlV14Y0STTKP9g0Rh4Lt4nLq/rvAD/gmlNUymo0W5ztlWI1yOurtcXC9zpAtf+/gutauT37lPc1epjwaoEvhLIhZJ7SeZkyaGfJKUjUeETCsFXggDc9XyXdL6kPugYWoA2lz6/437C1RnLxKbIHbZBYu67Wpk/gRN4X5omhtK0scEjd8mkrNdUORwd0MEmc8sfhVIvZEoqhwTbF6YpiSIIGP9ro5vjhL7Ss9WLLg==',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_863034': 'eyJpZCI6IjQzMzE5NWI1LTY0NjQtNDYzNy04YTdjLTcyY2M4MTI3MzkxYSIsImNyZWF0ZWQiOjE2NTcyMjkyNTYzODYsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'drift_campaign_refresh': '9594e6fe-d040-49d6-a0af-7f5765519f52',
    '_uetsid': 'e5ef2030fce311ecb53bedaab331166c',
    '_uetvid': 'e5ef5cc0fce311ecac2e85d56bbe46fb',
    'bm_sv': '7DB9E7168660C1D8B810C1223C65E3F4~YAAQVv4pF56Gp7CBAQAAzjWQ2hA/E1euzbOqKJjBWFHrRQvdh5n9Vbr39LLQFMSEH5/NLTMa38GK0ZL4d9RXqMN8H7Bhe5DF1R2jVoWITruBxjNjIfMbD53LgEm+PpAPCiu/BvA56AwFeUWZg1oygolF5H5X9tRXU8VI41KN0kEbrQYzQl3xidjgLFD/JZ/OzZ4P5SFio8tvvuJxJIzWbuIqScXg4Qh51QgmBq55Fr8d+CYFXhF0uZMWGAESj6EHcI6cdVnP~1',
    'intercom-session-hq3qq4eb': 'c0xPL3RRaHhCSm5UNEVLUmZrR1ZPK25kOWN1TlFUMlRzVGl1OWNZNmo3TjY3RjdDU3MwQVh1QzJOSUtRZjZ1NS0tQ05LZ2ErS1pFUER6Wk5pWmRDZHdRUT09--234b8aa01618d72caf88a002e673bc1b534766ca',
    '_dd_s': 'rum=0&expire=1657230253855',
}

headers = {
    'authority': 'app.rdstation.com.br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gid=GA1.3.841158784.1657081595; NPS_efd9b1a6_last_seen=1657081628591; intercom-id-hq3qq4eb=e5043f4d-96ed-4f4e-b632-499a74d25eb2; drift_aid=a0fe3ffd-3efa-4b45-8109-155e76b47eb0; driftt_aid=a0fe3ffd-3efa-4b45-8109-155e76b47eb0; _hjSessionUser_863034=eyJpZCI6ImE3NDdhZTkwLTc4MjgtNTUyZS04NGFjLWM4YTM2OTIyM2M3OSIsImNyZWF0ZWQiOjE2NTcwODE2Mjc3MjYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_2716062=eyJpZCI6IjY4MzkzNTZkLWYwYzItNWZlZi04NjA5LTE0ZDYyYjlmYzA4NSIsImNyZWF0ZWQiOjE2NTcwODE1OTU3NzAsImV4aXN0aW5nIjp0cnVlfQ==; split=%7B%22xp_ab_test%22%3A%22variant%22%2C%22caterpie_activation_strategies%22%3A%22control%22%7D; ajs_group_id=434927; ajs_user_id=697398; ajs_anonymous_id=2e1316f6-da5f-4f8b-bbd3-cdf64038e530; cto_bundle=GoVtFV9MS05nTzFUYVB4NmI5NFRWaU56Vk5oVXM5WDk1SlAlMkJGNWZwJTJCT2VCN2liSW85MlVMTGg3Ym5LdzRzNFVpOFFGcHJHQXlNRSUyRnNad3hZNFJmcDhMQTZpTDgxZ1NZOFZWejRrTlZLTkpPTG5BcVJSWDh0dmZyS29yaUc2Sk5DaFFNRXJHZ3ZFYlJieEZmUkwxR09abjN2VVJxTTVsZWp0ZnByMXozaE5mWG92NzAlM0Q; __rdsid=b71963fb2d396e768b93304090f445a6; _ga=GA1.3.1486625735.1657081595; _gac_UA-17276574-1=1.1657219555.%2528not%2520set%2529; _ga_GYGJG4ZD5K=GS1.1.1657219555.4.1.1657219589.0; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7IkNvdW50cnlfSVBzdGFjayI6IkJSIiwiYWNjb3VudF9pZCI6IjQzNDkyNyIsImNvdW50cnlfY29kZSI6IkJSIiwiZW1haWwiOiJuZXRvQHNwaW5vZmYuZGlnaXRhbCIsImxhbmd1YWdlIjoicHQtQlIiLCJwbGFuIjoiUHJvIiwicm9sZSI6IkFETUlOIn0sInVzZXJJZCI6IjY5NzM5OCJ9; drift_eid=697398; ak_bmsc=10F6F829779C60943AF90FF238F6D4C0~000000000000000000000000000000~YAAQVv4pFzR+p7CBAQAAYqSP2hAw0O9X5Fq2x2AxBGV9Sq2tb8DpC1q4Cv4XflqEDg+9Pi2hBvucrkqydn0UoIng0XvvmLjnQDmGPOptUvwecCPGRg5WuM0u2LC2u1MCfQrY+CVNGsW0JzWn7sNQk5beysPmnCISRQOFq+YhZRUgUQTlV14Y0STTKP9g0Rh4Lt4nLq/rvAD/gmlNUymo0W5ztlWI1yOurtcXC9zpAtf+/gutauT37lPc1epjwaoEvhLIhZJ7SeZkyaGfJKUjUeETCsFXggDc9XyXdL6kPugYWoA2lz6/437C1RnLxKbIHbZBYu67Wpk/gRN4X5omhtK0scEjd8mkrNdUORwd0MEmc8sfhVIvZEoqhwTbF6YpiSIIGP9ro5vjhL7Ss9WLLg==; _hjIncludedInSessionSample=0; _hjSession_863034=eyJpZCI6IjQzMzE5NWI1LTY0NjQtNDYzNy04YTdjLTcyY2M4MTI3MzkxYSIsImNyZWF0ZWQiOjE2NTcyMjkyNTYzODYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; drift_campaign_refresh=9594e6fe-d040-49d6-a0af-7f5765519f52; _uetsid=e5ef2030fce311ecb53bedaab331166c; _uetvid=e5ef5cc0fce311ecac2e85d56bbe46fb; bm_sv=7DB9E7168660C1D8B810C1223C65E3F4~YAAQVv4pF56Gp7CBAQAAzjWQ2hA/E1euzbOqKJjBWFHrRQvdh5n9Vbr39LLQFMSEH5/NLTMa38GK0ZL4d9RXqMN8H7Bhe5DF1R2jVoWITruBxjNjIfMbD53LgEm+PpAPCiu/BvA56AwFeUWZg1oygolF5H5X9tRXU8VI41KN0kEbrQYzQl3xidjgLFD/JZ/OzZ4P5SFio8tvvuJxJIzWbuIqScXg4Qh51QgmBq55Fr8d+CYFXhF0uZMWGAESj6EHcI6cdVnP~1; intercom-session-hq3qq4eb=c0xPL3RRaHhCSm5UNEVLUmZrR1ZPK25kOWN1TlFUMlRzVGl1OWNZNmo3TjY3RjdDU3MwQVh1QzJOSUtRZjZ1NS0tQ05LZ2ErS1pFUER6Wk5pWmRDZHdRUT09--234b8aa01618d72caf88a002e673bc1b534766ca; _dd_s=rum=0&expire=1657230253855',
    'if-none-match': 'W/"1acfa22216cf0f73e1006944d94849c3"',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
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
