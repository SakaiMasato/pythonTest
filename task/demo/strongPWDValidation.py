#! python3
# -*- coding: utf-8 -*-

' strong password validation'

import re
def strongPasswordValidation(pwd):
    regex = r'(([A-Z])?([a-z])?(\d)?){8,}'
    matcher = re.compile(regex)
    print(matcher.search(pwd).group())
if __name__ == '__main__':
    strongPasswordValidation('azA8fmskal5')
