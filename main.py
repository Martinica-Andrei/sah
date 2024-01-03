from app import app, ecran, layout
import sys
from joc_de_sah import JocDeSah

joc = JocDeSah()

ecran.show()

sys.exit(app.exec_())
