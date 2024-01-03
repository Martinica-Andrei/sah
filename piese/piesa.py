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
        self.rand_initial = None  # pentru pion, determina daca e prima miscare

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
        #dreapta sus
        i = 1
        while True:
            r = rand - i
            c = coloana + i
            if self.tabla_de_sah.is_coordonate_valide(r, c) == False:
                break
            coordonate[0].append((r,c))
            i += 1
        #stanga sus
        i = 1
        while True:
            r = rand - i
            c = coloana - i
            if self.tabla_de_sah.is_coordonate_valide(r, c) == False:
                break
            coordonate[1].append((r,c))
            i += 1
        #dreapta jos
        i = 1
        while True:
            r = rand + i
            c = coloana + i
            if self.tabla_de_sah.is_coordonate_valide(r, c) == False:
                break
            coordonate[2].append((r,c))
            i += 1
        #stanga jos
        i = 1
        while True:
            r = rand + i
            c = coloana - i
            if self.tabla_de_sah.is_coordonate_valide(r, c) == False:
                break
            coordonate[3].append((r,c))
            i += 1
        return coordonate
