#!/usr/bin/env python
# -*- coding: utf-8 -*-

' file traverse then rename the date from MM-DD-YYYY to MM-DD-YYYY '

__author__ = 'Bob'

import os, re

path = os.path.join(os.path.abspath('.'), 'renameDatesDatas')

filePaths = os.listdir(path)

def findAmericanDate(str):
    regex = r'''
        ((0\d)|(1[012]))              #MM
        -                           #separator
        ((0\d)|([12]\d)|(3[01]))      #DD
        -                           #separator
        (\d{1,})                      #YYYY
    '''
    matcher = re.compile(regex, re.VERBOSE)
    return matcher.search(str)

if __name__ == '__main__':
    for filePath in filePaths:
        filePath = os.path.join(path, filePath)
        file = open(filePath)
        str = file.read()
        mo = findAmericanDate(str)
        if(mo is not None):
            MM = mo.group(1)
            DD = mo.group(4)
            YYYY = mo.group(8)
            print(DD,'-',MM,'-',YYYY)

