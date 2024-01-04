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

    def __init__(self, index_fisier):
        super().__init__(["imagini/white_knight.png",
                          "imagini/black_knight.png"], index_fisier)

    def miscari_posibile(self):
        rand, coloana = self.pozitie()
        miscari = []
        for r, c in self.directii:
            r += rand
            c += coloana
            if self.tabla_de_sah.is_coordonate_valide(r, c) == False:
                continue
            piesa = self.tabla_de_sah.piese[r][c]
            if piesa is None:
                miscari.append(Mutare(self, r, c))
            elif piesa.echipa != self.echipa:
                miscari.append(Capturare(self, piesa))
        return miscari
        