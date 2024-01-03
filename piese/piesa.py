from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from app import layout

class Piesa:
    lungime_piese = 40
    inaltime_piese = 40
    alb = 0
    negru = 1

    def __init__(self, cale_fisiere, index_fisier):
        self.pixmap = QPixmap(cale_fisiere[index_fisier]).scaled(
            self.lungime_piese, self.inaltime_piese)
        self.label = QLabel()
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignCenter)
        self.tabla_de_sah = None # trebuie setat
        self.joc_de_sah = None # trebuie setat
        self.echipa = index_fisier # index fisier coincide cu echipa

    def pozitie(self):
        rand, coloana, _, _ = layout.getItemPosition(layout.indexOf(self.label))
        return (rand, coloana)
    
    def afisare_miscari_posibile(self, event):
        pass