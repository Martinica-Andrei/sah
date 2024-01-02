from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Piesa:
    lungime_piese = 40
    inaltime_piese = 40

    def __init__(self, cale_fisiere, index_fisier):
        self.pixmap = QPixmap(cale_fisiere[index_fisier]).scaled(self.lungime_piese, self.inaltime_piese)
        self.label = QLabel()
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignCenter)