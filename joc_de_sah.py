from tabla_de_sah import TablaDeSah
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget
from app import ecran, main_layout
from piese.miscari.capturare import Capturare
from piese.rege import Rege
from PyQt5.QtGui import QFont


class JocDeSah:
    def __init__(self):
        self.tabla_de_sah = TablaDeSah(self)
        self.interfata()
        self.jucatori = ["Alb", "Negru"]
        self.index_jucator_curent = -1
        self.miscari_posibile = []
        self.miscari_facute = []
        ecran.keyPressEvent = self.key_press_event
        self.setare_urmatorul_jucator()

    def stergere_miscari_posibile(self):
        for miscare in self.miscari_posibile:
            miscare.grafica.label.setParent(None)
        self.miscari_posibile = []

    def adaugare_miscari_posibile(self, miscari_posibile):
        for miscare in miscari_posibile:
            miscare.init_grafica()
            miscare.grafica.label.mousePressEvent = lambda e, miscare=miscare: self.miscare_click_event(
                e, miscare)
            self.tabla_de_sah.layout.addWidget(
                miscare.grafica.label, miscare.piesa_rand_tinta, miscare.piesa_coloana_tinta)
            miscare.terminare_miscare = self.terminare_miscare
            self.miscari_posibile.append(miscare)

    def actualizare_miscari_posibile(self, miscari_posibile):
        self.stergere_miscari_posibile()
        self.adaugare_miscari_posibile(miscari_posibile)

    def setare_index_jucator_curent(self, valoare):
        if valoare < 0:
            valoare = len(self.jucatori) - 1
        elif valoare >= len(self.jucatori):
            valoare = 0
        self.index_jucator_curent = valoare
        self.adaugare_eventuri(self.index_jucator_curent)
        self.afisare_stare_joc()
        self.tabla_de_sah.updatare_grafica()
        self.label_jucator_curent.setText(
            self.jucatori[self.index_jucator_curent])

    def setare_urmatorul_jucator(self):
        self.setare_index_jucator_curent(self.index_jucator_curent + 1)

    def setare_jucator_anterior(self):
        self.setare_index_jucator_curent(self.index_jucator_curent - 1)

    def terminare_miscare(self, miscare):
        self.stergere_miscari_posibile()
        self.setare_urmatorul_jucator()
        self.miscari_facute.append(miscare)

    def adaugare_eventuri(self, echipa):
        for i in range(self.tabla_de_sah.randuri):
            for j in range(self.tabla_de_sah.coloane):
                piesa = self.tabla_de_sah.piese[i][j]
                patratica = self.tabla_de_sah.patratele_background[i][j]
                if piesa is None:
                    patratica.label.mousePressEvent = self.patratica_click_event
                    continue
                # nu trebuie setat mousePressEvent la patratica pentru ca e acoperit complet de
                # piesa
                if piesa.echipa == echipa:
                    piesa.label.mousePressEvent = lambda e, piesa=piesa: self.piesa_click_event(
                        e, piesa)
                else:
                    piesa.label.mousePressEvent = self.patratica_click_event

    def patratica_click_event(self, e):
        mouse_butoane = e.buttons()
        if mouse_butoane & (Qt.LeftButton | Qt.RightButton):
            self.stergere_miscari_posibile()

    def piesa_click_event(self, e, piesa):
        mouse_butoane = e.buttons()
        if mouse_butoane & Qt.LeftButton:
            miscari_piesa = piesa.miscari_posibile()
            miscari_piesa = self.piesa_miscari_legale(miscari_piesa)
            self.actualizare_miscari_posibile(miscari_piesa)
        elif mouse_butoane & Qt.RightButton:
            self.stergere_miscari_posibile()

    def miscare_click_event(self, e, miscare):
        mouse_butoane = e.buttons()
        if mouse_butoane & Qt.LeftButton:
            miscare.executa()
        elif mouse_butoane & Qt.RightButton:
            self.stergere_miscari_posibile()

    # adauga doar miscari care nu il pun pe regele jucatorului curent in check
    def piesa_miscari_legale(self, miscari_piesa):
        miscari_legale = []
        for miscare in miscari_piesa:
            miscare.executa()
            if self.este_check() == False:
                miscari_legale.append(miscare)
            miscare.anuleaza()
        return miscari_legale

    def anulare_ultima_miscare(self):
        if len(self.miscari_facute):
            ultima_miscare = self.miscari_facute.pop()
            ultima_miscare.anuleaza()
            self.setare_jucator_anterior()
            self.stergere_miscari_posibile()

    def key_press_event(self, event):
        if event.key() == Qt.Key_Z:
            self.anulare_ultima_miscare()

    def miscari_jucator(self, index_jucator):
        piese = self.tabla_de_sah.piese_echipa(index_jucator)
        for piesa in piese:
            yield piesa.miscari_posibile()

    # este_check pentru jucator curent
    def este_check(self):
        for miscari in self.miscari_jucator(not self.index_jucator_curent):
            for miscare in miscari:
                if type(miscare) == Capturare and type(miscare.piesa_tinta) == Rege:
                    return True
        return False

    def este_checkmate(self):
        if self.este_check() == False:
            return False
        for miscari in self.miscari_jucator(self.index_jucator_curent):
            miscari_legale = self.piesa_miscari_legale(miscari)
            if len(miscari_legale) > 0:
                return False
        return True

    def este_stalemate(self):
        if self.este_check():
            return False
        for miscari in self.miscari_jucator(self.index_jucator_curent):
            miscari_legale = self.piesa_miscari_legale(miscari)
            if len(miscari_legale) > 0:
                return False
        return True

    def afisare_stare_joc(self):
        if self.este_stalemate():
            self.label_stare_joc.setText("Stalemate")
            self.label_stare_joc.show()
        elif self.este_checkmate():
            self.label_stare_joc.setText("Checkmate")
            self.label_stare_joc.show()
        elif self.este_check():
            self.label_stare_joc.setText("Check")
            self.label_stare_joc.show()
        else:
            self.label_stare_joc.hide()

    def interfata(self):
        self.widget_pagina = QWidget()
        self.layout = QGridLayout(self.widget_pagina)
        self.top_layout = QGridLayout()
        self.bottom_layout = QGridLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.top_layout, 0, 0)
        self.layout.addLayout(self.tabla_de_sah.layout, 1, 0)
        self.layout.addLayout(self.bottom_layout, 2, 0)

        self.font = QFont()
        self.font.setPointSize(20)

        self.label_jucator_curent = QLabel()
        self.label_jucator_curent.setFont(self.font)

        self.label_stare_joc = QLabel()
        self.label_stare_joc.setFont(self.font)
        self.label_stare_joc.hide()

        self.top_layout.addWidget(self.label_jucator_curent, 0, 0)
        self.top_layout.addWidget(self.label_stare_joc, 0, 1)

        self.label_jucator_curent.setAlignment(Qt.AlignCenter)
        self.label_stare_joc.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(self.widget_pagina)
