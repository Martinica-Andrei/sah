from tabla_de_sah import TablaDeSah
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget
from app import ecran, main_layout
from piese.miscari.capturare import Capturare
from piese.rege import Rege
from PyQt5.QtGui import QFont
from functools import wraps


class JocDeSah:
    def __init__(self):
        self.tabla_de_sah = TablaDeSah(self)
        self.interfata()
        self.jucatori = ["Alb", "Negru"]
        self.index_jucator_curent = -1
        self.miscari_posibile = []
        self.miscari_facute = []
        self.se_executa_event = False
        ecran.keyPressEvent = self.key_press_event
        self.este_check_jucator_curent = False
        self.este_checkmate_jucator_curent = False
        self.este_stalemate_jucator_curent = False
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
        self.tabla_de_sah.updatare_grafica()
        self.stare_joc()
        self.label_jucator_curent.setText(
            self.jucatori[self.index_jucator_curent])

    def setare_urmatorul_jucator(self):
        self.setare_index_jucator_curent(self.index_jucator_curent + 1)

    def setare_jucator_anterior(self):
        self.setare_index_jucator_curent(self.index_jucator_curent - 1)

    def terminare_miscare(self):
        self.stergere_miscari_posibile()
        self.setare_urmatorul_jucator()

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

    # blocheaza executarea altor evenimente atata timp cat se executa codul din func
    def eveniment_unic(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.se_executa_event == False:
                self.se_executa_event = True
                val_functie = func(self, *args, **kwargs)
                self.se_executa_event = False
                return val_functie
        return wrapper

    @eveniment_unic
    def patratica_click_event(self, e):
        mouse_butoane = e.buttons()
        if mouse_butoane & (Qt.LeftButton | Qt.RightButton):
            self.stergere_miscari_posibile()

    @eveniment_unic
    def piesa_click_event(self, e, piesa):
        mouse_butoane = e.buttons()
        if mouse_butoane & Qt.LeftButton:
            miscari_piesa = piesa.miscari_posibile()
            miscari_piesa = self.piesa_miscari_legale(miscari_piesa)
            self.actualizare_miscari_posibile(miscari_piesa)
        elif mouse_butoane & Qt.RightButton:
            self.stergere_miscari_posibile()

    @eveniment_unic
    def miscare_click_event(self, e, miscare):
        mouse_butoane = e.buttons()
        if mouse_butoane & Qt.LeftButton:
            miscare.executa()
        elif mouse_butoane & Qt.RightButton:
            self.stergere_miscari_posibile()

    @eveniment_unic
    def key_press_event(self, event):
        if event.key() == Qt.Key_Z:
            self.anulare_ultima_miscare()

    # adauga doar miscari care nu il pun pe regele jucatorului curent in check
    def piesa_miscari_legale(self, miscari_piesa):
        miscari_legale = []
        for miscare in miscari_piesa:
            miscare.executa()
            if self._este_check_jucator_curent() == False:
                miscari_legale.append(miscare)
            miscare.anuleaza()
        return miscari_legale

    def anulare_ultima_miscare(self):
        if len(self.miscari_facute):
            self.miscari_facute[-1].anuleaza()
            self.stergere_miscari_posibile()
            self.setare_jucator_anterior()

    def miscari_jucator(self, index_jucator):
        piese = self.tabla_de_sah.piese_echipa(index_jucator)
        for piesa in piese:
            yield piesa.miscari_posibile()

    # este_check pentru jucator curent
    def _este_check_jucator_curent(self):
        for miscari in self.miscari_jucator(not self.index_jucator_curent):
            for miscare in miscari:
                if type(miscare) == Capturare and type(miscare.piesa_tinta) == Rege:
                    return True
        return False

    def _este_checkmate_jucator_curent(self):
        if self._este_check_jucator_curent() == False:
            return False
        for miscari in self.miscari_jucator(self.index_jucator_curent):
            miscari_legale = self.piesa_miscari_legale(miscari)
            if len(miscari_legale) > 0:
                return False
        return True

    def _este_stalemate_jucator_curent(self):
        if self._este_check_jucator_curent():
            return False
        for miscari in self.miscari_jucator(self.index_jucator_curent):
            miscari_legale = self.piesa_miscari_legale(miscari)
            if len(miscari_legale) > 0:
                return False
        return True

    def stare_joc(self):
        if len(self.miscari_facute) == 3:
            pass
        self.este_check_jucator_curent = False
        self.este_checkmate_jucator_curent = False
        self.este_stalemate_jucator_curent = False
        if self._este_stalemate_jucator_curent():
            self.este_stalemate_jucator_curent = True
            self.label_stare_joc.setText("Stalemate")
            self.label_stare_joc.show()
        elif self._este_checkmate_jucator_curent():
            self.este_checkmate_jucator_curent = True
            self.label_stare_joc.setText("Checkmate")
            self.label_stare_joc.show()
        elif self._este_check_jucator_curent():
            self.este_check_jucator_curent = True
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
