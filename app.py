import tkinter as tk
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtCore import Qt


app = QApplication(sys.argv)

ecran = QWidget()

layout = QGridLayout()
layout.setAlignment(Qt.AlignCenter)
layout.setSpacing(0)

ecran.setLayout(layout)
