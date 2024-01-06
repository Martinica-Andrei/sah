import piese
from patratica import Patratica
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import Qt


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
        self.piese_scoase = set()
        self.layout = QGridLayout()
        self.layout_configurare()
        self.creere_background()
        self.creere_piese()

    def layout_configurare(self):
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def creere_background(self):
        for i in range(self.randuri):
            self.patratele_background.append([])
            for j in range(self.coloane):
                patratica = Patratica(
                    self.lungime_patratele, self.inaltime_patratele, self.cale_fisiere_patratele[(i + j) % 2])
                self.layout.addWidget(patratica.label, i, j)
                self.patratele_background[i].append(patratica)

    def adaugare_piesa(self, piesa, rand, coloana):
        if self.piese[rand][coloana] is not None:
            self.scoatere_piesa(rand, coloana)
        self.piese[rand][coloana] = piesa
        if piesa in self.piese_scoase:
            self.piese_scoase.remove(piesa)
        piesa.tabla_de_sah = self
        piesa.joc_de_sah = self.joc_de_sah
        piesa.rand = rand
        piesa.coloana = coloana
        if piesa.rand_initial is None:
            piesa.rand_initial = rand
            piesa.coloana_initiala = coloana

    def scoatere_piesa(self, rand, coloana):
        if self.piese[rand][coloana] is None:
            return
        self.piese_scoase.add(self.piese[rand][coloana])
        self.piese[rand][coloana] = None

    def muta_piesa(self, piesa, rand, coloana):
        rand_curent, coloana_curenta = piesa.pozitie()
        self.piese[rand_curent][coloana_curenta] = None
        if self.piese[rand][coloana] is not None:
            self.scoatere_piesa(rand, coloana)
        self.piese[rand][coloana] = piesa
        piesa.rand = rand
        piesa.coloana = coloana

    def updatare_grafica(self):
        for rand in self.piese:
            for piesa in rand:
                if piesa is not None:
                    piesa.label.setParent(None)
                    self.layout.addWidget(
                        piesa.label, piesa.rand, piesa.coloana)
        for piesa in self.piese_scoase:
            piesa.label.setParent(None)

    def creere_piese(self):
        for i in range(self.coloane):
            self.adaugare_piesa(piese.Pion(piese.Piesa.negru, 1), 1, i)
            self.adaugare_piesa(piese.Pion(piese.Piesa.alb, -1),
                                self.randuri - 2, i)
        for i in [0, self.coloane - 1]:
            self.adaugare_piesa(piese.Turn(piese.Piesa.negru), 0, i)
            self.adaugare_piesa(piese.Turn(piese.Piesa.alb),
                                self.randuri - 1, i)
        for i in [1, self.coloane - 2]:
            self.adaugare_piesa(piese.Cal(piese.Piesa.negru), 0, i)
            self.adaugare_piesa(piese.Cal(piese.Piesa.alb),
                                self.randuri - 1, i)

        for i in [2, self.coloane - 3]:
            self.adaugare_piesa(piese.Nebun(piese.Piesa.negru), 0, i)
            self.adaugare_piesa(piese.Nebun(piese.Piesa.alb),
                                self.randuri - 1, i)

        self.adaugare_piesa(piese.Regina(piese.Piesa.negru), 0, 3)
        self.adaugare_piesa(piese.Regina(piese.Piesa.alb),
                            self.randuri - 1, 3)

        self.adaugare_piesa(piese.Rege(piese.Piesa.negru), 0, 4)
        self.adaugare_piesa(piese.Rege(piese.Piesa.alb),
                            self.randuri - 1, 4)

    def is_coordonate_valide(self, r, c):
        return (r >= 0 and r < self.randuri and c >= 0 and c < self.coloane)

    def piese_echipa(self, echipa):
        piese = []
        for rand in self.piese:
            for piesa in rand:
                if piesa is not None and piesa.echipa == echipa:
                    piese.append(piesa)
        return piese
