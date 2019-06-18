#!/usr/bin/env python
# -*- coding: utf-8 -*-

' guess number game '

__author__ = 'Bob Bao'

try_number = 7

def game_logic(num):
    global try_number
    index = 0
    while index < try_number:
        print('please guess the number, range from 1~10: ', end='')
        guess_number = int(input())
        if (guess_number == num):
            print('bingo! you did it!')
            return
        elif (guess_number < num):
            print('your number is less than answer')
        else:
            print('your number is greater than answer')
        index += 1
    print('you have run out of all the chances')

if __name__ == '__main__':
    game_logic(4)