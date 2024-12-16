#!/usr/bin/env python3
import xlsxwriter
import json
filename = 'notes.xlsx'
workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet('Full 0')

worksheet.write(f'I1', 'Valid')
percentatges = ['10%','10%','10%','20%','50%']
with open('notes.json') as f:
    data = json.load(f)
    column = 3
    row = 2
    for element in data:
        keys = element.keys()
        worksheet.write(f'A{column}', element['Name'])
        column += 1
        col = 1
        fil = 2 
        for key in keys:
            worksheet.write_row(1,1,percentatges)

            if key in ['PR01', 'PR02', 'PR03', 'PR04', 'EX01']:
                worksheet.write(fil, col, element[key])  
                worksheet.write_row(0, 0, keys)
                col += 1

workbook.close()
print(f"Genearated: '{filename}'")







