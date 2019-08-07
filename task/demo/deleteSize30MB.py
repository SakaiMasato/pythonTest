#!/usr/bin/env python
# -*- coding: utf-8 -*-

' delete file which size larger than 30MB '

__author__ = 'Bob'

import os, send2trash, shutil

path = r'C:\ericsson\book'

for folderName, subForders, filenames in os.walk(path):
    for fileName in filenames:
        filePath = os.path.join(folderName, fileName)
        #print(fileName , ' ', os.path.getsize(filePath)/1000/1000)
        size = os.path.getsize(filePath)/1000/1000
        if size >= 30:
            #send2trash(fileName)
            #os.unlink(fileName)
            print(fileName, ' ', size, 'MB')
