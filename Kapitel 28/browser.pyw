#! /usr/bin/env python3

#----------------------------------------------------
# Dateiname:  browser.pyw 
# Ein einfacher Webbrowser.
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
        self.createWidgets()                           #1
        self.createLayout()
        self.createConnections()
        self.show()                                   

    def search(self):
        # Zeige Webseite
        address = str(self.addressBar.text())          #2
        if address:                                    #3
            if "://" not in address:
                address = "http://" + address          #4
            url = QUrl(address)                        #5
            self.webView.load(url)                     #6

    def createWidgets(self):
        self.setWindowTitle("Welt-Browser")            #7
        self.setWindowIcon(QIcon("welt.png"))          #8
        self.webView = QWebEngineView(self)            #9
        self.addressBar = QLineEdit(self)              #10
        self.searchButton = QPushButton("Suchen", self)#11


    def createLayout(self):
        hbl = QHBoxLayout()                            #12
        hbl.addWidget(self.addressBar)                
        hbl.addWidget(self.searchButton)
        vbl = QVBoxLayout()                            #13
        vbl.addLayout(hbl)
        vbl.addWidget(self.webView)
        self.setLayout(vbl)                            #14

    def createConnections(self):                       #15
        self.addressBar.returnPressed.connect(self.search)
        self.searchButton.clicked.connect(self.search)
        

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
