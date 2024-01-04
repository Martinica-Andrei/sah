from .piesa import Piesa
from app import layout
from .miscari.mutare import Mutare
from .miscari.capturare import Capturare


class Turn(Piesa):
    def __init__(self, index_fisier):
        super().__init__(["imagini/white_rook.png",
                          "imagini/black_rook.png"], index_fisier)

    def miscari_posibile(self):
        miscari = []
        coordonate = self.coordonate_orizontala_verticala()
        for directie in coordonate:
            for r, c in directie:
                miscare = self.ia_miscare(r, c)
                if miscare is not None:
                    miscari.append(miscare)
                if miscare is None or type(miscare) == Capturare:
                    break
        return miscari
