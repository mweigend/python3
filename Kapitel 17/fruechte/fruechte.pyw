#----------------------------------------------------
# Dateiname: fruechte.pyw
# Buttons mit Fotos, die Fruechte darstellen
# Python 3  mitp Verlag
# Kap. 17
# Michael Weigend 5.6.2019
#----------------------------------------------------

from tkinter import *
class Fruechte(object):
  def __init__(self):
    self.fenster = Tk()
    self.zitrone = PhotoImage(
              file='zitrone1.gif')   #1
    self.banane = PhotoImage(
              file='banane1.gif')
    Button(self.fenster, image=self.zitrone,
      command=self.__schreibeZitrone).pack(side=LEFT) #2
    Button(self.fenster, image=self.banane,
      command=self.__schreibeBanane).pack(side=LEFT)
    self.ausgabe=Label(self.fenster,
                       font=('Arial', 14), width=20)
    self.ausgabe.pack(side=RIGHT)   
    self.fenster.mainloop()

  def __schreibeZitrone (self):
      self.ausgabe.config(text='Zitrone')
  def __schreibeBanane (self):
      self.ausgabe.config(text='Banane')

f = Fruechte()

                    
