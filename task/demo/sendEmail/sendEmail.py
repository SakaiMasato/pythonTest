#!/usr/bin/env python
# -*- coding: utf-8 -*-

' email sender (126)'

__author__ = 'Bob'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time,logging,sys
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

#define target, subject, content
params = sys.argv

def automatedEmail(target, subject, content):
    browser = webdriver.Chrome()
    browser.get('https://baidu.com')
    browser.find_element_by_id('kw').send_keys('126')
    browser.find_element_by_id('su').click()
    time.sleep(5)
    logging.info('input account and password')
    browser.find_element_by_id('op_email3_username').send_keys('bao_xiong_wei')
    browser.find_element_by_class_name('op_email3_password').send_keys('951028')
    browser.find_element_by_class_name('op_email3_submit').click()
    logging.info('mail box login successfully')

    logging.info('to edit email page')
    search_handle = browser.current_window_handle  # save search_handle for recovering env
    handles = browser.window_handles
    browser.switch_to.window(handles[len(handles) - 1])  # swith to email window
    time.sleep(5)
    browser.find_element_by_id('_mail_component_24_24').click()

    logging.info('start to write email')
    time.sleep(3)
    browser.find_element_by_class_name('nui-editableAddr-ipt').send_keys(target)
    browser.find_element_by_css_selector('input[id$="_subjectInput"]').send_keys(subject)
    mail_handle = browser.current_window_handle  # save mail_handle for recovering env
    browser.switch_to.frame(
        browser.find_element_by_xpath(r'//iframe[@class="APP-editor-iframe"]'))  # switch to frame due to rich text
    browser.find_element_by_class_name('nui-scroll').send_keys(Keys.TAB)
    browser.find_element_by_class_name('nui-scroll').send_keys(content)
    browser.switch_to.window(mail_handle)  # recover mail env

    browser.find_element_by_id("_mail_icon_35_190").click()
    logging.info("submit done")
    time.sleep(5)

if(len(params)== 4):
    target = params[1]
    subject = params[2]
    content = params[3]
    automatedEmail(target, subject, content)
else:
    logging.error('please check params target, subject, content')

