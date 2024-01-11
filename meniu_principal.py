from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QApplication, QLabel, QSizePolicy
from app import meniu_principal, main_layout
from joc_de_sah import JocDeSah
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

joc = JocDeSah()

meniu_principal_layout = QVBoxLayout(meniu_principal)


def btn_joc_nou_click():
    global joc
    joc.destructor()
    joc = JocDeSah()
    main_layout.setCurrentWidget(joc.widget_pagina)


def btn_continua_joc_click():
    main_layout.setCurrentWidget(joc.widget_pagina)


font_titlu = QFont()
font_titlu.setPointSize(50)

font_btn = QFont()
font_btn.setPointSize(25)

titlu = QLabel("Sah")
titlu.setMaximumHeight(50)
titlu.setFont(font_titlu)
titlu.setAlignment(Qt.AlignCenter)


btn_joc_nou = QPushButton('Joc nou')
btn_joc_nou.setFont(font_btn)

btn_continua_joc = QPushButton("Continua Joc")
btn_continua_joc.setFont(font_btn)

btn_exit = QPushButton("Iesire")
btn_exit.setFont(font_btn)

btn_joc_nou.clicked.connect(btn_joc_nou_click)

btn_continua_joc.clicked.connect(btn_continua_joc_click)

btn_exit.clicked.connect(QApplication.instance().quit)

meniu_principal_layout.addWidget(titlu)

meniu_principal_layout.addWidget(btn_joc_nou)

meniu_principal_layout.addWidget(btn_continua_joc)

meniu_principal_layout.addWidget(btn_exit)
