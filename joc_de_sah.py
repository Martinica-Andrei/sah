from tabla_de_sah import TablaDeSah
import piese
from app import layout

class JocDeSah:
    def __init__(self):
        self.tabla_de_sah = TablaDeSah(self)
        self.jucatori = ["alb", "negru"]
        self.index_jucator_curent = 0
        self.miscari_posibile = []