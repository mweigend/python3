#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  browser_filter.pyw
# Browser mit Filter
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

HINT = """<html><body bgcolor="orange">
             <h1>Sorry...</h1>
             Diese Seite ist nicht erlaubt.
          </body> </html>"""

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.whiteList = ["www.wikipedia.de",
                          "de.wikipedia.org",
                          "www.planet-wissen.de"]
                        
        self.createWidgets()                           #1
        self.createLayout()
        self.createConnections()
        self.stopped = False
        self.show()

    def search(self):
        # Zeige Webseite
        self.stopped = False
        address = str(self.addressBar.text())          #2
        if address:                                    #3
            if "://" not in address:
                address = "http://" + address          #4
            url = QUrl(address)                        #5
            self.webView.load(url)

    def createWidgets(self):
        self.setWindowTitle("Welt-Browser")            #7
        self.setWindowIcon(QIcon("welt.png"))          #8
        self.webView = QWebEngineView(self)            #9
        self.addressBar = QLineEdit(self)              #10
        self.searchButton = QPushButton("Suchen", self)#11

    def checkUrl(self):                               #4
        if not self.stopped:                          #5
            url = str(self.webView.url().toString())
            if not any([x in url for x in self.whiteList]): #6
                self.stopped = True
                self.webView.stop()
                self.webView.setHtml(HINT)
          

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
        self.webView.urlChanged.connect(self.checkUrl)
        

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
