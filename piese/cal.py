from .piesa import Piesa
from app import layout
from .miscari.mutare import Mutare
from .miscari.capturare import Capturare


class Cal(Piesa):

    directii = [
        (2, 1), (1, 2),
        (-2, 1), (-1, 2),
        (2, -1), (1, -2),
        (-2, -1), (-1, -2)
    ]

    def __init__(self, index_fisier, directie_miscare):
        super().__init__(["imagini/white_knight.png",
                          "imagini/black_knight.png"], index_fisier)

    def afisare_miscari_posibile(self):
        rand, coloana = self.pozitie()
        miscari = []
        for r, c in self.directii:
            r += rand
            c += coloana
            if r < 0 or r >= self.tabla_de_sah.randuri or c < 0 or c >= self.tabla_de_sah.coloane:
                continue
            piesa = self.tabla_de_sah.piese[r][c]
            if piesa == None:
                miscari.append(Mutare(self, r, c))
            elif piesa.echipa != self.echipa:
                miscari.append(Capturare(self, piesa))
        self.joc_de_sah.actualizare_miscari_posibile(miscari)

        # urmatoarele_randuri = [rand + self.directie_miscare]
        # # adaugam si cea de-a doua miscare doar urmatoarea patratica nu are piesa
        # if self.prima_miscare and self.tabla_de_sah.piese[rand + self.directie_miscare][coloana] == None:
        #     urmatoarele_randuri.append(rand + self.directie_miscare * 2)
        # while len(urmatoarele_randuri) and (urmatoarele_randuri[-1] < 0 or urmatoarele_randuri[-1] >= self.tabla_de_sah.randuri):
        #     urmatoarele_randuri.pop()
        # miscari = []
        # for u in urmatoarele_randuri:
        #     if self.tabla_de_sah.piese[u][coloana] == None:
        #         miscari.append(Mutare(self, u, coloana))
        #         miscari[-1].actiune_suplimentara = lambda: self.setPrimaMiscare(
        #             False)
        # miscari += self.piese_de_capturat()
        # self.joc_de_sah.actualizare_miscari_posibile(miscari)
