from patratica import Patratica
from .miscari.mutare import Mutare
from .miscari.capturare import Capturare


class Piesa(Patratica):
    lungime_piese = 60
    inaltime_piese = 60
    alb = 0
    negru = 1

    def __init__(self, cale_fisiere, index_fisier):
        super().__init__(self.lungime_piese,
                         self.inaltime_piese, cale_fisiere[index_fisier])
        self.tabla_de_sah = None
        self.joc_de_sah = None
        self.rand = None
        self.coloana = None
        self.echipa = index_fisier  # index fisier coincide cu echipa
        self.rand_initial = None
        self.coloana_initiala = None
        self.miscari_facute = 0

    def pozitie(self):
        return (self.rand, self.coloana)

    def miscari_posibile(self):
        pass

    def coordonate_orizontala_verticala(self):
        rand, coloana = self.pozitie()
        coordonate = [[], [], [], []]
        # dreapta
        for c in range(coloana + 1, self.tabla_de_sah.coloane):
            coordonate[0].append((rand, c))
        # stanga
        for c in range(coloana - 1, -1, -1):
            coordonate[1].append((rand, c))
        # sus
        for r in range(rand - 1, -1, -1):
            coordonate[2].append((r, coloana))
        # jos
        for r in range(rand + 1, self.tabla_de_sah.randuri):
            coordonate[3].append((r, coloana))
        return coordonate

    def coordonate_diagonala(self):
        rand, coloana = self.pozitie()
        coordonate = [[], [], [], []]
        for i in range(1, self.tabla_de_sah.randuri + self.tabla_de_sah.coloane):
            index_coordonate = 0
            for j in [-1, 1]:
                for k in [-1, 1]:
                    r = rand + (j * i)
                    c = coloana + (k * i)
                    if self.tabla_de_sah.is_coordonate_valide(r, c):
                        coordonate[index_coordonate].append((r, c))
                    index_coordonate += 1
        return coordonate

    def ia_miscare(self, rand, coloana):
        piesa = self.tabla_de_sah.piese[rand][coloana]
        if piesa is None:
            return Mutare(self, rand, coloana)
        elif piesa.echipa != self.echipa:
            return Capturare(self, piesa)
        return None
