from .piesa import Piesa
from .miscari.rocada import Rocada


class Rege(Piesa):

    # directii = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, index_fisier):
        super().__init__(["imagini/white_king.png",
                          "imagini/black_king.png"], index_fisier)

    def coordonate(self):
        rand, coloana = self.pozitie()
        coord = []
        for r in range(-1, 2):
            for c in range(-1, 2):
                r_rezultat = r + rand
                c_rezultat = c + coloana
                if r == c == 0 or self.tabla_de_sah.is_coordonate_valide(r_rezultat, c_rezultat) == False:
                    continue
                coord.append((r_rezultat, c_rezultat))
        return coord

    def miscari_rocade(self):
        miscari = []
        if len(self.miscari_facute) > 0 or self.joc_de_sah.este_check_jucator_curent:
            return miscari
        rand, coloana = self.pozitie()
        turn_stanga = self.tabla_de_sah.piese[rand][0]
        turn_dreapta = self.tabla_de_sah.piese[rand][-1]
        # codul se poate optimiza
        if turn_stanga is not None and len(turn_stanga.miscari_facute) == 0:
            e_valid = True
            for c in range(coloana - 1, 0, -1):
                if self.tabla_de_sah.piese[rand][c] is not None:
                    e_valid = False
                    break
            if e_valid:
                miscari.append(Rocada(self, rand, coloana - 2, turn_stanga, rand, coloana - 1))
        if turn_dreapta is not None and len(turn_dreapta.miscari_facute) == 0:
            e_valid = True
            for c in range(coloana + 1, self.tabla_de_sah.coloane - 1):
                if self.tabla_de_sah.piese[rand][c] is not None:
                    e_valid = False
                    break
            if e_valid:
                miscari.append(Rocada(self, rand, coloana + 2, turn_dreapta, rand, coloana + 1))
        return miscari

    def miscari_posibile(self):
        miscari = []
        for r, c in self.coordonate():
            miscare = self.ia_miscare(r, c)
            if miscare is not None:
                miscari.append(miscare)
        miscari += self.miscari_rocade()
        return miscari
