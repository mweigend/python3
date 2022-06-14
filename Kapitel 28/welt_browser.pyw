#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  welt_browser.pyw 
# Objektorientiertes Programm, das ein Fenster erzeugt
#
# Python 3,  mitp Verlag
# Kap. 28
# Michael Weigend 11. 06. 2019
#----------------------------------------------------


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class Window(QWidget):                        #1
    def __init__(self):
        super().__init__()                    #2
        self.resize(250, 100)
        self.setWindowTitle('Welt-Browser')
        self.setWindowIcon(QIcon("welt.png")) #3
        self.show()                           #4
app = QApplication(sys.argv)
w = Window()                                  #5
sys.exit(app.exec_())
