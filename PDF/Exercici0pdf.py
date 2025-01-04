#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import json
import Estils as e
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
filename = 'PDF/Exercici0.pdf'
def draw_paragraph(c, text, style, x, y, width):
    p = Paragraph(text, style)
    _, height = p.wrap(width, float('inf'))
    p.drawOn(c, x, y - height)
    return height
def draw_bullet_list(c, items, style, x, y, width):
    for item in items:
        bullet_text = f"- {item}"
        p = Paragraph(bullet_text, style)
        _, height = p.wrap(width, float('inf'))
        p.drawOn(c, x, y - height)
        y -= (height + style.spaceBefore + style.spaceAfter)
    return y

custom_colors = {
    'primary': colors.HexColor('#1B4F72'),
    'secondary': colors.HexColor('#2E86C1'),
    'accent1': colors.HexColor('#E74C3C'),
    'accent2': colors.HexColor('#187bcd'),
    'neutral': colors.HexColor('#566573'),
}


# Crear el lienzo del PDF
c = canvas.Canvas(filename, pagesize=A4)
page_width, page_height = A4
current_y = page_height - 50
margin = 50
width = page_width - (2 * margin)
c.setFillColorRGB(24 / 255, 123 / 255, 205 / 255)  
c.rect(50, page_height - 50, 500, 3, stroke=0, fill=1)
with open("PDF/clients.json") as f:
    data = json.load(f)
    texts = [
    (f"{data['clients'][0]['companyia']}", "HeadingRight"),
    (f"Estimad@ {data['clients'][0]['nom']}, {data['clients'][0]['cognom']}", "BodyLeft"),
    (f"Ens dirigim a vostè per presentar-li el detall de la seva factura corresponent al mes de {data['clients'][0]['mes_factura']}: ", "BodyLeft"),
    ("Detall dels Cobraments", "BodyLeft"),

]
list_items = [
    f"Quota bàsica mensual: {data['clients'][0]['detall_cobraments']['quota_basica']}",
    "Serveis adicionals: "
]

# Añadir los servicios adicionales
serveis_addicionals = data['clients'][0]['detall_cobraments']['serveis_addicionals']
for servei in serveis_addicionals:
    list_items.append(f"{servei['nom']} : {servei['preu']}")

list_items += [
    f"Impostos aplicats: {data['clients'][0]['detall_cobraments']['impostos']}",

]
lista_serveis = []
for servei in serveis_addicionals:
    lista_serveis.append(f"{servei['nom']}: {servei['preu']}")

draw_paragraph(c,f"Total a pagar: {data['clients'][0]['detall_cobraments']['total']}€",e.styles["BodyLeft"],80,510,490)


draw_paragraph(
    c,
    "Recordi que pot consultar els detalls de les seves factures i gestionar els seus pagaments "
    f"a través de l'àrea de clients al nostre lloc web o contactar amb el nostre servei d'atenció al client al {data['clients'][0]['telefon']}",
    e.styles["BodyLeft"], 
    margin,              
    480,        
    width                
)

for text, style_name in texts:
    height = draw_paragraph(c, text, e.styles[style_name], margin, current_y, width)
    current_y -= (height + e.styles[style_name].spaceBefore + e.styles[style_name].spaceAfter)
current_y = draw_bullet_list(c, list_items, e.styles["ListStyle"], margin, current_y, width)
c.save()
