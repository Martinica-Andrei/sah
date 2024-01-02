import piese
import tkinter as tk
from app import layout
from patratica import Patratica


class TablaDeSah:

    cale_fisiere_patratele = [
        "imagini/white_tile.png", "imagini/black_tile.png"]
    spatiu_intre_piese = 20

    def __init__(self):
        self.patratele_background = []
        for i in range(8):
            self.patratele_background.append([])
            for j in range(8):
                patratica = Patratica(piese.Piesa.lungime_piese + self.spatiu_intre_piese, piese.Piesa.inaltime_piese + self.spatiu_intre_piese,
                                      self.cale_fisiere_patratele[(i + j) % 2])
                layout.addWidget(patratica.label, i, j)
                self.patratele_background.append(patratica)
