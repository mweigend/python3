#----------------------------------------------------
# Dateiname:  rasterspeichern.pyw
# Grafischer Editor für Raster mit Menue für Laden und Speichern
# Objektorientierte Programmierung mit Python
# Kap. 19 Lösung 1
# Michael Weigend 8.10.09
#----------------------------------------------------

from tkinter import *
from tkinter import filedialog
import pickle

class Raster(object):
  def __init__(self):
    liste = [(x, y) for x in range(10) for y in range(10)]
    self.fenster = Tk()
    self.d = {}                                      #1
    for (i, j) in liste:
      l = Label(self.fenster, width=2, height=1,
              bg='white')
      l.grid(column=i, row=j)
      l.bind(sequence='<Button-1>',
             func=self.linksklick)
      l.bind(sequence='<Button-3>',
             func=self.rechtsklick)
      l.bind(sequence='<Double-Button-1>',
                       func=self.doppelklick)
      self.d[(i,j)]=l                                #2 
    self.addMenueleiste()
    self.addDateimenue()
    self.fenster.mainloop()

  def linksklick(self, event):
      event.widget.config(bg='black')

  def rechtsklick(self, event):
      event.widget.config(bg='grey')

  def doppelklick(self, event):
      event.widget.config(bg='white')

  def addMenueleiste(self):
    self.menueleiste = Menu(self.fenster)
    self.fenster.configure (menu=self.menueleiste)

  def addDateimenue(self):
    self.dateimenue = Menu(self.menueleiste)
    self.dateimenue.add_command(label='Laden',
                               command=self.laden)     
    self.dateimenue.add_command(label='Speichern unter',
                               command=self.speichern)
    self.menueleiste.add_cascade(label='Datei',
                            menu=self.dateimenue) 

 
  def speichern (self):
    pfad = filedialog.asksaveasfilename()
    if pfad:
      dfarben={}                                     #3
      for x in self.d.keys():
          dfarben[x] = self.d[x].cget('bg')
      f = open(pfad, "wb")     # schreiben im Binärmodus
      pickle.dump(dfarben, f)                        #4
      f.close()

  def laden (self):
    pfad = filedialog.askopenfilename()
    if pfad:
      f = open(pfad, "rb")           # lesen im Binärmodus
      dfarben = pickle.load(f)                       #5
      f.close()
      for x in self.d.keys():
          self.d[x].config(bg=dfarben[x])            #6


r = Raster()







                    
