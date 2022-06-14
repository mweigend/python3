#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  writer.pyw
# Texteditor mit Timer. Nach 5 Sekunden Inaktivität
# gibt es einen Hinweis
#
# Python 3,  mitp Verlag
# Kap. 28
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

import sys, time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, 
        QVBoxLayout, QLabel, QTextEdit, QWidget)

class Writer(QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.text = QTextEdit(self)
        self.message = QLabel(self)
        self.timer = QTimer()

        # Layout
        vBox = QVBoxLayout()
        vBox.addWidget(self.text)
        vBox.addWidget(self.message)
        self.setLayout(vBox)

        # Connections
        self.text.textChanged.connect(self.clearLabel)   #1
        self.timer.timeout.connect(self.hint)            #2
        
        self.timer.start(5000)                           #3
        self.show()

    def hint(self):                                      #4
        self.message.setText("Bitte Text eingeben!")
        #self.timer.start(1000)                          #5
        
    def clearLabel(self):
        self.message.setText("")                         #6
        self.timer.stop()                                #7
        self.timer.start(5000)
  

app = QApplication(sys.argv)
w = Writer()
sys.exit(app.exec_())
