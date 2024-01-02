from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class Patratica:
    def __init__(self, lungime, inaltime, cale_fisier):
        self.pixmap = QPixmap(cale_fisier).scaled(lungime, inaltime)
        self.label = QLabel()
        self.label.setPixmap(self.pixmap)