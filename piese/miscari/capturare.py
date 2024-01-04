from .actiune import Actiune

class Capturare(Actiune):
    def __init__(self, piesa, piesa_tinta):
        super().__init__("imagini/green.png")
        self.piesa = piesa
        self.piesa_tinta = piesa_tinta
        self.piesa_rand_curent, self.piese_coloana_curenta = self.piesa.pozitie()
        self.piesa_rand_tinta, self.piesa_coloana_tinta = self.piesa_tinta.pozitie()

    def executa(self):
        self.piesa.tabla_de_sah.scoatere_piesa(self.piesa_rand_tinta, self.piesa_coloana_tinta)
        self.piesa.tabla_de_sah.muta_piesa(
        self.piesa, self.piesa_rand_tinta, self.piesa_coloana_tinta)
        super().executa()

    def anuleaza(self):
        tabla = self.piesa.tabla_de_sah
        tabla.muta_piesa(self.piesa, self.piesa_rand_curent, self.piese_coloana_curenta)
        tabla.adaugare_piesa(self.piesa_tinta, self.piesa_rand_tinta, self.piesa_coloana_tinta)
