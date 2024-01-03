from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Patratica:
    def __init__(self, lungime, inaltime, cale_fisier):
        self.pixmap = QPixmap(cale_fisier).scaled(lungime, inaltime)
        self.label = QLabel()
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignCenter)