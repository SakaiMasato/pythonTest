#!/usr/bin/env python
# -*- coding: utf-8 -*-

' web stuff '

__author__ = 'Bob'

#selenium 和 req 的区别 ， selenium无法后端静默操作
import requests,logging,bs4,time
from selenium import webdriver
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

# selenium stuff
browser = webdriver.Chrome()
browser.get('https://baidu.com')
'''
    browser.find_element_by_class_name(name)
    browser.find_elements_by_class_name(name)           使用CSS 类name 的元素
    browser.find_element_by_css_selector(selector)
    browser.find_elements_by_css_selector(selector)     匹配CSS selector 的元素
    browser.find_element_by_id(id)
    browser.find_elements_by_id(id)                     匹配id 属性值的元素
    browser.find_element_by_link_text(text)
    browser.find_elements_by_link_text(text)            完全匹配提供的text 的<a>元素
    browser.find_element_by_partial_link_text(text)
    browser.find_elements_by_partial_link_text(text)    包含提供的text 的<a>元素
    browser.find_element_by_name(name)
    browser.find_elements_by_name(name)                 匹配name 属性值的元素
    browser.find_element_by_tag_name(name)
    browser.find_elements_by_tag_name(name)             匹配标签name 的元素(大小写无关，<a>元素匹配'a'和'A')
'''
time.sleep(5)
search_box = browser.find_element_by_id('kw')
search_box.send_keys('wiki')
search_box.submit()
time.sleep(5)
browser.quit()

'''
    from selenium.webdriver.common.keys import Keys
    
    Keys.DOWN, Keys.UP, Keys.LEFT,Keys.RIGHT 键盘箭头键
    Keys.ENTER, Keys.RETURN 回车和换行键
    Keys.HOME, Keys.END,
    Keys.PAGE_DOWN,Keys.PAGE_UP
    Home 键、End 键、PageUp 键和Page Down 键
    Keys.ESCAPE, Keys.BACK_SPACE,Keys.DELETE Esc、Backspace 和字母键
    Keys.F1, Keys.F2, . . . , Keys.F12 键盘顶部的F1 到F12 键
    Keys.TAB Tab 键
    
    browser.back()
    browser.forward()
    browser.refresh()
    browser.quit()
'''


