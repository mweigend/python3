#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  ansichtskarte_aufgabe_2.pyw
# Editor für eine Ansichtskarte mit Auswahl des Fonts
# und der Schriftfarbe
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 29
# Michael Weigend 22.09.2016
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
        self.filename = ""
        self.show()

    def createWidgets(self):
        self.setWindowTitle("Ansichtskarte")
        self.label = QLabel()                                
        self.label.setMinimumSize(320,180)

        self.loadButton = QPushButton("Bild laden")
        self.loadButton.clicked.connect(self.load)
        self.saveButton = QPushButton("Bild Speichern")
        self.saveButton.clicked.connect(self.save)
        self.textButton = QPushButton("Text eingeben")
        self.textButton.clicked.connect(self.setText)
        self.colorButton = QPushButton("Farbe")
        self.colorButton.clicked.connect(self.selectColor)
        self.fontButton = QPushButton("Schriftart")
        self.fontButton.clicked.connect(self.selectFont)
        
     
    def createLayout(self):
        vBox = QVBoxLayout()
        vBox.addWidget(self.label)
        hBox = QHBoxLayout()
        hBox.addWidget(self.loadButton)
        hBox.addWidget(self.saveButton)
        hBox.addWidget(self.textButton)
        hBox.addWidget(self.colorButton)
        hBox.addWidget(self.fontButton)
        vBox.addLayout(hBox)
        self.setLayout(vBox)

    def save(self):
        filename, _ = QFileDialog.getSaveFileName(parent=self,
                                           caption ="Bild speichern",
                                           filter = "*.png")
        self.pixmap.save(filename)
        
    def load (self):
        filename, _ = QFileDialog.getOpenFileName(self, "Bild laden", "*.png")
        if filename:
            self.filename = filename
            #self.paint()


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
            #self.paint()

    def selectColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color
            #self.paint()

    def selectFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font = font
            #self.paint()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())



































