from .piesa import Piesa
from app import layout
from .miscari.mutare import Mutare
from .miscari.capturare import Capturare

class Pion(Piesa):
    def __init__(self, index_fisier, directie_miscare):
        super().__init__(["imagini/white_pawn.png",
                          "imagini/black_pawn.png"], index_fisier)
        self.directie_miscare = directie_miscare
        self.prima_miscare = True
    
    def piese_de_capturat(self):
        rand, coloana = self.pozitie()
        rand_urmator = rand + self.directie_miscare
        miscari = []
        if rand_urmator < 0 or rand_urmator >= self.tabla_de_sah.randuri:
            return miscari
        for coloana in [coloana - 1, coloana + 1]:
            if coloana >= 0 and coloana < self.tabla_de_sah.coloane:
                # trebuie modificat mai tarziu pentru rege
                piesa_tinta = self.tabla_de_sah.piese[rand_urmator][coloana] 
                if piesa_tinta != None:
                    miscari.append(Capturare(self, piesa_tinta))
                    miscari[-1].actiune_suplimentara = lambda : self.setPrimaMiscare(False)
        return miscari

    def afisare_miscari_posibile(self):
        rand, coloana = self.pozitie()
        urmatoarele_randuri = [rand + self.directie_miscare]
        # adaugam si cea de-a doua miscare doar urmatoarea patratica nu are piesa
        if self.prima_miscare and self.tabla_de_sah.piese[rand + self.directie_miscare][coloana] == None:
            urmatoarele_randuri.append(rand + self.directie_miscare * 2)
        while len(urmatoarele_randuri) and (urmatoarele_randuri[-1] < 0 or urmatoarele_randuri[-1] >= self.tabla_de_sah.randuri):
            urmatoarele_randuri.pop()
        miscari = []
        for u in urmatoarele_randuri:
            if self.tabla_de_sah.piese[u][coloana] == None:
                miscari.append(Mutare(self, u, coloana))
                miscari[-1].actiune_suplimentara = lambda : self.setPrimaMiscare(False)
        miscari += self.piese_de_capturat()
        self.joc_de_sah.actualizare_miscari_posibile(miscari)

    def setPrimaMiscare(self, valoare):
        self.prima_miscare = valoare