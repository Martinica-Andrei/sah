from tabla_de_sah import TablaDeSah
import piese
from app import layout


class JocDeSah:
    def __init__(self):
        self.tabla_de_sah = TablaDeSah(self)
        self.jucatori = ["alb", "negru"]
        self.index_jucator_curent = 0
        self.miscari_posibile = []
        self.adaugare_eventuri(self.index_jucator_curent)

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

    def terminare_miscare(self):
        self.stergere_miscari_posibile()
        self.setare_urmatorul_jucator()

    def adaugare_eventuri(self, echipa):
        for rand in self.tabla_de_sah.piese:
            for piesa in rand:
                if piesa == None:
                    continue
                if piesa.echipa == echipa:
                    piesa.activeaza_click_event()
                else:
                    piesa.dezactiveaza_click_event()
