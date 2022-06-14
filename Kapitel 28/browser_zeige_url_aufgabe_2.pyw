#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  browser_zeige_url_aufgabe_2.pyw
# Erweiterter Browser
#
# Python 3,  mitp Verlag
# Kap. 28
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        # Widgets
        self.setWindowTitle("Welt-Browser")             
        self.setWindowIcon(QIcon("welt.png"))           
        self.webView = QWebEngineView(self)                    
        self.addressBar = QLineEdit(self)               
        self.searchButton = QPushButton("Suchen", self)#1
        self.checkBox = QCheckBox("URL zeigen", self)
        self.checkBox.toggle()
        self.urlLabel = QLabel("", self)
        self.urlLabel.setMaximumWidth(400)

        # Layout
        hbl = QHBoxLayout()                            
        hbl.addWidget(self.addressBar)                
        hbl.addWidget(self.searchButton)
        hbl.addWidget(self.checkBox)
        vbl = QVBoxLayout()                            
        vbl.addLayout(hbl)
        vbl.addWidget(self.webView)
        vbl.addWidget(self.urlLabel)
        self.setLayout(vbl)                            

        # Connections                                  
        self.addressBar.returnPressed.connect(self.search)
        self.searchButton.clicked.connect(self.search)
        self.webView.urlChanged.connect (self.showUrl)
        self.checkBox.stateChanged.connect(self.changeVisibility)                        
        self.show()                                   

    def search(self):
        # Zeige Webseite
        address = str(self.addressBar.text())          
        if address:                                    
            if "://" not in address:
                address = "http://" + address          
            url = QUrl(address)                        
            self.webView.load(url)                     

    def changeVisibility(self):
        if self.checkBox.isChecked():
            self.urlLabel.show()
        else:
            self.urlLabel.hide()    

    def showUrl(self):
         url = self.webView.url().toString()
         self.urlLabel.setText(url)
                

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
