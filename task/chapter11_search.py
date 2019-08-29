#!/usr/bin/env python
# -*- coding: utf-8 -*-

' search in Baidu '

__author__ = 'Bob'

import webbrowser,pyperclip,sys

#set chrome as default browser
chromepath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromepath))

param = pyperclip.paste()
baiduUrl = "https://www.baidu.com/s?wd=" + param;
webbrowser.get('chrome').open(baiduUrl)
