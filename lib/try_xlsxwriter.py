# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:40:40 2020

@author: Carlesso
"""


import xlsxwriter
import datetime


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('dati_orari.xlsx')
worksheet = workbook.add_worksheet(name="")


header = ["timestamp", "temperature"]
# Some data we want to write to the worksheet.
expenses = (
    ['2020-01-01 12:00', -4],
    ['2020-01-01 12:10',  -2],
    ['2020-01-01 12:10',  2],
    )


# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# write the header row

worksheet.write(row, col, header[0])
worksheet.write(row, col+1, header[1])

row +=1
# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()