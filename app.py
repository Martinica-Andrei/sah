import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt


app = QApplication(sys.argv)

ecran = QWidget()

main_layout = QStackedLayout(ecran)

meniu_principal = QWidget()


main_layout.addWidget(meniu_principal)

main_layout.setCurrentWidget(meniu_principal)
