#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

custom_colors = {
    'primary': colors.HexColor('#1B4F72'),
    'secondary': colors.HexColor('#2E86C1'),
    'accent1': colors.HexColor('#E74C3C'),
    'accent2': colors.HexColor('#187bcd'),
    'neutral': colors.HexColor('#566573'),
}

styles = {
    "MainTitle": ParagraphStyle(
        name="MainTitle",
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=30,
        textColor=custom_colors['primary'],
        alignment=TA_CENTER,
        spaceAfter=20,
    ),
    "Subtitle": ParagraphStyle(
        name="Subtitle",
        fontName="Helvetica-Oblique",
        fontSize=18,
        leading=22,
        textColor=custom_colors['secondary'],
        alignment=TA_CENTER,
        spaceAfter=15,
    ),
    "HeadingLeft": ParagraphStyle(
        name="HeadingLeft",
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=custom_colors['accent1'],
        alignment=TA_LEFT,
        spaceBefore=10,
        spaceAfter=8,
    ),
    "HeadingRight": ParagraphStyle(
        name="HeadingRight",
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=custom_colors['accent2'],
        alignment=TA_RIGHT,
        spaceBefore=20,
        spaceAfter=15,
    ),
    "BodyJustified": ParagraphStyle(
        name="BodyJustified",
        fontName="Helvetica",
        fontSize=12,
        leading=15,
        textColor=custom_colors['neutral'],
        alignment=TA_JUSTIFY,
        spaceBefore=6,
        spaceAfter=6,
        firstLineIndent=20,
    ),
    "BodyCenter": ParagraphStyle(
        name="BodyCenter",
        fontName="Helvetica",
        fontSize=12,
        leading=15,
        textColor=colors.black,
        alignment=TA_CENTER,
        spaceBefore=6,
        spaceAfter=6,
    ),
    "BodyLeft": ParagraphStyle(
        name="BodyLeft",
        fontName="Helvetica",
        fontSize=15,
        leading=15,
        textColor=custom_colors['neutral'],
        alignment=TA_LEFT,
        spaceBefore=12,
        spaceAfter=12,
        firstLineIndent=0,
    ),
    "BodyRight": ParagraphStyle(
        name="BodyRight",
        fontName="Helvetica",
        fontSize=15,
        leading=15,
        textColor=custom_colors['accent2'],
        alignment=TA_RIGHT,
        spaceBefore=6,
        spaceAfter=6,
        firstLineIndent=0,
    ),


    "Quote": ParagraphStyle(
        name="Quote",
        fontName="Helvetica-Oblique",
        fontSize=14,
        leading=18,
        textColor=custom_colors['secondary'],
        alignment=TA_CENTER,
        leftIndent=50,
        rightIndent=50,
        spaceBefore=15,
        spaceAfter=15,
    ),
    "Highlight": ParagraphStyle(
        name="Highlight",
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=colors.white,
        alignment=TA_CENTER,
        backColor=custom_colors['accent1'],
        borderPadding=10,
        spaceBefore=10,
        spaceAfter=10,
    ),
    "Strikethrough": ParagraphStyle(
        name="Strikethrough",
        fontName="Helvetica",
        fontSize=14,
        leading=18,
        textColor=custom_colors['neutral'],
        alignment=TA_LEFT,
        spaceBefore=8,
        spaceAfter=8,
    ),
    "ListStyle": ParagraphStyle(
        name="ListStyle",
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=custom_colors['neutral'],
        alignment=TA_LEFT,
        spaceBefore=6,
        spaceAfter=6,
        leftIndent=30,  # Espai per als bullets
        bulletIndent=15,  # Posició dels bullets
    ) }

