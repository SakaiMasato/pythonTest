#!/usr/bin/env python
# -*- coding: utf-8 -*-

' standardize the file name '

import os

path = os.path.abspath('standardizeFileName')
#print(path)
files = os.listdir(path)
indexs = []
index = {}
for i in range(len(files)):
    index['k'] = i
    index['v'] = files[i]
    indexs.append(index)
    if(files[i].find(str(i))<0):
        print(indexs[len(indexs)-1])