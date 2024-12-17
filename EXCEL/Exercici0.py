#!/usr/bin/env python3
import xlsxwriter
import json

filename = 'notes.xlsx'
workbook = xlsxwriter.Workbook(f"EXCEL/{filename}")
worksheet = workbook.add_worksheet('Full 0')

worksheet1 = workbook.add_worksheet('Full 1')
lista_columns = ['B','C','D','E','F','G','H','I']
titols = ["Name", "PR01", "PR02", "PR03", "PR04", "EX01", "%Faltes", "Valid", "Nota Final"]
titols_pag_2 = ["id", "PR01", "PR02", "PR03", "PR04", "EX01", "%Faltes", "Valid", "Nota Final"]
percentatges = ['10%', '10%', '10%', '20%', '50%']


#ESTILS FULLS 0
worksheet.conditional_format("B3:F34", { 
    'type': 'cell',
    'criteria': '<',
    'value': 5,
    'format': workbook.add_format({'bg_color': '#FF0000', 'font_color': '#000000', 'align': 'center', 'valign': 'vcenter'})
})
worksheet.conditional_format("I3:I34", { 
    'type': 'cell',
    'criteria': '<',
    'value': 5,
    'format': workbook.add_format({'bg_color': '#FF0000', 'font_color': '#000000', 'align': 'center', 'valign': 'vcenter'})
})
worksheet.conditional_format("I3:I34", { 
    'type': 'cell',
    'criteria': '>=',
    'value': 7,
    'format': workbook.add_format({'bg_color': '#00ff00', 'font_color': '#000000', 'align': 'center', 'valign': 'vcenter'})
})
#ESTILS FULL 1
worksheet1.conditional_format("B3:F34", { 
    'type': 'cell',
    'criteria': '<',
    'value': 5,
    'format': workbook.add_format({'bg_color': '#FF0000', 'font_color': '#000000', 'align': 'center', 'valign': 'vcenter'})
})
worksheet1.conditional_format("I3:I34", { 
    'type': 'cell',
    'criteria': '<',
    'value': 5,
    'format': workbook.add_format({'bg_color': '#FF0000', 'font_color': '#000000', 'align': 'center', 'valign': 'vcenter'})
})
worksheet1.conditional_format("I3:I34", { 
    'type': 'cell',
    'criteria': '>=',
    'value': 7,
    'format': workbook.add_format({'bg_color': '#00ff00', 'font_color': '#000000', 'align': 'center', 'valign': 'vcenter'})
})





#FULL 0
with open('EXCEL/notes.json') as f:
    data = json.load(f)
    worksheet.write_row(0, 0, titols) 
    worksheet.write_row(1, 1, percentatges)  
    row = 2
    linea_notes = 3
    for element in data:  
        col = 0
        for titol in titols:
            if titol in element:  
                worksheet.write(row, col, element[titol]) 
            col += 1

        worksheet.write_formula(row, 7, f'=IF(AND(F{linea_notes} > 4, G{linea_notes} < 20), "Valid", "No Valid")')
        worksheet.write_formula(row, 8, f'=IF(H{linea_notes} = "Valid", B{linea_notes}*10% + C{linea_notes}*10% + D{linea_notes}*10% + E{linea_notes}*20% + F{linea_notes}*50%, 1)')

        linea_notes += 1
        row += 1 
# FULL 1    
worksheet1.write_row(0, 0, titols_pag_2) 
worksheet1.write_row(1, 1, percentatges)  
row = 2
linees2 = 3
for element in data:  
    col_2 = 1  
    for titol in titols_pag_2:
        if titol == "id":  
            worksheet1.write_formula(row, 0, f'=MID("={element["id"]}",2,4)') 
        elif titol in element:  
            for columna in lista_columns:
                if col_2 < len(lista_columns) + 1:
                    worksheet1.write_formula(row, col_2, f"'Full 0'!{columna}{linees2}") 
                    col_2 += 1


    linees2 += 1
    row += 1

workbook.close()
print(f"Generated: '{filename}'")
