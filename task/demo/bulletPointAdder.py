#! python3
# -*- coding: utf-8 -*-

' add bullet point'

__author__  = 'Bob Bao'

import sys, pyperclip

text = pyperclip.paste()

# to add bullet point
bulletPoint = sys.argv[1] # bulletpoint is from cmd

lines = text.split('\n')
for i in range(len(lines)):
    if (lines[i].strip() == ''):
        continue
    lines[i] = '*' + lines[i]
text = '\n'.join(lines);

pyperclip.copy(text)

