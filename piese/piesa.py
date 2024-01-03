from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from patratica import Patratica
from app import layout

class Piesa(Patratica):
    lungime_piese = 40
    inaltime_piese = 40
    alb = 0
    negru = 1

    def __init__(self, cale_fisiere, index_fisier):
        super().__init__(self.lungime_piese, self.inaltime_piese, cale_fisiere[index_fisier])
        self.tabla_de_sah = None # trebuie setat
        self.joc_de_sah = None # trebuie setat
        self.echipa = index_fisier # index fisier coincide cu echipa

    def pozitie(self):
        rand, coloana, _, _ = layout.getItemPosition(layout.indexOf(self.label))
        return (rand, coloana)
    
    def activeaza_click_event(self):
        self.label.mousePressEvent = lambda e : self.afisare_miscari_posibile()

    def dezactiveaza_click_event(self):
        self.label.mousePressEvent = lambda e : None

    def afisare_miscari_posibile(self):
        pass