#! python3
# -*- coding: utf-8 -*-

# multiContentInClipboard.pyw - Saves and loads pieces of text to the clipboard.
# Usage:
# python.exe multiContentInClipboard.pyw save <keyword> - Saves clipboard to keyword.
# python.exe multiContentInClipboard.pyw <keyword> - Loads keyword to clipboard.
# python.exe multiContentInClipboard.pyw list - Loads all keywords to clipboard.
# python.exe multiContentInClipboard.pyw delete <keyword> - delete keyword
# python.exe multiContentInClipboard.pyw delete - delete all keyword

__author__  = 'Bob Bao'

import sys, pyperclip, shelve

param = sys.argv[1] #cmd command

text = pyperclip.paste() #content in clipboard

# file
line = 0
file = shelve.open('notebook')

if len(sys.argv) == 3:
    spam = sys.argv[2]  # keyword
    if param == 'save':
        file[spam] = text
    if param == 'delete':
        file.pop(spam)
elif len(sys.argv) == 2:
    if param == 'list':
        pyperclip.copy(str(list(file.keys())))
    elif param == 'delete':
        file.clear()
    else:
        spam = param
        pyperclip.copy(str(file[spam]))

file.close()



