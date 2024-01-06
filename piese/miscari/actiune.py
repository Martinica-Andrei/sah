from patratica import Patratica


class Actiune:
    def __init__(self, cale_fisier, piesa, rand_tinta, coloana_tinta):
        self.cale_fisier = cale_fisier
        self.piesa = piesa
        self.piesa_rand_curent, self.piesa_coloana_curenta = self.piesa.pozitie()
        self.piesa_rand_tinta = rand_tinta
        self.piesa_coloana_tinta = coloana_tinta
        self.grafica = None
        self.terminare_miscare = None
        self.actiune_suplimentara = None

    def init_grafica(self):
        if self.grafica is None:
            self.grafica = Patratica(60, 60, self.cale_fisier)

    def executa(self):
        if self.actiune_suplimentara:
            self.actiune_suplimentara()
        if self.terminare_miscare:
            self.terminare_miscare(self)

    def anuleaza(self):
        pass
