from patratica import Patratica
from app import layout

class Mutare(Patratica):
    def __init__(self, piesa, rand_tinta, coloana_tinta):
        super().__init__(50,50, "imagini/ok_move")
        self.piesa = piesa
        self.piesa_rand_curent, self.piese_coloana_curenta = self.piesa.pozitie()
        self.piesa_rand_tinta = rand_tinta
        self.piesa_coloana_tinta = coloana_tinta
        #self.label.mousePressEvent = lambda e : self.executa()

    def executa(self):
        self.piesa.tabla_de_sah.muta_piesa(self.piesa, self.piesa_rand_tinta, self.piesa_coloana_tinta)
        #self.piesa.joc_de_sah.stergere_miscari_posibile()

    def anuleaza(self):
        self.piesa.tabla_de_sah.muta_piesa(
            self.piesa, self.piesa_rand_curent, self.piese_coloana_curenta)
