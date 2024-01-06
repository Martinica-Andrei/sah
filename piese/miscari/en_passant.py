from .actiune import Actiune


class EnPassant(Actiune):
    def __init__(self, piesa, pion_capturare, rand_tinta, coloana_tinta):
        super().__init__("imagini/green.png")
        self.piesa = piesa
        self.pion_capturare = pion_capturare
        self.piesa_rand_curent, self.piesa_coloana_curenta = self.piesa.pozitie()
        self.piesa_rand_tinta = rand_tinta
        self.piesa_coloana_tinta = coloana_tinta

    def executa(self):
        self.piesa.tabla_de_sah.muta_piesa(
            self.piesa, self.piesa_rand_tinta, self.piesa_coloana_tinta)
        self.piesa.tabla_de_sah.scoatere_piesa(
            self.pion_capturare.rand, self.pion_capturare.coloana)
        super().executa()

    def anuleaza(self):
        self.piesa.tabla_de_sah.muta_piesa(
            self.piesa, self.piesa_rand_curent, self.piesa_coloana_curenta)
        self.piesa.tabla_de_sah.adaugare_piesa(
            self.pion_capturare, self.pion_capturare.rand, self.pion_capturare.coloana)
