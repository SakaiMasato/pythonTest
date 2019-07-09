#! python3
# -*- coding: utf-8 -*-

' re '

__author__  = 'Bob Bao'

import re

def regMatch (str, reg):
    matcher = re.compile(reg)
    mo = matcher.search(str)
    return mo
if __name__ == '__main__':
    # match phone number
    msg = 'my phone number is 415-555-4242'
    reg = r'\d{3}-\d{3}-\d{4}'
    pNumber = regMatch(msg, reg)
    print('match Phone Number' + pNumber.group())

    #groups
    regGroup = r'(\d{3})-(\d{3}-\d{4})'
    pNumberGp = regMatch(msg, regGroup)
    print(pNumberGp.group(1)+ ' ' + pNumberGp.group(2) + ' ' + pNumberGp.group())
    areaCode, mainNumber = pNumberGp.groups()
    print('groups' + areaCode + ' ' + mainNumber)

    #pipeline
    heroReg = r'batMan|superMan'
    heros = 'batMan and superMan'
    print('pipeline(|)' + regMatch(heros, heroReg).group())

    #hero equipments
    heroESReg = r'bat(mobile|car|gun)'
    herosES = 'batcar batmobile batgun'
    print('hero equipments ' + regMatch(herosES, heroESReg).group())

    # ? match
    #  (\d{3})?
    # 匹配 ? 之前的表达式 1 次或 0 次， (\d{3})*    0 次或 多 次     (\d{3})+  1 次或 多 次

    #findall()
    PNMessage = 'my phone number is 415-555-4242， your phone number is 212-555-0000'
    matcher1 = re.compile(r'\d{3}-\d{3}-\d{4}')
    res = matcher1.findall(PNMessage)
    print('findall():', res)

    #贪心 非贪心
    #re.compile(r'.*', re.DOTALL)通过传递re.DOTALL来匹配换行符， re.I(re.IGNORECASE)作为第二个参数，部分大小写匹配，
    # re.VERBOSE 作为第二个参数 可以将正则放在多行并可以加注释
    greedyRe = re.compile(r'<.*>')
    nonGreedyRe = re.compile(r'<.*?>')
    ttMsg = '<To serve man> for dinner>'
    print('greedy: ' + greedyRe.search(ttMsg).group())
    print('non greedy:' + nonGreedyRe.search(ttMsg).group())

    '''
    p.s.
     ? 匹配0次或1次
     * 匹配0次或多次
     + 匹配1次或多次
     {n}匹配n次前面的分组
     {n,}匹配n次或多次前面的分组
     {,m}匹配0次或m次前面的分组
     {n,m}匹配n次到m次前面的分组
     {n,m}?或*?或+?非贪心匹配
     ^spam以spam为首
     spam$以spam结尾
     .匹配一个所有字符，换行符\n除外
     \d,\w,\s分别匹配数字,单词，空格
     \D,\W,\S分别匹配数字，单词，空格以外
     [abc]匹配a,b,c任意字符
     [^abc]匹配不在abc之内的字符
    '''
