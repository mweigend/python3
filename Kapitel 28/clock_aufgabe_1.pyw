#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  clock_aufgabe_1.pyw
# Digitaluhr, die den Bildschirm ganz ausfüllt
#
# Python 3,  mitp Verlag
# Kap. 28
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

import sys, time
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtGui

STYLE = """background: qlineargradient(x1: 0, y1: 0,
           x2: 0, y2: 1,stop: 0 blue, stop: 1 lightblue);
        """                                               #1
STYLE_LABEL = """background:transparent; color: white"""  #2

class Clock(QWidget):  
    def __init__(self):
        super().__init__()
        
        self.label = QLabel("", self)
        font = QtGui.QFont("Arial",160)                   #3
        self.label.setFont(font)
        self.setStyleSheet(STYLE)
        self.label.setStyleSheet(STYLE_LABEL)             #4
        self.label.move(250, 250)                         

        self.timer = QTimer()                             #5
        self.timer.timeout.connect(self.update)          
        self.timer.start(1000)                            #6
        self.showFullScreen()                             #7

    def update(self):
        t = time.asctime().split()                        #8      
        self.label.setText(t[3])                       
        self.label.adjustSize()                           #9
     
    def keyPressEvent(self, e):                          #10
        self.showNormal()                                #11
        
app = QApplication(sys.argv)
clock = Clock()
sys.exit(app.exec_())
