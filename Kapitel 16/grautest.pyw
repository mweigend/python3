#----------------------------------------------------
# Dateiname: grautest.pyw
# Psychologisches Experiment zur Wahrnehmung
# Python 3, mitp Verlag
# Kap. 16, Lösung 1
# Michael Weigend 5.6.2019
#----------------------------------------------------

from tkinter import *
from random import *
class Grautest:
  def __init__(self):
    self.fenster = Tk()
    self.linksGrau = Frame(self.fenster, width=20, height=120)       
    self.rechtsGrau = Frame(self.fenster, width=20, height=120)
    self.ausgabe=Label(self.fenster, width=20, height=2)
    self.pruefButton=Button(self.fenster, text='check',
                            command=self.pruefe)
    self.scale=Scale(self.fenster, orient=HORIZONTAL, 
                     label='Helligkeit', to=255,
                     showvalue=0, length=200,
                     command=self.aktualisiere)       #1
    self.layout()
    self.neu()
    self.fenster.mainloop()

  def layout(self):
    self.linksGrau.pack(side=LEFT)
    self.rechtsGrau.pack(side=RIGHT)
    self.scale.pack()
    self.ausgabe.pack(side=BOTTOM)
    self.pruefButton.pack(side=BOTTOM)

  def neu(self):
    ziffern = '0123456789ABCDEF'
    farbwert = choice(ziffern)+choice(ziffern)        #2
    grau = '#' + 3*farbwert                           #3
    self.linksGrau.config(bg=grau)

  def aktualisiere(self, event):
    nr = hex(self.scale.get())                        #4
    farbwert = str(nr).lstrip('0x').zfill(2)          #5
    grauton = '#' + 3*farbwert
    self.rechtsGrau.config(bg=grauton)

  def loesche(self):
    self.ausgabe.config(text='')

  def pruefe(self):
    links = self.linksGrau.cget('bg')
    rechts = self.rechtsGrau.cget('bg')
    if rechts == links:
      self.ausgabe.config(text='Gleiche Helligkeit!')
    elif links < rechts:
      self.ausgabe.config(text='Zu hell!')
    else:
      self.ausgabe.config(text='Zu dunkel!')
    self.ausgabe.after(1000, self.loesche)          #6
    self.linksGrau.after(1000, self.neu)

grautest = Grautest()



