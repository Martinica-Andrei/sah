from .piesa import Piesa
from app import layout
from .miscari.mutare import Mutare

class Pion(Piesa):
    def __init__(self, index_fisier, directie_miscare):
        super().__init__(["imagini/white_pawn.png",
                          "imagini/black_pawn.png"], index_fisier)
        self.directie_miscare = directie_miscare
        self.prima_miscare = True

    def afisare_miscari_posibile(self, event):
        rand, coloana = self.pozitie()
        urmatoarele_randuri = [rand + self.directie_miscare]
        if self.prima_miscare:
            urmatoarele_randuri.append(rand + self.directie_miscare * 2)
        while len(urmatoarele_randuri) and (urmatoarele_randuri[-1] < 0 or urmatoarele_randuri[-1] >= self.tabla_de_sah.randuri):
            urmatoarele_randuri.pop()
        miscari = []
        for u in urmatoarele_randuri:
            if self.tabla_de_sah.piese[u][coloana] == None:
                miscari.append(Mutare(self, u, coloana))
        self.joc_de_sah.actualizare_miscari_posibile(miscari)
