from .piesa import Piesa
class Pion(Piesa):  
    def __init__(self, index_fisier):
       super().__init__(["imagini/white_pawn.png", "imagini/black_pawn.png"], index_fisier)
        