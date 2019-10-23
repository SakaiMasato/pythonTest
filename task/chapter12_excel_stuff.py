#! python3
# -*- coding: utf-8 -*-

' excel stuff '

__author__ = 'Bob Bao'

import openpyxl, logging
from openpyxl.utils import get_column_letter, column_index_from_string
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

wb = openpyxl.load_workbook('bob.xlsx')
logging.info(type(wb))
sheet = wb.worksheets[0]                                                                            #first sheet
logging.info('first worksheet: ' + sheet.title)
logging.info('first cell: value-' + sheet['A1'].value + ' row-' + str(sheet['A1'].row) + ' column-' + str(sheet['A1'].column) + ' coordinate-' + sheet['A1'].coordinate)
logging.info('first cell: value-' + sheet.cell(1,1).value+ ' row-' + str(sheet.cell(1,1).row) + ' column-' + str(sheet.cell(1,1).column) + ' coordinate-' + sheet.cell(1,1).coordinate)
logging.info('len(row): ' + str(sheet.max_row))
logging.info('len(column): ' + str(sheet.max_column))
logging.info('translate int to str: ' + get_column_letter(sheet.max_row))
logging.info('translate str to int: ' + str(column_index_from_string('B')))
logging.info(tuple(sheet['A1': 'C3']))

logging.info('=================excel write==================')
wb1 = openpyxl.Workbook()       ##create a new workbook
sheet1 = wb1.worksheets[0]
logging.info('sheet title: ' + sheet1.title)        #default sheet name is 'Sheet'
sheet1.title = 'Spam Bacon Eggs sheet'              ##Modify first sheet name
logging.info('sheet title: ' + sheet1.title)
wb1.save('bobTestExcel.xlsx')

wb2 = openpyxl.Workbook()
wb2.create_sheet()
wb2.create_sheet(index=0, title='1st sheet')
wb2.create_sheet(index=2, title='middle sheet')
sheet2 = wb2['middle sheet']
sheet2.cell(1,1).value = 'Hello world'
logging.info(sheet2['A1'].value)
