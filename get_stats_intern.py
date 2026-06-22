from genericpath import exists
from time import sleep
from tokenize import String
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from datetime import date, datetime
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from turtle import clear
import sqlite3
import instaloader
from TikTokApi import TikTokApi
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# BROWSER AUTOMATION

# SETUP GECKODRIVER WEBDRIVER TO USE WITH SELENIUM AND FIREFOX HEADLESS
options = Options()
options.add_argument('--headless')
s = Service('/Users/neto/ARDUINO/CounterSnapAll/geckodriver')
driver = webdriver.Firefox(service=s, options=options)
driver.implicitly_wait(10)

# SCRAP EMAIL COUNT ON RD STATION (BRAZIL/LATAM CRM PLATFORM)
# NOTE: ALL SCRAPED STRINGS MUST BE CONVERTED TO THE FORMAT "XX.XX K"
with sync_playwright() as p:
    browser = p.chromium.launch(headless = True, slow_mo=50)
    page = browser.new_page()
    page.goto('https://app.rdstation.com.br/leads?utf8=%E2%9C%93&query=&segmentation_list=7174454')
    page.fill('input#email','neto@spinoff.digital')
    page.fill('input#password','061231(RDStation)')
    page.click('button[type=submit]')
    page.is_visible('div.slats-heading')
    html = page.inner_html('span.btn-height-sm')
    soup = BeautifulSoup(html,'html.parser')   
    email_info = soup.get_text()
    email_number = email_info.split('.')[0] #99
    email_decimal1 = (email_info.split('.')[1]).split(' ')[0]  
    email_decimal = email_decimal1[0]
    email_count = email_number + "." + email_decimal + "K"




           
## SCRAPE YouTube BRAZIL FOLLOWERS
#driver.get('https://www.youtube.com/c/SnapdragonBrasil')
#youtube_count = driver.find_element(By.ID,'subscriber-count').text.split(' ')[0]
#youtube_mil = youtube_count.split('.')[0]
#
#try:
#   youtube_dec = (youtube_count.split('.')[1])[0]
#   youtube_count = youtube_mil + "." + youtube_dec + "K"
#except ValueError:
#    youtube_count = youtube_mil
#
### SCRAPE YouTube LATAM FOLLOWERS
#driver.get('https://www.youtube.com/c/SnapdragonLatam')
#youtube_countL = driver.find_element(By.ID,'subscriber-count').text.split(' ')[0]
#youtube_milL = youtube_countL.split('.')[0]
#try:
#    youtube_decL = (youtube_countL.split('.')[1])[0]
#    youtube_countL = youtube_milL + "." + youtube_decL + "K"
#except ValueError:
#    youtube_countL = youtube_milL + "K"


## SCRAPE TikTok BRAZIL FOLLOWERS - SELENIUM PYTHON LIBRARY + GECKODRIVE
driver.get('https://www.tiktok.com/@snapdragon_brasil')
tiktok_countB = driver.find_element(By.XPATH,'//*[@id="main-content-others_homepage"]/div/div[1]/h3/div[2]/strong').text
print(tiktok_countB)

## SCRAPE TikTok LATAM FOLLOWERS - SELENIUM PYTHON LIBRARY + GECKODRIVE
driver.get('https://www.tiktok.com/@snapdragon_latam')
tiktok_countL = driver.find_element(By.XPATH,'//*[@id="main-content-others_homepage"]/div/div[1]/h3/div[2]/strong').text
print(tiktok_countL)

tiktokNumberB = float(tiktok_countB.split('K')[0])
print(tiktokNumberB)



## SCRAPE Twitter BRAZIL FOLLOWERS - SELENIUM PYTHON LIBRARY + GECKODRIVER
#driver.get('https://twitter.com/snapdragon_BRA')
#twitter_count = driver.find_element(By.CSS_SELECTOR,'a[href="/snapdragon_BRA/followers"] > span > span').text
#
## SCRAPE Twitter LATAM FOLLOWERS - SELENIUM PYTHON LIBRARY + GECKODRIVER
#driver.get('https://twitter.com/snapdragon_LAT')
#twitter_countL = driver.find_element(By.CSS_SELECTOR,'a[href="/snapdragon_LAT/followers"] > span > span').text
#
## SCRAPE Instagram BRAZIL AND LATIM FOLLOWERS - INSTALOADER PYTHON LIBRARY
#L = instaloader.Instaloader()
##L.login(user="neto_netohouse",passwd="061231(Counter)")
##L.login(user="mentor_neto",passwd="638612(password)")
#profile = instaloader.Profile.from_username(L.context, "snapdragon_brasil")
#profile2 = instaloader.Profile.from_username(L.context, "snapdragon_latam")
#instaBR_mil = str(profile.followers)[:3]
#instaBR_dec = str(profile.followers)[2]
#instagram_count = instaBR_mil + "." + instaBR_dec + "K"
#instaLT_mil = str(profile2.followers)[:2]
#instaLT_dec = str(profile2.followers)[2]
#instagram_countL = instaLT_mil + "." + instaLT_dec + "K"
#
# CLOSE GECKODRIVER WEBDRIVER - MAKE SURE TO SLEEP 5 TO CLOSE ALL INSTANCES OF FIREFOX
#sleep(5)
#driver.close()
#
## CREATE GRAPHIC
#
## PARSE ALL CONVERTES XX.XX K STRINGS TO FLOATS TO CALCULATE TOTAL FOLLOWERS, THEN CONVERT BACK TO STRING
#emailNumber = float(email_count.split('K')[0])
#email_count = str(emailNumber) + "K"
#youtubeBrNumber = float(youtube_count.split('K')[0])
#youtubeLNumber = float(youtube_countL.split('K')[0])
#twitterBrNumber = float(twitter_count.split('K')[0])
#twitterLtNumber = float(twitter_countL.split('K')[0]) 
#instaBrNumber = float(instagram_count.split('K')[0])
#instagram_count = str(instaBrNumber) + "K"
#instaLtNumber = float(instagram_countL.split('K')[0])
#instagram_countL = str(instaLtNumber) + "K"
#
#totalFF = emailNumber + youtubeBrNumber + youtubeLNumber + instaBrNumber + twitterBrNumber + instaLtNumber + twitterLtNumber
#
#totalFF = round(totalFF,1)
#
#if len(str(totalFF)) == 5:
#    totalFFS = str(totalFF) + "M (Congrats Team!)"
#else:
#    totalFFS = str(totalFF) + "K"
#
#
## print data
#print("eMail: ",email_count,"YouTubeBR: ", youtube_count,"TwitterBR: ", twitter_count,"InstagramBR: ", instagram_count,"YouTubeLT: ", youtube_countL,"TwitterLT: ", twitter_countL,"InstagramLT: ", instagram_countL,"TOTAL: ", totalFFS)
#
#