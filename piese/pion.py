from .piesa import Piesa
from .miscari.mutare import Mutare
from .miscari.capturare import Capturare


class Pion(Piesa):
    def __init__(self, index_fisier, directie_miscare):
        super().__init__(["imagini/white_pawn.png",
                          "imagini/black_pawn.png"], index_fisier)
        #directie_miscare e 1 pentru jos si -1 pentru sus
        self.directie_miscare = directie_miscare

    def miscari_de_capturat(self):
        rand, coloana = self.pozitie()
        rand_urmator = rand + self.directie_miscare
        miscari = []
        for c in [coloana - 1, coloana + 1]:
            if self.tabla_de_sah.is_coordonate_valide(rand_urmator, c):
                piesa_tinta = self.tabla_de_sah.piese[rand_urmator][c]
                if piesa_tinta is not None and piesa_tinta.echipa != self.echipa:
                    miscari.append(Capturare(self, piesa_tinta))
        return miscari

    def miscari_posibile(self):
        rand, coloana = self.pozitie()
        este_prima_miscare = (self.rand_initial == rand)
        nr_randuri = 1 + este_prima_miscare
        oprire = rand + ((nr_randuri + 1) * self.directie_miscare)
        miscari = []
        for r in range(rand + self.directie_miscare, oprire, self.directie_miscare):
            if self.tabla_de_sah.is_coordonate_valide(r, coloana) and self.tabla_de_sah.piese[r][coloana] is None:
                miscari.append(Mutare(self, r, coloana))
            else:
                break
        miscari += self.miscari_de_capturat()
        return miscari
            