from tabla_de_sah import TablaDeSah
import piese
from app import layout

class JocDeSah:
    def __init__(self):
        self.tabla_de_sah = TablaDeSah(self)
        self.jucatori = ["alb", "negru"]
        self.index_jucator_curent = 0
        self.miscari_posibile = []

    def stergere_miscari_posibile(self):
        for miscare in self.miscari_posibile:
            layout.removeWidget(miscare.label)
        self.miscari_posibile = []

    def adaugare_miscari_posibile(self, miscari_posibile):
        for miscare in miscari_posibile:
            layout.addWidget(miscare.label, miscare.piesa_rand_tinta, miscare.piesa_coloana_tinta)
            self.miscari_posibile.append(miscare)

    def actualizare_miscari_posibile(self, miscari_posibile):
        self.stergere_miscari_posibile()
        self.adaugare_miscari_posibile(miscari_posibile)