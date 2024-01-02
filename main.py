from app import app, ecran, layout
import sys
from tabla_de_sah import TablaDeSah
import piese
sah_marime = 8

t = TablaDeSah()
for i in range(sah_marime):
    for j in range(sah_marime):
        pion = piese.Pion(0)
        layout.addWidget(pion.label, i, j)


ecran.show()
sys.exit(app.exec_())
