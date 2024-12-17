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


#ESTILS FULLS

def estils_condicionals(full):
    full.conditional_format("B3:F34", { 
        'type': 'cell',
        'criteria': '<',
        'value': 5,
        'format': workbook.add_format({'bg_color': '#FF0000', 'font_color': '#000000', 'align': 'center', 'valign': 'vcenter'})
    })
    full.conditional_format("I3:I34", { 
        'type': 'cell',
        'criteria': '<',
        'value': 5,
        'format': workbook.add_format({'bg_color': '#FF0000', 'font_color': '#000000', 'align': 'center', 'valign': 'vcenter'})
    })
    full.conditional_format("I3:I34", { 
        'type': 'cell',
        'criteria': '>=',
        'value': 7,
        'format': workbook.add_format({'bg_color': '#00ff00', 'font_color': '#000000', 'align': 'center', 'valign': 'vcenter'})
    })

estils_condicionals(worksheet)
estils_condicionals(worksheet1)



#FULL 0
with open('EXCEL/notes.json') as f:
    data = json.load(f)
    worksheet.write_row(0, 0, titols) 
    worksheet.write_row(1, 1, percentatges)  
    fila = 2
    fila_notes = 3
    for element in data:  
        col = 0
        for titol in titols:
            if titol in element:  
                worksheet.write(fila, col, element[titol]) 
            col += 1

        worksheet.write_formula(fila, 7, f'=IF(AND(F{fila_notes} > 4, G{fila_notes} < 20), "Valid", "No Valid")')
        worksheet.write_formula(fila, 8, f'=IF(H{fila_notes} = "Valid", SUMPRODUCT(B{fila_notes}:F{fila_notes}, B2:F2), 1)')

        fila_notes += 1
        fila += 1 
# FULL 1    
worksheet1.write_row(0, 0, titols_pag_2) 
worksheet1.write_row(1, 1, percentatges)  
fila = 2
files2 = 3
for element in data:  
    col_2 = 1  
    for titol in titols_pag_2:
        if titol == "id":  
            worksheet1.write_formula(fila, 0, f'=MID("={element["id"]}",4,4)') 
        elif titol in element:  
            for columna in lista_columns:
                if col_2 < len(lista_columns) + 1:
                    worksheet1.write_formula(fila, col_2, f"'Full 0'!{columna}{files2}") 
                    col_2 += 1


    files2 += 1
    fila += 1

workbook.close()
print(f"Generated: '{filename}'")
