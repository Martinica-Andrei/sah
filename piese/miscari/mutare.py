from .actiune import Actiune


class Mutare(Actiune):
    def __init__(self, piesa, rand_tinta, coloana_tinta):
        super().__init__("imagini/blue.png")
        self.piesa = piesa
        self.piesa_rand_curent, self.piesa_coloana_curenta = self.piesa.pozitie()
        self.piesa_rand_tinta = rand_tinta
        self.piesa_coloana_tinta = coloana_tinta

    def executa(self):
        self.piesa.tabla_de_sah.muta_piesa(
            self.piesa, self.piesa_rand_tinta, self.piesa_coloana_tinta)
        super().executa()

    def anuleaza(self):
        self.piesa.tabla_de_sah.muta_piesa(
            self.piesa, self.piesa_rand_curent, self.piesa_coloana_curenta)