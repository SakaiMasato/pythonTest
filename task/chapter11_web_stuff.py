#!/usr/bin/env python
# -*- coding: utf-8 -*-

' web stuff '

__author__ = 'Bob'

import requests

if __name__ == '__main__':
    baiduObj = requests.get('https://www.baidu.com')
    print(type(baiduObj))
    print(baiduObj.text)