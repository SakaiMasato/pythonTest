#!/usr/bin/env python
# -*- coding: utf-8 -*-

' collaz series '

__author__ = 'Bob Bao'
def oddOrEven (number):
    if (number % 2 == 0):
        return number // 2
    else:
        return 3 * number + 1

def collaz (number):
    return oddOrEven(number)


if __name__ == '__main__':
    print('please input a number: ', end='')
    try:
        inputNum = int(input())
    except ValueError:
        print('Error: please input a number')
    while inputNum != 1:
        print(inputNum)
        inputNum = collaz(inputNum)
    print(inputNum)