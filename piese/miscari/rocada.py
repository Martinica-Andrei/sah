from .actiune import Actiune


class Rocada(Actiune):
    def __init__(self, piesa, rand_tinta, coloana_tinta, turn, turn_rand_tinta, turn_coloana_tinta):
        super().__init__("imagini/blue.png", piesa, rand_tinta, coloana_tinta)
        self.turn = turn
        self.turn_rand_curent, self.turn_coloana_curenta = self.turn.pozitie()
        self.turn_rand_tinta = turn_rand_tinta
        self.turn_coloana_tinta = turn_coloana_tinta

    def executa(self):
        self.piesa.tabla_de_sah.muta_piesa(
            self.piesa, self.piesa_rand_tinta, self.piesa_coloana_tinta)
        self.piesa.tabla_de_sah.muta_piesa(self.turn, self.turn_rand_tinta, self.turn_coloana_tinta)
        super().executa()

    def anuleaza(self):
        self.piesa.tabla_de_sah.muta_piesa(
            self.piesa, self.piesa_rand_curent, self.piesa_coloana_curenta)
        self.piesa.tabla_de_sah.muta_piesa(self.turn, self.turn_rand_curent, self.turn_coloana_curenta)
        super().anuleaza()
