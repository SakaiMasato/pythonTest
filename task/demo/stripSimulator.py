#! python3
# -*- coding: utf-8 -*-

' strip simulator'

__author__ = 'Bob'

import re
def myStrip(text, str):
    if str is None:
        regex = r'\s+'
    regex = str
    matcher = re.compile(regex)
    print(matcher.sub('', text))

if __name__ == '__main__':
    myStrip('   abc   ', 'b')