#!/usr/bin/env python
# -*- coding: utf-8 -*-

' Mad libs game '

__author__ = 'Bob'

import os, re
#read msg from file
path = os.path.join(os.path.abspath('.'), 'text')
fileR = open(path)
msg = fileR.read()
templates = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']


#return result
#map ADJECTIVE, NOUN, ADVERB, VERB
def templateMapping(template, msg):
    matcher = re.compile(template)
    return matcher.findall(msg)

if __name__ == '__main__':
    #modify template
    for tmp in templates:
        results = list(templateMapping(tmp, msg))
        for r in results:
            print('Enter a ', r)
            incoming = str(input())
            msg = msg.replace(r,incoming,1)
print(msg)


