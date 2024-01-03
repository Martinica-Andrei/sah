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
        ecran.keyPressEvent = self.keyPressEvent

    def stergere_miscari_posibile(self):
        for miscare in self.miscari_posibile:
            # layout.removeWidget(miscare.label) # nu prea sterge uneori prin urmare folosim setParent(None)
            miscare.label.setParent(None)
        self.miscari_posibile = []

    def adaugare_miscari_posibile(self, miscari_posibile):
        for miscare in miscari_posibile:
            layout.addWidget(
                miscare.label, miscare.piesa_rand_tinta, miscare.piesa_coloana_tinta)
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
                if piesa == None:
                    patratica.label.mousePressEvent = lambda e: self.stergere_miscari_posibile()
                    continue
                # nu trebuie setat mousePressEvent la patratica pentru ca e acoperit complet de
                # piesa
                if piesa.echipa == echipa:
                    piesa.activeaza_click_event()
                else:
                    piesa.label.mousePressEvent = lambda e: self.stergere_miscari_posibile()

    def anulare_ultima_miscare(self):
        if len(self.miscari_facute):    
            ultima_miscare = self.miscari_facute.pop()
            ultima_miscare.anuleaza()
            self.setare_jucator_anterior()
            self.stergere_miscari_posibile()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z:
            self.anulare_ultima_miscare()
