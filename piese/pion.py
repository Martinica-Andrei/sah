from .piesa import Piesa
from app import layout

class Pion(Piesa):
    def __init__(self, index_fisier, directie_miscare):
        super().__init__(["imagini/white_pawn.png",
                          "imagini/black_pawn.png"], index_fisier)
        self.directie_miscare = directie_miscare
        self.prima_miscare = True

    def afisare_miscari_posibile(self, event):
        rand, coloana = self.pozitie()
        self.tabla_de_sah.muta_piesa(self, rand + self.directie_miscare, coloana)
        pass
