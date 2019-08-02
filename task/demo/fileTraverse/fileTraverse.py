#!/usr/bin/env python
# -*- coding: utf-8 -*-

' file traverser '

__author__ = 'Bob'

import os, re

regs = [r'.*name\sis\s(\S+),', r'.*(\d{3}-\d{3}-\d{3})', r'I\slove\s(\S+).']

files = os.listdir(os.path.abspath('text'))

def readFile(file):
    content = open(file).read()
    for i in range(len(regs)):
        matcher = re.compile(regs[i])
        if(i == 0):
            name = matcher.search(content).group(1)
        if(i == 1):
            phoneNumber = matcher.search(content).group(1)
        if(i == 2):
            like = matcher.search(content).group(1)
    print('name: ' + name + ' phoneNumber: ' + phoneNumber + ' like: ' + like)

if __name__ == '__main__':
    path = os.path.abspath('text')
    #traverse file
    for file in files:
        if (file.index('.txt')):
            readFile(os.path.join(path, file))
