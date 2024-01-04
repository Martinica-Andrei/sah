from tabla_de_sah import TablaDeSah
from app import layout
from PyQt5.QtCore import Qt
from app import ecran
from piese.miscari.capturare import Capturare
from piese.rege import Rege


class JocDeSah:
    def __init__(self):
        self.tabla_de_sah = TablaDeSah(self)
        self.jucatori = ["alb", "negru"]
        self.index_jucator_curent = 0
        self.miscari_posibile = []
        self.miscari_facute = []
        ecran.keyPressEvent = self.key_press_event
        self.adaugare_eventuri(self.index_jucator_curent)

    def stergere_miscari_posibile(self):
        for miscare in self.miscari_posibile:
            miscare.grafica.label.setParent(None)
        self.miscari_posibile = []

    def adaugare_miscari_posibile(self, miscari_posibile):
        for miscare in miscari_posibile:
            miscare.init_grafica()
            miscare.grafica.label.mousePressEvent = lambda e, miscare=miscare: self.miscare_click_event(
                e, miscare)
            layout.addWidget(
                miscare.grafica.label, miscare.piesa_rand_tinta, miscare.piesa_coloana_tinta)
            miscare.terminare_miscare = self.terminare_miscare
            self.miscari_posibile.append(miscare)

    def actualizare_miscari_posibile(self, miscari_posibile):
        self.stergere_miscari_posibile()
        self.adaugare_miscari_posibile(miscari_posibile)

    def setare_urmatorul_jucator(self):
        self.index_jucator_curent += 1
        if self.index_jucator_curent >= len(self.jucatori):
            self.index_jucator_curent = 0
        self.adaugare_eventuri(self.index_jucator_curent)

    def setare_jucator_anterior(self):
        self.index_jucator_curent -= 1
        if self.index_jucator_curent < 0:
            self.index_jucator_curent = len(self.jucatori) - 1
        self.adaugare_eventuri(self.index_jucator_curent)

    def terminare_miscare(self, miscare):
        self.stergere_miscari_posibile()
        self.setare_urmatorul_jucator()
        self.miscari_facute.append(miscare)
        self.verificare_joc_sfarsit()

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
        miscari_check = []
        for miscare in miscari_piesa:
            miscare.executa()
            if self.este_check() == False:
                miscari_check.append(miscare)
            miscare.anuleaza()
        return miscari_check

    def anulare_ultima_miscare(self):
        if len(self.miscari_facute):
            ultima_miscare = self.miscari_facute.pop()
            ultima_miscare.anuleaza()
            self.setare_jucator_anterior()
            self.stergere_miscari_posibile()
            self.verificare_joc_sfarsit()

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
                if type(miscare) == Capturare and type(miscare.piesa_tinta) == Rege and miscare.piesa_tinta.echipa != miscare.piesa.echipa:
                    return True
        return False

    def este_checkmate(self):
        for miscari in self.miscari_jucator(self.index_jucator_curent):
            for miscare in miscari:
                miscare.executa()
                if self.este_check() == False:
                    miscare.anuleaza()
                    return False
                miscare.anuleaza()
        return True

    def verificare_joc_sfarsit(self):
        if self.este_check():
            if self.este_checkmate():
                print("checkmate")
            else:
                print('check')
