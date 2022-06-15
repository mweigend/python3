#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  ansichtskarte.pyw
# Erstellen einer Ansichtskarte (Foto plus Text).
#
# Python 3,  mitp Verlag
# Kap. 28
# Michael Weigend 11. 06. 2019
#----------------------------------------------------
 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap , QPainter, QColor, QFont                #1
import sys 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.color = QColor(0, 0, 200)
        self.font = QFont('Arial', 30)
        self.text = ""
        self.createWidgets()
        self.createLayout()
        self.filename=""
        self.show()

    def createWidgets(self):
        self.setWindowTitle("Ansichtskarte")
        self.label = QLabel()                                
        self.label.setMinimumSize(320,180)
        self.loadButton = QPushButton("Bild laden")
        self.loadButton.clicked.connect(self.load)
        self.textButton = QPushButton("Text eingeben")
        self.textButton.clicked.connect(self.setText)
             
    def createLayout(self):
        vBox = QVBoxLayout()
        vBox.addWidget(self.label)
        hBox = QHBoxLayout()
        hBox.addWidget(self.loadButton)
        hBox.addWidget(self.textButton)
        vBox.addLayout(hBox)
        self.setLayout(vBox)

    def load (self):
        filename, _ = QFileDialog.getOpenFileName(self, "Bild laden", "*.png")
        if filename:
            self.filename = filename

    def paintEvent(self, event):
        if self.filename:
            self.pixmap = QPixmap(self.filename) 
            painter = QPainter()
            painter.begin(self.pixmap)
            painter.setPen(self.color)
            painter.setFont(self.font)
            painter.drawText(QRect(0, 0, self.label.width(), 160),
                             Qt.AlignCenter, self.text)
            painter.end()
            self.label.setPixmap(self.pixmap)
            self.label.adjustSize()
            self.adjustSize()

    def setText(self):
        text, ok  = QInputDialog.getText(self, "Texteingabe",
                             "Bitte geben Sie einen Grußtext ein")
        if ok:
            self.text = text
                                         
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())



































