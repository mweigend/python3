#----------------------------------------------------
# Dateiname: farbmischer.pyw
#
# Python 3, mitp Verlag
# Kap. 15
# Michael Weigend 5.6.2019
#----------------------------------------------------
 
from tkinter import *

class Farbmischer(object):
  def __init__(self):
    self.fenster = Tk()
    self.rot, self.gruen, self.blau=IntVar(), IntVar(), IntVar() #1
    self.check = []                                  #2
    for (farbe, var) in [('rot',self.rot), 
                         ('gr\xfcn',self.gruen),
                         ('blau',self.blau)]:
        self.check.append(Checkbutton(self.fenster,
                          text=farbe,
                          offvalue=0, onvalue=255,
                          variable=var,
                          command=self.mix))
    self.farbfeld = Label(self.fenster,width=20, height=6)
    self.farbfeld.pack(side=LEFT)                    #3
    for button in self.check:
        button.pack(side=RIGHT)
    self.fenster.mainloop()

  def mix(self):                                     #4
      summe='#'
      for farbe in (self.rot, self.gruen, self.blau):
          summe += str(hex(farbe.get())).lstrip('0x').zfill(2)
      self.farbfeld.config(bg=summe)                 #5

farbmischer = Farbmischer()



 



