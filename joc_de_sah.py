from tabla_de_sah import TablaDeSah
from app import layout
from PyQt5.QtCore import Qt
from app import ecran


class JocDeSah:
    def __init__(self):
        self.tabla_de_sah = TablaDeSah(self)
        self.jucatori = ["alb", "negru"]
        self.index_jucator_curent = 0
        self.miscari_posibile = []
        self.miscari_facute = []
        self.adaugare_eventuri(self.index_jucator_curent)
        ecran.keyPressEvent = self.key_press_event

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
            piesa_miscari = piesa.miscari_posibile()
            self.actualizare_miscari_posibile(piesa_miscari)
        elif mouse_butoane & Qt.RightButton:
            self.stergere_miscari_posibile()

    def miscare_click_event(self, e, miscare):
        mouse_butoane = e.buttons()
        if mouse_butoane & Qt.LeftButton:
            miscare.executa()
        elif mouse_butoane & Qt.RightButton:
            self.stergere_miscari_posibile()

    def anulare_ultima_miscare(self):
        if len(self.miscari_facute):
            ultima_miscare = self.miscari_facute.pop()
            ultima_miscare.anuleaza()
            self.setare_jucator_anterior()
            self.stergere_miscari_posibile()

    def key_press_event(self, event):
        if event.key() == Qt.Key_Z:
            self.anulare_ultima_miscare()

    def este_mat(self):
        piese = self.tabla_de_sah.piese_echipa(self.index_jucator_curent)

    def este_sah_mat(self):
        pass
