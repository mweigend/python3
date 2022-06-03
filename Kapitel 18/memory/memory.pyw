#----------------------------------------------------
# Dateiname:  memory.pyw
# Memory-Spiel
# Python 3
# Kap. 18 Lösung 2
# Michael Weigend 7.10.07
#----------------------------------------------------

from tkinter import *
from random import *
basis=''

class Memory(object):
  def __init__(self):
    self.bilder=['kreis.gif', 'krone.gif', 'pfeil.gif', 'pilz.gif',
                 'quadrat.gif', 'dreieck.gif', 'mond.gif', 'raute.gif']                             #1
    self.fenster=Tk()
    self.neu()
    Button(self.fenster, text='Neu',
           command=self.neu).grid(column=3, row=4, pady=5)                                              #2
    self.fenster.mainloop()

  def neu(self):
    bilderliste=self.bilder[:]+self.bilder[:]        #3
    shuffle(bilderliste)
    self.offen=[]   # Liste aktiver offener Karten
    for x in range(4):
      for y in range(4):
        karte= Karte(basis+bilderliste.pop(), self)  #4
        karte.grid(column=x, row=y)                  #5

  def check(self, karte):
      if not self.offen:
          self.offen.append(karte)                   #6
      elif len(self.offen)==1:
          if self.offen[0].bilddatei==karte.bilddatei:
              self.offen=[]                          #7
          else: self.offen.append(karte)              
      else:
          for k in self.offen: k.verdecken()         #8
          self.offen=[karte]  

class Karte(Label):
  def __init__ (self, bild, spiel):
    self.rueck=PhotoImage(file=basis+'rueck.gif')    
    Label.__init__(self, spiel.fenster,
                   image=self.rueck)                 #9
    self.bild=PhotoImage(file=bild)
    self.bilddatei=bild
    self.verdeckt=True
    self.spiel=spiel
    self.bind(sequence='<1>', func=self.aufdecken)   #10

  def aufdecken(self, event):
    self.configure(image=self.bild)
    if self.verdeckt: self.spiel.check(self)         #11
    self.verdeckt=False

  def verdecken(self):
      self.configure(image=self.rueck)
      self.verdeckt=True

m=Memory()




                    
