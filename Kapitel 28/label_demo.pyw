#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  label_demo.pyw 
# Ein Anwednungsfenster mit Text und Bild.
#
# Python 3,  mitp Verlag
# Kap. 28
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class PhotoView(QWidget):
    def __init__(self):
        super().__init__()
        picture = QPixmap("skytree.png")
        self.label1= QLabel()
        self.label1.setPixmap(picture)
        self.label2 = QLabel("Der Skytree in Tokio, Japan")
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        self.setLayout(vbox)
        self.show()

app = QApplication(sys.argv)
pv = PhotoView()
sys.exit(app.exec_())
