from .piesa import Piesa
from .miscari.mutare import Mutare
from .miscari.capturare import Capturare
from .miscari.promovare import Promovare
from .miscari.en_passant import EnPassant
from .rege import Rege


class Pion(Piesa):
    def __init__(self, index_fisier, directie_miscare):
        super().__init__(["imagini/white_pawn.png",
                          "imagini/black_pawn.png"], index_fisier)
        # directie_miscare e 1 pentru jos si -1 pentru sus
        self.directie_miscare = directie_miscare

    def miscari_de_capturat(self):
        rand, coloana = self.pozitie()
        rand_urmator = rand + self.directie_miscare
        miscari = []
        for c in [coloana - 1, coloana + 1]:
            if self.tabla_de_sah.is_coordonate_valide(rand_urmator, c):
                piesa_tinta = self.tabla_de_sah.piese[rand_urmator][c]
                if piesa_tinta is not None and piesa_tinta.echipa != self.echipa:
                    if (rand_urmator == 0 or rand_urmator == self.tabla_de_sah.randuri - 1) and type(piesa_tinta) != Rege:
                        miscari.append(Promovare(self, rand_urmator, c))
                    else:
                        miscari.append(Capturare(self, piesa_tinta))
        return miscari

    def ultima_miscare_valida_en_passant(self):
        if len(self.joc_de_sah.miscari_facute) == 0:
            return False
        ultima_miscare = self.joc_de_sah.miscari_facute[-1]
        return (type(ultima_miscare) == Mutare and type(ultima_miscare.piesa) == Pion and ultima_miscare.distanta() == 2)

    def miscare_en_passant(self):
        miscari = []
        if self.ultima_miscare_valida_en_passant() == False:
            return miscari
        pion_en_passant = self.joc_de_sah.miscari_facute[-1].piesa
        rand, coloana = self.pozitie()       
        for c in [coloana -1, coloana + 1]:
            if self.tabla_de_sah.is_coordonate_valide(rand, c):
                piesa_tinta = self.tabla_de_sah.piese[rand][c] 
                if piesa_tinta == pion_en_passant:
                    miscari.append(EnPassant(self, pion_en_passant, rand + self.directie_miscare, c))
                    break
        return miscari

    def miscari_posibile(self):
        rand, coloana = self.pozitie()
        este_prima_miscare = (len(self.miscari_facute) == 0)
        nr_randuri = 1 + este_prima_miscare
        oprire = rand + ((nr_randuri + 1) * self.directie_miscare)
        miscari = []
        for r in range(rand + self.directie_miscare, oprire, self.directie_miscare):
            if self.tabla_de_sah.is_coordonate_valide(r, coloana) and self.tabla_de_sah.piese[r][coloana] is None:
                if r == 0 or r == self.tabla_de_sah.randuri - 1:
                    miscari.append(Promovare(self, r, coloana))
                else:
                    miscari.append(Mutare(self, r, coloana))
            else:
                break
        miscari += self.miscari_de_capturat() + self.miscare_en_passant()
        return miscari
