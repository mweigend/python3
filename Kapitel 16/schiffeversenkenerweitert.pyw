#----------------------------------------------------
# Dateiname: schiffeversenkenerweitert.pyw
# Schifferversenken mit Punktwertung und
# Schaltfläche für neues Spiel
# Python 3, mitp Verlag
# Kap. 16
# Michael Weigend 5.6.2019
#----------------------------------------------------
from tkinter import *
from random import *
class Feld(object):
  def __init__(self,spiel,x,y):
    self.x=x
    self.y=y
    self.spiel=spiel
    self.button=Button(self.spiel.fenster,
                       text='   ',command=self.press)
    self.button.grid(column=x, row=y)

  def press(self):

    if self.spiel.spielfeld.checkTreffer(self.x, self.y):
      self.button.config(bg='blue')
      self.spiel.punkte.aktualisiere(3)
      if self.spiel.spielfeld.alleVersenkt():
        self.spiel.punkte.aktualisiere(0)
    else:
      self.button.config(bg='white')
      self.spiel.punkte.aktualisiere(-1)
      
    

class Spielfeld(object):
  def __init__(self):
    self.d={}
    for i in range(12):
      for j in range(12):
        self.d[(i,j)]=0
    for i in range(4): self.setzeBoot(1)
    for i in range(3): self.setzeBoot(2)
    for i in range(2): self.setzeBoot(3)
    self.setzeBoot(4)

  def setzeBoot(self, laenge):
    # setzt an freie Position neues Schiff
    max=11-laenge
    ok=0
    while not ok:
      if choice([0,1]):
        # Schiff ist waagrecht
        y=randint(1,10)    # Rand bleibt frei
        x=randint(1,max)
        if self.check(x,y,x+laenge-1,y):
          for x in range(x,x+laenge):self.d[(x,y)]=1
          ok=1
      else: # Schiff ist senkrecht
        x=randint(1,10)
        y=randint(1,max)
        if self.check(x,y,x,y+laenge-1):
          for y in range(y,y+laenge):self.d[(x,y)]=1
          ok=1

  def check(self, x1, y1,x2,y2 ):
    # Liefert 1, falls der Bereich frei ist und 0 sonst 
    ok=1
    for x in range(x1-1,x2+2):
      for y in range (y1-1, y2+2):
        if self.d[x,y]: ok= 0
    return ok

  def checkTreffer(self, x, y):
    # Liefert 1, falls Treffer und None sonst
    # Falls getroffen, wird d[x,y] auf 0 gesetzt
    if self.d[x,y]:
      self.d[x,y]=0
      return 1

  def alleVersenkt(self):
     #liefert 1, wenn alle Schiffe versenkt und 0 sonst
     test=1
     for feld in self.d.keys():
       if self.d[feld]:
         test=0
         break
     return test
 
class Punkte(object):
  def __init__(self, spiel):
     self.l=Label(master=spiel.fenster,text='0',
             font=('Arial',10))
     self.l.grid(column=0, row=12, 
                 columnspan=7)

  def aktualisiere(self,p):
    punkte=int(self.l.cget('text'))
    if p==0:
      self.l.config(text='Fertig! '+str(punkte)+' Punkte')
    else:
      self.l.config(text=str(punkte+p))
             
class  NeuButton(object):
  def __init__(self, spiel):
     self.spiel=spiel
     self.b=Button(spiel.fenster, text='Neues Spiel',
                   font=('Arial',10),
                   command=self.neu)
     self.b.grid(column=7, row=12, 
                 columnspan=5)

  def neu(self):
    self.spiel.spielfeld=Spielfeld()
    for x in range(12):
      for y in range(12):
        button=Feld(self.spiel, x, y)
    self.spiel.punkte.l.config(text='0')
                  
class Schiffeversenken(object):
  def __init__ (self):
    self.fenster=Tk()
    self.spielfeld=Spielfeld()
    for x in range(12):
      for y in range(12):
        button=Feld(self, x, y)
    self.punkte=Punkte(self)
    self.neu=NeuButton(self)
    self.fenster.mainloop()
        
spiel=Schiffeversenken()                      
