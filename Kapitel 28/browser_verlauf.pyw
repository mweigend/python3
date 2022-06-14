#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  browser_verlauf.pyw
# Browser, der den Verlauf einer Sitzung anzeigemn kann.
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

HISTORY_PATTERN = """
<html><body bgcolor="#C0C0FF">
   <h1>Verlauf</h1>
   {}
</body></html>"""

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.createWidgets()                            
        self.createLayout()
        self.createConnections()
        self.show()                                   

    def search(self):
        # Zeige Webseite
        address = str(self.addressBar.text())           
        if address:                                     
            if "://" not in address:
                address = "http://" + address          
            url = QUrl(address)                         
            self.webView.load(url)                      
    

    def showHistory(self):
        history = self.webView.history().items()
        htmlHistory=""
        for i in history:
            htmlHistory += '<a href="{}"> {} </a><br/>'.format(
                              i.url().toString(), i.title())
        self.webView.setHtml(HISTORY_PATTERN. format(htmlHistory))

    def createWidgets(self):
        self.setWindowTitle("Welt-Browser")             
        self.setWindowIcon(QIcon("welt.png"))           
        self.webView = QWebEngineView(self)                    
        self.addressBar = QLineEdit(self)               
        self.searchButton = QPushButton("Suchen", self) 
        self.historyButton = QPushButton("Verlauf", self)
        


    def createLayout(self):
        hbl = QHBoxLayout()                             
        hbl.addWidget(self.addressBar)                
        hbl.addWidget(self.searchButton)
        hbl.addWidget(self.historyButton)
        vbl = QVBoxLayout()                          
        vbl.addLayout(hbl)
        vbl.addWidget(self.webView)
        self.setLayout(vbl)                             

    def createConnections(self):                        
        self.addressBar.returnPressed.connect(self.search)
        self.searchButton.clicked.connect(self.search)
        self.historyButton.clicked.connect(self.showHistory)
        

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
