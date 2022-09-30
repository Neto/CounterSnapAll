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

# SCRAPE Instagram BRAZIL AND LATIM FOLLOWERS - INSTALOADER PYTHON LIBRARY
L = instaloader.Instaloader()
L.login(user="neto_netohouse",passwd="061231NetoHouse")
profile = instaloader.Profile.from_username(L.context, "snapdragon_brasil")

# Print list of followees
follow_list = []
count = 0
for followee in profile.get_followers():

    profile2 = instaloader.Profile.from_username(L.context, followee.username)
    instaBR_mil = str(profile2.followers)

    userData = str(followee.username, "-", instaBR_mil)

    follow_list.append(userData)
    

    file = open("followers.txt", "a+")

    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count = count + 1
# (likewise with profile.get_followers())



# CLOSE GECKODRIVER WEBDRIVER - MAKE SURE TO SLEEP 5 TO CLOSE ALL INSTANCES OF FIREFOX
sleep(5)
driver.close()

