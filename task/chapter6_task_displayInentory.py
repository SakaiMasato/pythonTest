#!/usr/bin/env python
# -*- coding: utf-8 -*-

' display inventory '

__author__ = 'Bob Bao'

def displayInventory(dic):
    print('Inventory:')
    totalNum = 0
    for k, v in dic.items():
        print(k,' ',v)
        totalNum += v
    print('Total number of items: ', totalNum)

def addToInventory(inventory, addedItems):
    for k1, v1 in addedItems.items():
        inventory.setdefault(k1, 0)
        inventory[k1] += v1
    return;

if __name__ == '__main__':
    dic = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
    displayInventory(dic)
    print('kill a dragon')
    dragonLoot = {'gold coin':5, 'dagger':1, 'ruby':1}
    addToInventory(dic, dragonLoot)
    displayInventory(dic)