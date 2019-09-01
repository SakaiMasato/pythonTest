#!/usr/bin/env python
# -*- coding: utf-8 -*-

' web stuff '

__author__ = 'Bob'

import requests,logging,bs4
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


if __name__ == '__main__':
    baiduObj = requests.get('https://www.baidu.com')
    #baiduObj.raise_for_status()//if successful do nothing, or raise exception
    print(type(baiduObj))
    print(baiduObj.text)

    try:
        baiduObj.raise_for_status()#check status
    except Exception as e:
        print(logging.debug('there is a issue: ',e))
'''
    file = open('webPage.txt', 'wb')
    for chunk in baiduObj.iter_content(100000): #每十万字节一段
        file.write(chunk)

    file.close()
'''
#use BeautifulSoup module
'''
    soup.select('div') 所有名为<div>的元素
    soup.select('#author') 带有id 属性为author 的元素
    soup.select('.notice') 所有使用CSS class 属性名为notice 的元素
    soup.select('div span') 所有在<div>元素之内的<span>元素
    soup.select('div > span') 所有直接在<div>元素之内的<span>元素，中间没有其他元素
    soup.select('input[name]') 所有名为<input>，并有一个name 属性，其值无所谓的元素
    soup.select('input[type="button"]') 所有名为<input>，并有一个type 属性，其值为button 的元素
'''
openFile = open('webPage.txt', encoding='utf8')
exampleSoup1 = bs4.BeautifulSoup(openFile.read(), 'lxml') #from file
exampleSoup2 = bs4.BeautifulSoup(baiduObj.text, 'lxml') #from resp
ftConw = exampleSoup1.select('.cp-feedback');
logging.debug(type(ftConw[0]))
logging.debug(ftConw[0].getText())
logging.debug(ftConw[0])
logging.debug(ftConw[0].attrs)