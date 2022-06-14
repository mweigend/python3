#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  pizza_order.pyw
# Eine Anwendung mit Schaltfächen und Checkboxen zum
# Bestellen einer Pizza
#
# Python 3,  mitp Verlag
# Kap. 28
# Michael Weigend 11. 06. 2019
#----------------------------------------------------
# pizza_order.py
import sys, random
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QLabel, 
                             QTextEdit, QWidget, QRadioButton,
                             QButtonGroup, QCheckBox)

ORDER = "Die Pizza kostet {:.2f} €."

class Order(QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.label = QLabel()                                     #1                            
        self.rbBig = QRadioButton("Groß")                         #2     
        self.rbBig.setChecked(True)                               
        self.rbSmall = QRadioButton("Klein")
        self.sizeButtons = QButtonGroup()                         #3  
        self.sizeButtons.addButton(self.rbBig)           
        self.sizeButtons.addButton(self.rbSmall)
        self.cbTomatos = QCheckBox("Tomaten")                     #4
        self.cbCheese = QCheckBox("Käse")
        self.cbSalami = QCheckBox("Salami")
                                   
        # Layout
        vBox = QVBoxLayout()                                      #5
        self.setLayout(vBox)
        vBox.addWidget(self.rbBig)
        vBox.addWidget(self.rbSmall)
        vBox.addWidget(self.cbTomatos)
        vBox.addWidget(self.cbCheese)
        vBox.addWidget(self.cbSalami)
        vBox.addWidget(self.label)

        # Connections
        for element in (self.rbBig, self.rbSmall,
                self.cbTomatos, self.cbCheese, self.cbSalami):
            element.clicked.connect(self.calculate)               #6

        self.setWindowTitle("Pizza-Bestellung")
        self.show()
        self.calculate()

    def calculate(self):
        size = self.sizeButtons.checkedButton().text()
        if size == "Groß":                                        #7
            price = 3.0
        else:
            price = 2.0
        if self.cbTomatos.isChecked():                            #8
            price += 1
        if self.cbCheese.isChecked():
            price += 1.5
        if self.cbSalami.isChecked():
            price += 1.5
            
        self.label.setText(ORDER.format(price))

app = QApplication(sys.argv)
order = Order()
sys.exit(app.exec_())
