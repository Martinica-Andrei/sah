from patratica import Patratica


class Actiune(Patratica):
    def __init__(self, cale_fisier):
        super().__init__(50, 50, cale_fisier)
        self.label.mousePressEvent = lambda e: self.executa()
        self.terminare_miscare = None
        self.actiune_suplimentara = None

    def executa(self):
        pass

    def anuleaza(self):
        pass
