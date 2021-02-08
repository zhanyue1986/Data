# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:25:15 2021

@author: Jiayiying
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def get_html(url):
    chrome_driver = "D:\Program Files\Anaconda\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(executable_path = chrome_driver)
    driver.get(url)
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    return soup

def analyze(soup):
    temp=soup.find('div',class_='tslb_b')
    columns = []
    #print(temp)
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        temp1 = {}
        column_index = 0
        if len(td_list) > 0:
            for td in td_list:
                temp1[columns[column_index]] = td.text
                column_index += 1
            df = df.append(temp1,ignore_index = True)
        
        else:
            th_list = temp.find_all('th')
            for th in th_list:
                columns.append(th.text)
            df = pd.DataFrame(columns=columns)
    return(df)
                

base_url = "http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-"
page_num = 2
result = pd.DataFrame([])
for i in range(page_num):
    url = base_url + str(i+1) + '.shtml'
    soup = get_html(url)
    df = analyze(soup)
    result = result.append(df)
print(result)
result.to_excel('car_complain_data1.xlsx', index = False)