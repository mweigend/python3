#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  hello_qt.pyw 
# Erszeugt ein Fenster mit Titel "Hallo Qt"
#
# Python 3,  mitp Verlag
# Kap. 28
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

import sys
from PyQt5.QtWidgets import QApplication, QWidget
 
app = QApplication(sys.argv)
w = QWidget()
w.resize(250, 100)
w.setWindowTitle("Hallo Qt")
w.show()
sys.exit(app.exec_())
