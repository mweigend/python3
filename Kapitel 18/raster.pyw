#----------------------------------------------------
# Dateiname:  raster.pyw
# Einfacher Editor zur Erstellung eines Rasters aus
# unterschiedlich gefaerbten Quadraten
# Python 3
# Kap. 18 
# Michael Weigend 7.10.09
#----------------------------------------------------

from tkinter import *
class Raster(object):
  def __init__(self):
    liste = [(x,y) for x in range(10) for y in range(10)]
    self.fenster = Tk()
    for (i,j) in liste:
      l=Label(self.fenster, width=2, height=1,
                bg='white')                         #1
      l.grid(column=i, row=j)                       #2
      l.bind(sequence='<Button-1>', 
             func=self.linksklick)                  #3
      l.bind(sequence='<Button-3>', 
             func=self.rechtsklick)
      l.bind(sequence='<Double-Button-1>',
             func=self.doppelklick)
    self.fenster.mainloop()

  def linksklick(self, event):
      event.widget.config(bg='black')               #4

  def rechtsklick(self, event):
      event.widget.config(bg='grey')

  def doppelklick(self, event):
      event.widget.config(bg='white')

r = Raster()




                    
