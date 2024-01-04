from .piesa import Piesa
from app import layout
from .miscari.mutare import Mutare
from .miscari.capturare import Capturare


class Rege(Piesa):

    # directii = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, index_fisier):
        super().__init__(["imagini/white_king.png",
                          "imagini/black_king.png"], index_fisier)

    def ia_miscare(self, rand, coloana):
        piesa = self.tabla_de_sah.piese[rand][coloana]
        if piesa == None:
            return Mutare(self, rand, coloana)
        elif piesa.echipa != self.echipa:
            return Capturare(self, piesa)
        return None

    def coordonate(self):
        rand, coloana = self.pozitie()
        coord = []
        for r in range(-1, 2):
            for c in range(-1, 2):
                r_rezultat = r + rand
                c_rezultat = c + coloana
                if r == c == 0 or self.tabla_de_sah.is_coordonate_valide(r_rezultat,c_rezultat) == False:
                    continue
                coord.append((r_rezultat, c_rezultat))
        return coord


    def afisare_miscari_posibile(self):
        miscari = []
        for r, c in self.coordonate():
            miscare = self.ia_miscare(r, c)
            if miscare != None:
                miscari.append(miscare)
        self.joc_de_sah.actualizare_miscari_posibile(miscari)
