#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
import json
import Estils as e  # Asegúrate de tener este archivo correctamente implementado

# Configuración
filename = 'PDF/Exercici0.pdf'
json_path = "PDF/clients.json"

def draw_paragraph(c, text, style, x, y, width):
    """Dibuja un párrafo en el lienzo y devuelve la altura ocupada."""
    p = Paragraph(text, style)
    _, height = p.wrap(width, float('inf'))
    p.drawOn(c, x, y - height)
    return height

def draw_separator(c, x, y, width):
    """Dibuja una línea horizontal como separador."""
    c.setStrokeColor(colors.HexColor("#187BCD"))
    c.line(x, y, x + width, y)

# Crear el lienzo del PDF
c = canvas.Canvas(filename, pagesize=A4)
page_width, page_height = A4
current_y = page_height - 50
margin = 50
width = page_width - (2 * margin)

# Dibujar encabezado
c.setFillColor(colors.HexColor("#187BCD"))
c.rect(margin, page_height - 50, width, 3, stroke=0, fill=1)

try:
    with open(json_path) as f:
        data = json.load(f)
        client = data["clients"][0]

        # Encabezado del cliente
        texts = [
            (f"{client['companyia']}", "HeadingRight"),
            (f"Estimad@ {client['nom']} {client['cognom']}", "BodyLeft"),
            (f"Mes de factura: {client['mes_factura']}", "BodyLeft"),
            ("Detall dels Cobraments:", "HeadingLeft"),
        ]

        # Dibujar textos iniciales
        for text, style_name in texts:
            height = draw_paragraph(c, text, e.styles[style_name], margin, current_y, width)
            current_y -= (height + e.styles[style_name].spaceBefore + e.styles[style_name].spaceAfter)

        # Dibujar detalles de los cobros
        list_items = [
            f"Quota bàsica mensual: {client['detall_cobraments']['quota_basica']} €",
            "Serveis adicionals:",
        ]

        for servei in client['detall_cobraments']['serveis_addicionals']:
            list_items.append(f"  - {servei['nom']}: {servei['preu']} €")

        list_items += [
            f"Impostos aplicats: {client['detall_cobraments']['impostos']} €",
            f"Total a pagar: {client['detall_cobraments']['total']} €",
        ]

        for item in list_items:
            height = draw_paragraph(c, item, e.styles["BodyLeft"], margin, current_y, width)
            current_y -= (height + e.styles["BodyLeft"].spaceBefore + e.styles["BodyLeft"].spaceAfter)

        # Separador
        current_y -= 10
        draw_separator(c, margin, current_y, width)
        current_y -= 20

        # Calendario de pagos
        height = draw_paragraph(c, "Calendari de Pagaments:", e.styles["HeadingLeft"], margin, current_y, width)
        current_y -= (height + e.styles["HeadingLeft"].spaceBefore + e.styles["HeadingLeft"].spaceAfter)

        for mes, estat in client["calendari_pagaments"].items():
            item_text = f"{mes}: {estat}"
            height = draw_paragraph(c, item_text, e.styles["BodyLeft"], margin, current_y, width)
            current_y -= (height + e.styles["BodyLeft"].spaceBefore + e.styles["BodyLeft"].spaceAfter)

except (FileNotFoundError, KeyError, json.JSONDecodeError) as ex:
    print(f"Error al procesar el archivo JSON: {ex}")

# Guardar el PDF
c.save()
