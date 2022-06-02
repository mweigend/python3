#----------------------------------------------------
# Dateiname: catclient.py
# Client-Programm fuer XML-basierte Kommunikation
# mit einem Server, der eine Webseite mit einem
# Katalog für ein Online-Shop pflegt
#
# Python 3
# Kap. 26 
# Michael Weigend 19.8.2016
#----------------------------------------------------
from tkinter import *
from xml.dom import minidom                           #1
import urllib.request 

URL = "http://localhost:8000/cgi-bin/catserver.py"    #2 
class NewItem (object):
  def __init__ (self, group, ID, price, text):
    start = """<?xml version="1.0" ?>
            <neu></neu>"""                            #3
    self.doc = minidom.parseString(start)             
    neu = self.doc.documentElement
    neu.setAttribute("warengruppe", group)            
    item = self.doc.createElement("ware")             #4
    itemText = self.doc.createTextNode(text)
    item.setAttribute("id", ID)                       #5
    item.setAttribute("preis", price)
    item.appendChild(itemText)                        #6
    neu.appendChild(item)

  def send (self):
    f = urllib.request.urlopen(URL,
            bytes(self.doc.toxml(), encoding="utf-8"))                         #7
    response = f.read()
    f.close()
    return response

class GUI:
  def __init__(self):
    # Widgets definieren
    self.window = Tk();
    self.window.title("Vogelshop Client") 
    self.label1 = Label(self.window,
                        text="Neuer Artikel",
                        font=("Arial",14))
    self.buttonUpdate = Button(self.window, width=20,
                     text = "Katalog aktualisieren",
                     command = self.update)
    self.labelId = Label(self.window,
                         text="Bestellnummer: ")
    self.labelGroup = Label(self.window,
                            text="Warengruppe: ")
    self.labelPrice = Label(self.window, text="Preis: ")
    self.labelText = Label(self.window, text="Text: ") 
    self.text = Text(self.window, height=5, width=30, 
                     wrap=WORD)
    self.id = Entry (self.window, width=5)
    self.group = Entry (self.window, width=30)
    self.price = Entry (self.window, width=8)
    # Layout
    self.label1.grid(columnspan=2, column=0, row=0)
    self.labelId.grid(column=0, row=1, sticky=E)
    self.id.grid(column=1, row=1, sticky=W)
    self.labelGroup.grid(column=0, row=2, sticky=E)
    self.group.grid(column=1, row=2, sticky=W)
    self.labelPrice.grid(column=0, row=3, sticky=E)
    self.price.grid(column=1, row=3, sticky=W)
    self.labelText.grid(column=0, row=4,  sticky=NE)
    self.text.grid(column=1, row=4, padx=5, pady=5,
                   sticky=W)
    self.buttonUpdate.grid(columnspan=2, column=0,
                           row=5, pady=5)
    self.window.mainloop() 

  def update(self):                                   #8
    doc = NewItem(self.group.get(), self.id.get(),
                  self.price.get(), self.text.get(1.0, END))
    response = doc.send()                             #9
    self.text.insert(END,"\n\n"+response.decode("utf-8"))
     

GUI()

