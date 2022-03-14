import warnings
warnings.filterwarnings('ignore')


# import required modules
import datetime
import json
import pandas as pd
import requests
import time

from splinter import Browser

# splinter set up
path_ = '/Volumes/GoogleDrive/My Drive/508/chromedriver'
executable_path = {'executable_path':path_}


# launch browser and point to URL
browser = Browser('chrome', **executable_path)
url = 'https://www.weather.gov/sgx/cliplot'
browser.visit(url)


years = ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]


browser.click_link_by_href('#tabs-4')
year_list = browser.find_by_id('PrevCalYear')





year = '2009'
for month in months:
    # click on wanted month
    browser.find_by_id('MonthRow').find_by_xpath(f"//button[normalize-space()='{month}']").click()

    # Pause & allow website to materialize
    time.sleep(2)

    # Pull HTML & convert to pd.DFs
    html = browser.find_by_id('PrevDataTable').html
    dfs = pd.read_html(html)

    dfs[0].to_csv(f'{year}_{month}.csv')

    # allow system to complete above tasks
    time.sleep(1)



