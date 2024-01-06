from PyQt5.QtWidgets import QDialog, QGridLayout
from piese.cal import Cal
from piese.nebun import Nebun
from piese.regina import Regina
from piese.turn import Turn
from patratica import Patratica
from PyQt5.QtCore import Qt


class DialogPromovarePion(QDialog):
    def __init__(self, echipa):
        super().__init__()
        self.echipa = echipa

        # scoate butonul de inchidere dialog
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

        self.interfata()

    def interfata(self):
        # Set up the layout
        layout = QGridLayout(self)
        self.setLayout(layout)
        # Add labels to the layout
        texturi_patratele = [
            "imagini/white_tile.png", "imagini/black_tile.png"]
        for i, tip_piesa in enumerate([Regina, Turn, Nebun, Cal]):
            piesa = tip_piesa(self.echipa)
            piesa.label.mousePressEvent = lambda e, tip_piesa=tip_piesa: self.piesa_click_event(
                e, tip_piesa)
            piesa.redimensionare(80, 80)
            patratica = Patratica(120, 120, texturi_patratele[i % 2])
            layout.addWidget(patratica.label, 0, i)
            layout.addWidget(piesa.label, 0, i)
        self.setWindowTitle('Promovare pion')
        # modal inseamna ca opreste evenimenturile care nu sunt ale dialogului
        self.setModal(True)

    def piesa_click_event(self, e, tip_piesa):
        mouse_butoane = e.buttons()
        if mouse_butoane & Qt.LeftButton:
            self.tip_piesa = tip_piesa
            self.accept()
