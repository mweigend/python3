#----------------------------------------------------
# Dateiname: taschenrechner.pyw
#
# Python 3, mitp Verlag
# Kap. 16
# Michael Weigend 5.6.2022
#----------------------------------------------------
 
from tkinter import *

class Taschenrechner(Tk):                           #1
  def __init__(self):
    Tk.__init__(self)                               #2
    self.ende = 0                                   #3
    self.display = Display(self)
    self.display.grid(column=0,row=0,sticky=E+W,
                      columnspan=6, pady=5)         #4
    tasten=[(0,1,'7'),(1,1,'8'),(2,1,'9'),(3,1,'//'),
            (0,2,'4'),(1,2,'5'),(2,2,'6'),(3,2,'*'),
            (0,3,'1'),(1,3,'2'),(2,3,'3'),(3,3,'-'),
            (0,4,'0'),(1,4,'%'),(3,4,'+')]
    for (i,j,zeichen) in tasten:  
       Taste(self,zeichen).grid(column=i,row=j)     #5
    Clear(self).grid(column=5,row=1)
    Gleich(self).grid(column=5,row=2)
    self.mainloop()

class Taste(Button):
  def __init__(self, fenster,aufschrift):
    Button.__init__(self,fenster,text=aufschrift,
                    command=self.drücken,width=3)
    self.aufschrift = aufschrift
    self.fenster = fenster

  def drücken(self):
    d = self.fenster.display
    if self.fenster.ende:                           #6
        d.delete(0,len(d.get()))
        self.fenster.ende=0
    d.anhängen(self.aufschrift)

class Clear(Button):
  def __init__(self, fenster):
    Button.__init__(self,fenster,text='C',
                    command=self.löschen,width=3)
    self.display=fenster.display

  def löschen(self):
    self.display.löschen()

class Gleich(Button):
  def __init__(self, fenster):
    Button.__init__(self,fenster,text='=',
                    command=self.rechnen,width=3)
    self.fenster = fenster

  def rechnen(self):
    ergebnis = eval(self.fenster.display.get())     #7
    ende = len(self.fenster.display.get())
    self.fenster.display.insert(ende, '='+str(ergebnis))
    self.fenster.ende = 1

class Display(Entry):
  def __init__(self,fenster):
    Entry.__init__(self, fenster,width=20)

  def anhängen (self,zeichen):
    self.insert(len(self.get()),zeichen)

  def löschen(self):
    self.delete(len(self.get())-1)                  #8

t = Taschenrechner()    



 



