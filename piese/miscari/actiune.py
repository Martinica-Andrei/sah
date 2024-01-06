from patratica import Patratica


class Actiune:
    def __init__(self, cale_fisier):
        self.cale_fisier = cale_fisier
        self.grafica = None
        self.terminare_miscare = None
        self.actiune_suplimentara = None

    def init_grafica(self):
        if self.grafica is None:
            self.grafica = Patratica(50, 50, self.cale_fisier)

    def executa(self):
        if self.actiune_suplimentara:
            self.actiune_suplimentara()
        if self.terminare_miscare:
            self.terminare_miscare(self)

    def anuleaza(self):
        pass
