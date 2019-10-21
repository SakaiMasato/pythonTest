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
