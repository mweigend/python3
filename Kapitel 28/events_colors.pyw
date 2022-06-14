#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  events_colors.pyw
# Ein Beispiel zur Event-Verarbeitung
#
# Python 3,  mitp Verlag
# Kap. 28
# Michael Weigend 11. 06. 2019
#----------------------------------------------------
import sys, random
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt

COLOR = ["green", "blue", "black", "red", "rgb(12, 233, 33)"]

class Lamp(QWidget):  
    def __init__(self):
        super().__init__()
        self.showFullScreen()
        
    def keyPressEvent(self, e):                 #1
        if e.key() == Qt.Key_Escape:            #2
            self.close()                        
        else:
            style = "background:" + random.choice(COLOR)
            self.setStyleSheet(style)
            
app = QApplication(sys.argv)
lamp = Lamp()
sys.exit(app.exec_())


