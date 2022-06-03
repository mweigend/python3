#----------------------------------------------------
# Dateiname: mandelbrot.pyw
# Visualisierung der Mandelbrot-Menge
# Objektorientierte Programmierung mit Python
# Kap. 17.2
# Michael Weigend 2.10.09
#----------------------------------------------------
from tkinter import *
RADIUS = 2.0
ZOOM = 50.0
class Mandelbrot(object):
  def __init__(self):
    self.fenster = Tk()
    self.bild = PhotoImage(width=200, height=200)
    self.bildflaeche = Label(master=self.fenster,
                      image=self.bild)
    self.bildflaeche.pack()
    self.__zeichnen()
    self.fenster.mainloop()

  def __zeichnen(self):
    intervall = [x/ZOOM for x in range(-100, 100)]
    mandelbrot = ((x, y) for x in intervall
                              for y in intervall
                              if self.__test(x, y))
    for  x, y in mandelbrot:
      self.bild.put("#0000ff", (int(ZOOM*x+100), int(ZOOM*y+100)))   
               
  def __test (self, x, y):
    c = x + 1j * y
    z = 0
    for i in range(20):
      if abs (z)< RADIUS:
          z = z*z - c
      else: return False # nicht Element der Mandelbrot-Menge
    return True 

m = Mandelbrot()           
        
