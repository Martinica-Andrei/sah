from .piesa import Piesa
from app import layout
from .miscari.mutare import Mutare
from .miscari.capturare import Capturare


class Turn(Piesa):
    def __init__(self, index_fisier, directie_miscare):
        super().__init__(["imagini/white_rook.png",
                          "imagini/black_rook.png"], index_fisier)

    def ia_miscare(self, rand,coloana):
        piesa = self.tabla_de_sah.piese[rand][coloana]
        if piesa == None:
            return Mutare(self, rand, coloana)
        elif piesa.echipa != self.echipa:
            return Capturare(self, piesa)
        return None

    def afisare_miscari_posibile(self):
        rand, coloana = self.pozitie()
        miscari = []
        #dreapta
        for c in range(coloana + 1, self.tabla_de_sah.coloane):
            miscare = self.ia_miscare(rand,c)
            if miscare != None:
                miscari.append(miscare)
            if miscare == None or type(miscare) == Capturare:
                break
        #stanga
        for c in range(coloana - 1, -1, -1):
            miscare = self.ia_miscare(rand,c)
            if miscare != None:
                miscari.append(miscare)
            if miscare == None or type(miscare) == Capturare:
                break
        #sus
        for r in range(rand - 1, -1, -1):
            miscare = self.ia_miscare(r,coloana)
            if miscare != None:
                miscari.append(miscare)
            if miscare == None or type(miscare) == Capturare:
                break
        #jos
        for r in range(rand + 1, self.tabla_de_sah.randuri):
            miscare = self.ia_miscare(r,coloana)
            if miscare != None:
                miscari.append(miscare)
            if miscare == None or type(miscare) == Capturare:
                break
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