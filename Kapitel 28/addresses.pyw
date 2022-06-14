#! /use/bin/env python3

#----------------------------------------------------
# Dateiname:  addresses.pyw
# Test Layout mit Policies
#
# Python 3,  mitp Verlag
# Kap. 28
# Michael Weigend 08. 06. 2019
#----------------------------------------------------
# addresses.py
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QFormLayout, 
          QPushButton, QTextEdit, QLineEdit, QWidget)

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.editName = QLineEdit(self)
        self.editEMail =  QLineEdit(self)
        self.editAddress = QTextEdit(self)         

        # Layout
        form = QFormLayout()
        form.addRow("Name:", self.editName)
        form.addRow("E-Mail:", self.editEMail)
        form.addRow("Adresse:", self.editAddress)
        self.setLayout(form)

        #Policies
        form.setFieldGrowthPolicy(
           QFormLayout.FieldsStayAtSizeHint)
        form.setLabelAlignment(QtCore.Qt.AlignRight)

app = QApplication(sys.argv)
book = AddressBook()
book.show()
sys.exit(app.exec_())
