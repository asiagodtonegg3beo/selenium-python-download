from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import os
import sys

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 01:38:55 2021

@author: Fuckyoubitch
"""



def dwn(url:str) ->str :
    os.system('sudo ./i.sh')
    time.sleep(6)

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")

#    url = sys.argv[1]
    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get(url)

    time.sleep(2)
    chrome.find_element_by_class_name('downloadbtn').click()
    time.sleep(61)
    chrome.find_element_by_id('downloadbtn').click()
    print('click dwn button')

    time.sleep(2)
    #chrome.switch_to.window(chrome.current_window_handle)
    #url = chrome.current_url
    #print(url)
    #chrome.get(url)
    #dwnurl = chrome.find_elements_by_tag_name("a")
    #print(dwnurl)
    #for i in dwnurl:
    #    print(i.get_attribute('href'))
    html = chrome.page_source
    dwnurl = chrome.find_element_by_class_name('files_list--active')
    durl = dwnurl.get_attribute('href')
    print(durl)
    chrome.close()
    return durl

queue = []
out = []
f = open('url.txt','r')
for i in f.readlines():
    queue.append(i)
while queue != []:
    out.append(dwn(queue[0]))
    print('done')
    del queue[0]

for i in out:
    print(i)
