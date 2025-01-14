#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import json
import Estils as e
from reportlab.platypus import Paragraph
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth


idx_client = 0
image_path = 'PDF/firmafirma.png'
page_width, page_height = A4
def draw_paragraph(c, text, style, x, y, width):
    p = Paragraph(text, style)
    _, height = p.wrap(width, float('inf'))
    p.drawOn(c, x, y - height)
    return height

def draw_encabezado(c,client,y):
    c.setStrokeColor((0.22,0.5, 0.63))
    draw_paragraph(c, f"{client['companyia']}", e.styles["HeadingRight"], 50, y, 500)
    c.setLineWidth(3)
    c.line(50, page_height - 50, 550, page_height - 50)

def draw_peu(c, client, num_pag):
    c.setStrokeColor((0.22,0.5, 0.63))

    c.setLineWidth(1)  
    c.line(50, 50, 550, 50) 
    draw_paragraph(c, f"Factura {client['mes_factura']}", e.styles["piepagina"], 50, 65, 100)
    draw_paragraph(c, str(num_pag), e.styles["piepaginanum"], 50, 65, 500)

def dibuixarllegenda(c, x, y, color, text):
    c.setFillColor(color)
    c.rect(x, y, 15, 15, stroke=1, fill=1)
    draw_paragraph(c, text, e.styles["BodyLeft"], x + 25, y + 15, width=150)


def draw_bullet_list(c, items, style, x, y, width):
    for item in items:
        bullet_text = f"- {item}"
        p = Paragraph(bullet_text, style)
        _, height = p.wrap(width, float('inf'))
        p.drawOn(c, x, y - height)
        y -= (height + style.spaceBefore + style.spaceAfter)
    return y


rect_width = 200
rect_height = 90
margin_x = 50
margin_y = 430


with open("PDF/clients.json", encoding="utf-8") as f:
    data = json.load(f)
    num = 0
    for idx_client in range(5):
        client = data['clients'][idx_client]
        filename = f"PDF/Factura{num}.pdf"
        num+=1
        c = canvas.Canvas(filename, pagesize=A4)
        current_y = page_height - 50
        margin = 50
        width = page_width - (2 * margin)
        draw_peu(c,client,1)
        draw_encabezado(c,client,current_y)

        texts = [
            (f"Estimad@ {client['nom']}, {client['cognom']}", "BodyLeft"),
            (f"Ens dirigim a vostè per presentar-li el detall de la seva factura corresponent al mes de {client['mes_factura']}: ", "BodyLeft"),
            ("Detall dels Cobraments", "BodyLeft"),
        ]



        list_items = [
            f"Quota bàsica mensual: {client['detall_cobraments']['quota_basica']}",
            "Serveis adicionals: "
        ]

        serveis_addicionals = client['detall_cobraments']['serveis_addicionals']
        for servei in serveis_addicionals:
            list_items.append(f"{servei['nom']} : {servei['preu']}")

        list_items += [
            f"Impostos aplicats: {client['detall_cobraments']['impostos']}",
        ]

        draw_paragraph(c,f"Total a pagar: <b>{client['detall_cobraments']['total']}€</b>",e.styles["BodyLeft"],80,510,490)

        c.drawImage(image_path, 50, 325, 175, 75, None, True)

        draw_paragraph(
            c,"Recordi que pot consultar els detalls de les seves factures i gestionar els seus pagaments "
            f"a través de l'àrea de clients al nostre lloc web o contactar amb el nostre servei d'atenció al client al {client['telefon']}",e.styles["BodyLeft"],margin,480,width)

        draw_paragraph(
            c,"Gràcies per confiar en nosaltres",e.styles["BodyLeft"],margin,430, width)

        link_txt = "Departament d'Atenció al Client "
        link_x = 300
        link_y = 350
        link_url = "https://www.iesesteveterradas.cat"
        link_height = draw_paragraph(c, "<u>" + link_txt + "</u>", e.styles["link_style"], link_x, link_y, width)

        text = f"""
        Atentament, <br/><br/>
        {client['companyia']}<br/><br/>
        """
        
        link_width = stringWidth(link_txt, e.styles["link_style"].fontName, e.styles["link_style"].fontSize)
        link_rect = (
            link_x,                    # x1
            link_y - link_height,      # y1
            link_x + link_width,       # x2
            link_y                     # y2
        )
        c.linkURL(link_url, link_rect, relative=0)

        draw_paragraph(c, text, e.styles["BodyLeft"], 300, 400, width)

        text_height = draw_paragraph(c, text, e.styles["BodyLeft"], 100 + width + 10, 200 + 100, width)

        for text, style_name in texts:
            height = draw_paragraph(c, text, e.styles[style_name], margin, current_y - 60, width)
            current_y -= (height + e.styles[style_name].spaceBefore + e.styles[style_name].spaceAfter)

        current_y = draw_bullet_list(c, list_items, e.styles["ListStyle"], margin, current_y - 60, width)

        c.showPage()
        current_y = page_height - 50
        draw_encabezado(c,client,current_y)
        draw_peu(c,client,2)
        current_y -= 20
        draw_paragraph(c, f"Calendari", e.styles["HeadingLeft"], 50, current_y - 40, 500)
        draw_paragraph(c,f"Li recordem el calendari de pagaments anual segons el seu pla contractat:",e.styles["BodyLeft"],50,current_y - 60,500)



        draw_paragraph(c,f"Factura {client['mes_factura']}",e.styles["piepagina"],50,65,100)

        x = 100
        y = 600
        mesos = []
        tipus = []

        calendari_pagaments = client["calendari_pagaments"]

        for i in calendari_pagaments.keys():
            mesos.append(i)

        for j in calendari_pagaments.values():
            tipus.append(j)

        idx = 0
        for fila in range(3):  
            for columna in range(4):  
                actual = tipus[idx]  
                mes = mesos[idx]  
                c.setLineWidth(1)
                if actual.startswith("Bon"):
                    c.setFillColorRGB(0.5, 0.7, 1.0) 
                elif actual == "Regular":
                    c.setFillColorRGB(1.0, 1.0, 1.0)  
                elif actual == "Exempt":
                    c.setFillColorRGB(0.0, 1.0, 0.0)  

                c.setStrokeColorRGB(0.0, 0.0, 0.0) 

                c.rect(x, y, 100, 50, stroke=1, fill=1)

                draw_paragraph(c, mes, e.styles["BodyCenter"], x, y + 25, width=100)
                idx += 1
                x += 100  

            x = 100 
            y -= 50  


        dibuixarllegenda(c, x, y + 20, (0.0, 1.0, 0.0), "Exempt de pagament")
        dibuixarllegenda(c, x, y, (0.5, 0.7, 1.0), "Bonificacio del X%")

        dibuixarllegenda(c, x, y - 20, (1.0, 1.0, 1.0), "Pagament regular")



        c.save() 
