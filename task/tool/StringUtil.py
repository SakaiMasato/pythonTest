#!/usr/bin/env python
# -*- coding: utf-8 -*-

' String util '

__author__ = 'Bob Bao'

'''
    isalpha(): only string
    isalnum(): string and number
    isdecimal(): only number
    isspace(): space, TAB, and \n
    istitle(): start with capital letter concat lowercase
    startswith()
    endswith()
    join(): ' '.join(['My', 'name', 'is', 'Bob'])
    split(): 'aABCbABCcABC'.split('ABC')
    rjust(), ljust() center(): 
    strip():    Hello   ==>Hello :remove left and right space
'''

if __name__ == '__main__':
    print('Hello'.ljust(10,'*'))