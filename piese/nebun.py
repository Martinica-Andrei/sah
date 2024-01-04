from .piesa import Piesa
from app import layout
from .miscari.mutare import Mutare
from .miscari.capturare import Capturare

# nebunul are aproape acelasi cod ca turnul
class Nebun(Piesa):
    def __init__(self, index_fisier):
        super().__init__(["imagini/white_bishop.png",
                          "imagini/black_bishop.png"], index_fisier)

    def ia_miscare(self, rand, coloana):
        piesa = self.tabla_de_sah.piese[rand][coloana]
        if piesa == None:
            return Mutare(self, rand, coloana)
        elif piesa.echipa != self.echipa:
            return Capturare(self, piesa)
        return None

    def afisare_miscari_posibile(self):
        miscari = []
        coordonate = self.coordonate_diagonala()
        for directie in coordonate:
            for r, c in directie:
                miscare = self.ia_miscare(r, c)
                if miscare != None:
                    miscari.append(miscare)
                if miscare == None or type(miscare) == Capturare:
                    break
        self.joc_de_sah.actualizare_miscari_posibile(miscari)
