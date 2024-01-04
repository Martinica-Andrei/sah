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
        super().__init__(self.lungime_piese,
                         self.inaltime_piese, cale_fisiere[index_fisier])
        self.tabla_de_sah = None  # trebuie setat
        self.joc_de_sah = None  # trebuie setat
        self.echipa = index_fisier  # index fisier coincide cu echipa
        self.rand_initial = None  
        self.coloana_initiala = None

    def pozitie(self):
        rand, coloana, _, _ = layout.getItemPosition(
            layout.indexOf(self.label))
        return (rand, coloana)

    def activeaza_click_event(self):
        self.label.mousePressEvent = lambda e: self.afisare_miscari_posibile()

    def dezactiveaza_click_event(self):
        self.label.mousePressEvent = lambda e: None

    def afisare_miscari_posibile(self):
        pass

    def coordonate_orizontala_verticala(self):
        rand, coloana = self.pozitie()
        coordonate = [[], [], [], []]
        # dreapta
        for c in range(coloana + 1, self.tabla_de_sah.coloane):
            coordonate[0].append((rand, c))
        # stanga
        for c in range(coloana - 1, -1, -1):
            coordonate[1].append((rand, c))
        # sus
        for r in range(rand - 1, -1, -1):
            coordonate[2].append((r, coloana))
        # jos
        for r in range(rand + 1, self.tabla_de_sah.randuri):
            coordonate[3].append((r, coloana))
        return coordonate

    def coordonate_diagonala(self):
        rand, coloana = self.pozitie()
        coordonate = [[], [], [], []]
        for i in range(1, self.tabla_de_sah.randuri + self.tabla_de_sah.coloane):
            index_coordonate = 0
            for j in [-1, 1]:
                for k in [-1, 1]:
                    r = rand + (j * i)
                    c = coloana + (k * i)
                    if self.tabla_de_sah.is_coordonate_valide(r, c):   
                        coordonate[index_coordonate].append((r,c))
                    index_coordonate += 1          
        return coordonate
