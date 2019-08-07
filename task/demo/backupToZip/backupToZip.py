#!/usr/bin/env python
# -*- coding: utf-8 -*-

' backup to zip '

__author__ = 'Bob'

import os, zipfile, datetime

#path = os.path.abspath('.')

date = datetime.datetime.today()

print('creating zip package')
zipPack = zipfile.ZipFile('backup_' + date.strftime('%Y-%m-%d') + '.zip', 'w')

for folderName, subfolders, fileNames in os.walk('.'):
    print('Adding files in ', folderName)
    zipPack.write(folderName)
    for fileName in fileNames:
        if fileName.endswith('.zip'):
            continue # do not backup the backup file
        zipPack.write(os.path.join(folderName, fileName))

zipPack.close()