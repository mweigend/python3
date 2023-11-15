#----------------------------------------------------
# Dateiname:  digitaluhr.pyw
# Python 3  mitp Verlag
# Kap. 20
# Michael Weigend 7.6.2019
#----------------------------------------------------
from tkinter import *
from time import *
import _thread


class Uhr(object):
  def __init__(self):
    self.fenster = Tk()
    self.zeit = StringVar()                           #1
    self.anzeige = Label(self.fenster,
                         textvariable=self.zeit,
                         font=('Arial', 20))          #2
    self.anzeige.pack()
    _thread.start_new_thread(self.aktualisieren, ())  #3
    self.fenster.mainloop()

  def aktualisieren (self):
    while True:
      self.zeit.set(strftime('%X'))                   #4
      sleep(1)                                        #5
      

uhr = Uhr()










                    
