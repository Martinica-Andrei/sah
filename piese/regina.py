from .piesa import Piesa
from app import layout
from .miscari.mutare import Mutare
from .miscari.capturare import Capturare


class Regina(Piesa):
    def __init__(self, index_fisier):
        super().__init__(["imagini/white_queen.png",
                          "imagini/black_queen.png"], index_fisier)

    def afisare_miscari_posibile(self):
        miscari = []
        coordonate = self.coordonate_diagonala() + self.coordonate_orizontala_verticala()
        for directie in coordonate:
            for r, c in directie:
                miscare = self.ia_miscare(r, c)
                if miscare != None:
                    miscari.append(miscare)
                if miscare == None or type(miscare) == Capturare:
                    break
        self.joc_de_sah.actualizare_miscari_posibile(miscari)
