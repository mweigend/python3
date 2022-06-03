#----------------------------------------------------
# Dateiname: kreuze.pyw
# Demo fuer Tkinter.PhotoImage
# Objektorientierte Programmierung mit Python
# Kap. 17.2.1
# Michael Weigend 7.10.09
#----------------------------------------------------
from tkinter import *

class Bild(object):  
  def __init__ (self):   
    self.fenster = Tk()
    self.bild = PhotoImage(width=50, height=50)
    Label(master=self.fenster, image=self.bild).pack()
    Label(master=self.fenster, image=self.bild).pack()
    self.bild.put("#ff0000", (20,10, 30, 40))
    self.bild.put("#ff0000", (10,20, 40, 30))
    self.fenster.mainloop()
         
b = Bild()
