#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  worldmap.pyw
# Auf einer Weltkarte wird ein gesuchter Ort angezeigt
#
# Python 3,  mitp Verlag
# Kap. 29
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from urllib.request import urlopen
import sys
from geopy.geocoders import Nominatim

MAPFILE = "world_map.png"


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.createWidgets()
        self.show()

    def createWidgets(self):
        self.setWindowTitle("Weltkarte")
        self.label = QLabel(self)
        self.pixmap = QPixmap(MAPFILE)
        self.label.setPixmap(self.pixmap)
        self.label.adjustSize()
        self.adjustSize()
        self.target = QLabel(self)
        self.target.setPixmap(QPixmap("target.gif"))
        self.button = QPushButton("Ort suchen", self)
        self.button.clicked.connect(self.search)
        self.button.move(20, 200)
        self.target.hide()

        
    def search(self):
        town, ok  = QInputDialog.getText(self, "Suche Ort",
                            "Bitte geben Sie eine Stadt ein")
        self.target.hide()
        if ok:
            geolocator = Nominatim(user_agent="worldmap.pyw")      
            location = geolocator.geocode(town, timeout=10)
            # print(location)  
            k = self.pixmap.width()/360
            x = (location.longitude + 180)* k
            y = (-location.latitude + 90) * k
            # print(x, y) 
            self.target.move(int(x), int(y))
            self.target.show()
 
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())



































