#!/usr/bin/env python
# -*- coding: utf-8 -*-

' search something in Baidu by cmd '

__author__ = 'Bob'

import webbrowser, pyperclip, bs4, logging, requests

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
chromepath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))


### param: param you want to search
### n: the link number you want to open
def search(param, n):
    logging.info('.............baiduing.............')
    baidu = "http://baidu.com/s?wd=" + param
    res = requests.get(baidu)
    try:
        res.raise_for_status()
    except Exception as e:
        logging.error('there is something issue: ' + e)
        return
    logging.info('............baidu done..............')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    a = soup.select('.t a')
    elementNum = min(5, n)
    for i in range(elementNum):
        webbrowser.get('chrome').open(a[i].get('href'))


param = pyperclip.paste()
search('炉石啦啦啦', 3)
