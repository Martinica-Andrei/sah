from .actiune import Actiune
from ..cal import Cal
from ..nebun import Nebun
from ..regina import Regina
from ..turn import Turn
from dialog_promovare_pion import DialogPromovarePion


class Promovare(Actiune):
    def __init__(self, piesa, rand_tinta, coloana_tinta):
        super().__init__("imagini/blue.png", piesa, rand_tinta, coloana_tinta)
        self.piesa_tinta = self.piesa.tabla_de_sah.piese[self.piesa_rand_tinta][self.piesa_coloana_tinta]
        if self.piesa_tinta:
            self.cale_fisier = "imagini/green.png"
        self.tip_piesa = Regina

    def executa(self):
        if self.grafica is not None:
            dialog = DialogPromovarePion(self.piesa.echipa)
            dialog.exec_()
            self.tip_piesa = dialog.tip_piesa
        piesa_noua = self.tip_piesa(self.piesa.echipa)
        self.piesa.tabla_de_sah.scoatere_piesa(self.piesa.rand, self.piesa.coloana)
        self.piesa.tabla_de_sah.adaugare_piesa(piesa_noua, self.piesa_rand_tinta, self.piesa_coloana_tinta)
        super().executa()

    def anuleaza(self):
        self.piesa.tabla_de_sah.scoatere_piesa(self.piesa_rand_tinta, self.piesa_coloana_tinta)
        self.piesa.tabla_de_sah.adaugare_piesa(self.piesa, self.piesa_rand_curent, self.piesa_coloana_curenta)
        if self.piesa_tinta:
            self.piesa.tabla_de_sah.adaugare_piesa(self.piesa_tinta, self.piesa_rand_tinta, self.piesa_coloana_tinta)
        super().anuleaza()
