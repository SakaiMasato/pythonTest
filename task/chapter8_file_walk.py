#!/usr/bin/env python
# -*- coding: utf-8 -*-

' file walk '

__author__ = 'Bob'

import os, zipfile

# shutil : shutil.copy(source, destination), copyTree 将复制整个文件夹
#          shutil.move(source, destination)
# os.unlink(path): 删除path的文件 os.rmdir: 删除文件夹， 文件夹里面不能有文件 shutil.rmtree(path) 删除所有 不可恢复！！！
# send2Trash.send2Trash(path): 删除path的文件，To回收站
path = r'C:\\ericsson\\book'
for foldName, subfolders, fileNames in os.walk(path):
    print(foldName)

    for subfolder in subfolders:
        print(subfolder)

    for fileName in fileNames:
        print(fileName)

# compress
os.chdir(path)
exampleZip = zipfile.ZipFile('book.zip')
fileInfo = exampleZip.getinfo('Regular-Expression-Tutorial.pdf')
print('zipFileLList: ', exampleZip.namelist(), 'fileSize: ', fileInfo.file_size, 'compress: ', fileInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(fileInfo.file_size / fileInfo.compress_size, 2)))
exampleZip.close()

# extract all
'''
os.chdir(path)
exampleZip = zipfile.ZipFile('book.zip')
exampleZip.extractall()
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders') 解压到指定文件夹
exampleZip.close()
'''

# create zip file //全量写入
os.chdir(path)
exampleZip = zipfile.ZipFile('book.zip', 'w')
exampleZip.write('Oreilly.JavaScript.The.Good.Parts.May.2008.pdf', compress_type=zipfile.ZIP_DEFLATED)
exampleZip.close()
