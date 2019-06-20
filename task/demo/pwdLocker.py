#! python3
# -*- coding: utf-8 -*-

' insecure pwd locker '

__author__ = 'Bob Bao'

PASSWORDS = {'wechat': '123456',
             'qq': 'abcdefg'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pwdLocker.py [account]')
    sys.exit()

account = sys.argv[1] # argv[0] is filename, argv[1] is account

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account);