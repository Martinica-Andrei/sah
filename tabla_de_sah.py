import piese
from app import layout
from patratica import Patratica


class TablaDeSah:

    cale_fisiere_patratele = [
        "imagini/white_tile.png", "imagini/black_tile.png"]
    spatiu_intre_piese = 20
    lungime_patratele = piese.Piesa.lungime_piese + spatiu_intre_piese
    inaltime_patratele = piese.Piesa.inaltime_piese + spatiu_intre_piese

    def __init__(self, joc_de_sah):
        self.joc_de_sah = joc_de_sah
        self.randuri = 8
        self.coloane = 8
        self.patratele_background = []
        self.piese = [[None for c in range(self.coloane)]
                      for r in range(self.randuri)]
        self.creere_background()
        self.creere_piese()

    def creere_background(self):
        for i in range(self.randuri):
            self.patratele_background.append([])
            for j in range(self.coloane):
                patratica = Patratica(
                    self.lungime_patratele, self.inaltime_patratele, self.cale_fisiere_patratele[(i + j) % 2])
                layout.addWidget(patratica.label, i, j)
                self.patratele_background[i].append(patratica)

    def adaugare_piesa(self, piesa, rand, coloana):
        layout.addWidget(piesa.label, rand, coloana)
        self.piese[rand][coloana] = piesa
        piesa.tabla_de_sah = self
        piesa.joc_de_sah = self.joc_de_sah

    def muta_piesa(self, piesa, rand, coloana):
        rand_curent, coloana_curenta = piesa.pozitie()
        self.piese[rand_curent][coloana_curenta] = None
        self.piese[rand][coloana] = piesa
        piesa.label.setParent(None)
        layout.addWidget(piesa.label, rand, coloana)

    def creere_piese(self):
        for i in range(8):
            self.adaugare_piesa(piese.Pion(piese.Piesa.negru, 1), 1, i)
            self.adaugare_piesa(piese.Pion(
                piese.Piesa.alb, -1), self.randuri - 2, i)