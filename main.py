from app import app, ecran, layout
import sys
from joc_de_sah import JocDeSah
sah_marime = 8

joc = JocDeSah()


ecran.show()
sys.exit(app.exec_())
