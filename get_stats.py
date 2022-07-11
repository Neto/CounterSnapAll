from time import sleep
from tokenize import String
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from datetime import datetime
from playwright.sync_api import sync_playwright
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
#cookies = {
#    'NPS_efd9b1a6_last_seen': '1657081628591',
#    'intercom-id-hq3qq4eb': 'e5043f4d-96ed-4f4e-b632-499a74d25eb2',
#    'drift_aid': 'a0fe3ffd-3efa-4b45-8109-155e76b47eb0',
#    'driftt_aid': 'a0fe3ffd-3efa-4b45-8109-155e76b47eb0',
#    '_hjSessionUser_863034': 'eyJpZCI6ImE3NDdhZTkwLTc4MjgtNTUyZS04NGFjLWM4YTM2OTIyM2M3OSIsImNyZWF0ZWQiOjE2NTcwODE2Mjc3MjYsImV4aXN0aW5nIjp0cnVlfQ==',
#    '_hjSessionUser_2716062': 'eyJpZCI6IjY4MzkzNTZkLWYwYzItNWZlZi04NjA5LTE0ZDYyYjlmYzA4NSIsImNyZWF0ZWQiOjE2NTcwODE1OTU3NzAsImV4aXN0aW5nIjp0cnVlfQ==',
#    'split': '%7B%22xp_ab_test%22%3A%22variant%22%2C%22caterpie_activation_strategies%22%3A%22control%22%7D',
#    'ajs_group_id': '434927',
#    'ajs_user_id': '697398',
#    'ajs_anonymous_id': '2e1316f6-da5f-4f8b-bbd3-cdf64038e530',
#    'cto_bundle': 'F9oZN19MS05nTzFUYVB4NmI5NFRWaU56Vk5oRmZuNkVsRXdQbWpVaVQ0WEFkekdpS0FQMzNpaDcwbGdheDIyRSUyRkRmZlluVEwzOEg0QWtRa0c0TkVud3hkeWdHR09CZFhCenFRaWlqbDlnU2MyVUYlMkJEVHZKNEdBOFJDJTJCN0RaM1Y3RWpBcXFIRG16QXpleHVPdkk4cW9BTUQzVFVuRUtGWTlsMHRQNTM2aFlhcGYxcTFEejEyTDVOTzQ4Nm1kZ3NocklaWnV5ejBISVRTRSUyQnVaaWpaSTdMRmdDWXclM0QlM0Q',
#    'NPS_efd9b1a6_surveyed': 'true',
#    '_hjCachedUserAttributes': 'eyJhdHRyaWJ1dGVzIjp7IkNvdW50cnlfSVBzdGFjayI6IkJSIiwiYWNjb3VudF9pZCI6IjQzNDkyNyIsImNvdW50cnlfY29kZSI6IkJSIiwiZW1haWwiOiJuZXRvQHNwaW5vZmYuZGlnaXRhbCIsImxhbmd1YWdlIjoicHQtQlIiLCJwbGFuIjoiUHJvIiwicm9sZSI6IkFETUlOIn0sInVzZXJJZCI6IjY5NzM5OCJ9',
#    'drift_eid': '697398',
#    '_uetvid': 'e5ef5cc0fce311ecac2e85d56bbe46fb',
#    'intercom-session-hq3qq4eb': 'eXlITWZaWTh6bHZ6VnlUQVJ0MWlYSFVxcnJmaDFncW84UG4yYWhCWU9HM0t0Q3ZSaC9LZnNXdlp1aHhVRngyUi0tZUVsMXNHL05rYW05d1gxUVcxTityZz09--9ccbab8fffbe3b59cfe15d7c9f5c2c220b67a917',
#    '__rdsid': 'ccfa80beeec16ead174e9fdbbad5a8df',
#    'ak_bmsc': 'A8870C800FAC5A2CF39AEBFE8589E270~000000000000000000000000000000~YAAQT9PPF1QbWLSBAQAABM286RCOZfDhUhGGmxotyMQGWIw89j4tMflmZ3rNcr4F9ikEKeEar7JLAsMo0YhSC8AvW8lolv8lGsCoLWohfS5OWRwDK316WfCqu7rLH+hiMVbSco+6OSUY2fq1+QLJux5TCvUrddK4OOXVR+FVelgT33kGjNvhBeAJEJg4+QCBsuh6HvQeYNkVcLzSazDfrOhSVs/3Gm4KRK1yIuMSUzm9GOCIWA4alE4cnbxHx1gUjfpEQUCUtzqA1zOmJyTzLgd6/DDuRNUpGVdWYl3YdM/bE89AFBGRI0ftLhBIumPlgUfcnPw0Zk3XhL9cQkdbAhvxSHSUrgbE/jYY1BZpQOs5tSIfWD6U/hmZQVVCu7AMfPboGQ5LniyWqAry87yKTQ==',
#    '_dd_s': '',
#    '_hjSession_2716062': 'eyJpZCI6ImEzNDlmZDI4LTc5Y2YtNGM1My1iZmIyLWE0ZWMwYjZkZWNhNSIsImNyZWF0ZWQiOjE2NTc0ODM4NzQ1NTksImluU2FtcGxlIjpmYWxzZX0=',
#    '_hjAbsoluteSessionInProgress': '0',
#    '_ga_GYGJG4ZD5K': 'GS1.1.1657483874.9.0.1657483874.0',
#    '_ga': 'GA1.3.1486625735.1657081595',
#    '_gid': 'GA1.3.394741834.1657483875',
#    '_gac_UA-17276574-1': '1.1657483875.%2528not%2520set%2529',
#    '_gat_UA-17276574-1': '1',
#    'bm_sv': 'C043D409463DF3BE15D8314B2E3C3C6B~YAAQT9PPF+4nWLSBAQAAMFe96RDd3Py7GaOl7jnq4l++yXhCBvmWib049/SmiNSl/9jD06CwM77vpYALxhMBYlbQnNlHPvjW276uAxkYzEZ5o1TTKJy+DZ5nWgio4dHhYX/5+g7KipUmpB5PbtBCk10FULOZDJEopPHLz69Kc8Hq35LotJIUoHDZMs3cM2cmjLzyaL9v/1dmvZ2ZcpbYm5FgP7nITd+y8FvgdTrU5MqDyxIRVj3bLud2SfEYHuVPd/PMrGBu~1',
#}
#
#headers = {
#    'authority': 'app.rdstation.com.br',
#    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#    'accept-language': 'en-US,en;q=0.9',
#    # Requests sorts cookies= alphabetically
#    # 'cookie': 'NPS_efd9b1a6_last_seen=1657081628591; intercom-id-hq3qq4eb=e5043f4d-96ed-4f4e-b632-499a74d25eb2; drift_aid=a0fe3ffd-3efa-4b45-8109-155e76b47eb0; driftt_aid=a0fe3ffd-3efa-4b45-8109-155e76b47eb0; _hjSessionUser_863034=eyJpZCI6ImE3NDdhZTkwLTc4MjgtNTUyZS04NGFjLWM4YTM2OTIyM2M3OSIsImNyZWF0ZWQiOjE2NTcwODE2Mjc3MjYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_2716062=eyJpZCI6IjY4MzkzNTZkLWYwYzItNWZlZi04NjA5LTE0ZDYyYjlmYzA4NSIsImNyZWF0ZWQiOjE2NTcwODE1OTU3NzAsImV4aXN0aW5nIjp0cnVlfQ==; split=%7B%22xp_ab_test%22%3A%22variant%22%2C%22caterpie_activation_strategies%22%3A%22control%22%7D; ajs_group_id=434927; ajs_user_id=697398; ajs_anonymous_id=2e1316f6-da5f-4f8b-bbd3-cdf64038e530; cto_bundle=F9oZN19MS05nTzFUYVB4NmI5NFRWaU56Vk5oRmZuNkVsRXdQbWpVaVQ0WEFkekdpS0FQMzNpaDcwbGdheDIyRSUyRkRmZlluVEwzOEg0QWtRa0c0TkVud3hkeWdHR09CZFhCenFRaWlqbDlnU2MyVUYlMkJEVHZKNEdBOFJDJTJCN0RaM1Y3RWpBcXFIRG16QXpleHVPdkk4cW9BTUQzVFVuRUtGWTlsMHRQNTM2aFlhcGYxcTFEejEyTDVOTzQ4Nm1kZ3NocklaWnV5ejBISVRTRSUyQnVaaWpaSTdMRmdDWXclM0QlM0Q; NPS_efd9b1a6_surveyed=true; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7IkNvdW50cnlfSVBzdGFjayI6IkJSIiwiYWNjb3VudF9pZCI6IjQzNDkyNyIsImNvdW50cnlfY29kZSI6IkJSIiwiZW1haWwiOiJuZXRvQHNwaW5vZmYuZGlnaXRhbCIsImxhbmd1YWdlIjoicHQtQlIiLCJwbGFuIjoiUHJvIiwicm9sZSI6IkFETUlOIn0sInVzZXJJZCI6IjY5NzM5OCJ9; drift_eid=697398; _uetvid=e5ef5cc0fce311ecac2e85d56bbe46fb; intercom-session-hq3qq4eb=eXlITWZaWTh6bHZ6VnlUQVJ0MWlYSFVxcnJmaDFncW84UG4yYWhCWU9HM0t0Q3ZSaC9LZnNXdlp1aHhVRngyUi0tZUVsMXNHL05rYW05d1gxUVcxTityZz09--9ccbab8fffbe3b59cfe15d7c9f5c2c220b67a917; __rdsid=ccfa80beeec16ead174e9fdbbad5a8df; ak_bmsc=A8870C800FAC5A2CF39AEBFE8589E270~000000000000000000000000000000~YAAQT9PPF1QbWLSBAQAABM286RCOZfDhUhGGmxotyMQGWIw89j4tMflmZ3rNcr4F9ikEKeEar7JLAsMo0YhSC8AvW8lolv8lGsCoLWohfS5OWRwDK316WfCqu7rLH+hiMVbSco+6OSUY2fq1+QLJux5TCvUrddK4OOXVR+FVelgT33kGjNvhBeAJEJg4+QCBsuh6HvQeYNkVcLzSazDfrOhSVs/3Gm4KRK1yIuMSUzm9GOCIWA4alE4cnbxHx1gUjfpEQUCUtzqA1zOmJyTzLgd6/DDuRNUpGVdWYl3YdM/bE89AFBGRI0ftLhBIumPlgUfcnPw0Zk3XhL9cQkdbAhvxSHSUrgbE/jYY1BZpQOs5tSIfWD6U/hmZQVVCu7AMfPboGQ5LniyWqAry87yKTQ==; _dd_s=; _hjSession_2716062=eyJpZCI6ImEzNDlmZDI4LTc5Y2YtNGM1My1iZmIyLWE0ZWMwYjZkZWNhNSIsImNyZWF0ZWQiOjE2NTc0ODM4NzQ1NTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga_GYGJG4ZD5K=GS1.1.1657483874.9.0.1657483874.0; _ga=GA1.3.1486625735.1657081595; _gid=GA1.3.394741834.1657483875; _gac_UA-17276574-1=1.1657483875.%2528not%2520set%2529; _gat_UA-17276574-1=1; bm_sv=C043D409463DF3BE15D8314B2E3C3C6B~YAAQT9PPF+4nWLSBAQAAMFe96RDd3Py7GaOl7jnq4l++yXhCBvmWib049/SmiNSl/9jD06CwM77vpYALxhMBYlbQnNlHPvjW276uAxkYzEZ5o1TTKJy+DZ5nWgio4dHhYX/5+g7KipUmpB5PbtBCk10FULOZDJEopPHLz69Kc8Hq35LotJIUoHDZMs3cM2cmjLzyaL9v/1dmvZ2ZcpbYm5FgP7nITd+y8FvgdTrU5MqDyxIRVj3bLud2SfEYHuVPd/PMrGBu~1',
#    'referer': 'https://accounts.rdstation.com.br/?affiliate_id=%28not%20set%29&email_signup_account=false&exist_account=false&gclid=%28not%20set%29&lmdsid=%28not%20set%29&locale=pt-BR&redirect_to=https%3A%2F%2Fapp.rdstation.com.br%2Fauth%2Fcallback&referrer=%28not%20set%29&show_signup_account=false&signup_final_step=false&trial_origin=%28not%20set%29&utm_campaign=%28not%20set%29&utm_medium=%28not%20set%29&utm_source=%28not%20set%29&utm_term=%28not%20set%29&xtra=%28not%20set%29',
#    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
#    'sec-ch-ua-mobile': '?0',
#    'sec-ch-ua-platform': '"macOS"',
#    'sec-fetch-dest': 'document',
#    'sec-fetch-mode': 'navigate',
#    'sec-fetch-site': 'same-site',
#    'sec-fetch-user': '?1',
#    'upgrade-insecure-requests': '1',
#    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
#}
#
#params = {
#    'segmentation_list': '6496060',
#}
#
#response = requests.get('https://app.rdstation.com.br/leads', params=params, cookies=cookies, headers=headers)
#
#
#soup = BeautifulSoup(response.content, 'html.parser')
#
#email_number = ""
#
#infos_selector = soup.find_all('div', class_='col-xs-5')
#for info_selector in infos_selector:
#    right_div = info_selector.find('span', class_='btn-height-sm')
#    if right_div:
#      email_info = right_div.get_text()
#      emailNoSpape = email_info.split('\n          ')[1]
#      email_number = emailNoSpape.split('.')[0]
#      email_decimal = (email_info.split('.')[1])[0]
#      email_count = email_number + "." + email_decimal + "K"

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
