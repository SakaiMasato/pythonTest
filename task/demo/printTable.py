#! python3
# -*- coding: utf-8 -*-

' print table'

__author__  = 'Bob Bao'

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def getMaxLen(arr):
    length = 0;
    for word in arr:
        if int(len(word)) > length:
            length = int(len(word))
    return length;

def getColWidth(datas):
    colWidths = []
    for data in datas:
        len = getMaxLen(data)
        colWidths.append(len)
    return colWidths

def printTable(datas, colWidth):
    for i in range(len(datas[0])):
        for j in range(len(datas)):
            if(j == 0):
                print(datas[j][i].rjust(colWidth[j]),end=' ')
            else:
                print(datas[j][i].ljust(colWidth[j]),end=' ')
        print()

if __name__ == '__main__':
    colWidths = getColWidth(tableData)
    printTable(tableData, colWidths)

