#!/usr/bin/env python
# -*- coding: utf-8 -*-

' chapter4 task '

__author__ = 'Bob Bao'

def concatStr(arr):
    res = ""
    index = 0
    for str in arr:
        if index == len(arr) - 1:
            res += 'and ' + str
        else:
            res += str + ', '
        index += 1
    return res;

def countWord(str):
    count = {}
    for cha in str:
        count.setdefault(cha, 0)
        count[cha] += 1
    return count

if __name__ == '__main__':
    #task1
    spam = ['apples', 'bananas', 'tofu', 'cats']
    res = concatStr(spam)
    print(res)

    #task2
    str = 'Everything that downs me makes me wanna fly'
    count = countWord(str)
    print(count)