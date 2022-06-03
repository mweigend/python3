#----------------------------------------------------
# Dateiname:  meteore2.pyw
# Ein Raumschiff muss an Meteoren vorbei gesteuert werden
# und mitten auf dem rechten großen Meteor landen.
# Python 3  mitp Verlag
# Kap. 20
# Michael Weigend 5.6.2019
#----------------------------------------------------

from tkinter import *
from threading import *
from time import *
from random import *

class Weltraum(object):
  def __init__(self):
    self.fenster = Tk()
    self.canvas = Canvas(self.fenster, width=350,
                         height=250, bg='black')      #1
    self.canvas.pack()
    self.addSteine()                                  #2
    self.addAsteroid()
    self.schiff = Schiff('schiff.gif',
                         self, 50, 150)               #3
    self.fenster.bind(sequence='<Any-KeyPress>',
                          func=self.schiff.steuere)   #4
    self.schiff.start()                               #5
    self.fenster.mainloop() 

  def addAsteroid(self):
    self.astx, self.asty = 300,100                    #6
    self.astbild = PhotoImage(
                file='metgross.gif')
    self.asteroid = self.canvas.create_image(
           self.astx, self.asty, image=self.astbild)  #7

  def addSteine(self):
    self.steinbild=PhotoImage(
                  file='metklein.gif')
    self.steine = []                                  #8
    for i in range(7):    
      id=self.canvas.create_image(
                    randint(100,220), randint(-10,270),
                    image=self.steinbild)             #9         
      self.steine.append(id)

  def kollision (self, schiff):
    x, y = schiff.x, schiff.y
    for id in self.steine:                           #10
      try:
        if id in self.canvas.find_overlapping(x-20, y-5, x+0, y+5):
          return True
      except:
        pass
    return False

  def gelandet(self):                                #11
    return (self.astx-10 < self.schiff.x < self.astx+10) and \
           (self.asty-10 < self.schiff.y < self.asty+10) and \
           (-2 <= self.schiff.vx < 2) and \
           (-2 <= self.schiff.vy < 2) 

class Schiff (Thread):
  def __init__(self, bilddatei, weltraum, x, y):
    Thread.__init__(self)
    self.c = weltraum.canvas
    self.w = weltraum
    self.x, self.y = x, y                            #12
    self.vx = self.vy = 0                            #13
    self.bild = PhotoImage(file=bilddatei)
    self.id=self.c.create_image(x,y,image=self.bild) #14

  def run(self):                                     #15
    while not self.w.kollision(self):
        sleep(0.1) 
        self.x += self.vx                            #16
        self.y += self.vy
        self.c.move(self.id, self.vx, self.vy)       #17
        if self.w.gelandet():                        #18
            self.c.create_text(100, 50,
                      text = 'Gewonnen!',
                      font =('Arial', 20), fill='white')
            break
    else:
        self.c.create_text(100, 50, text='Verloren!',
                       font=('Arial', 20), fill='white')

  def steuere(self, event):                          #19             
    if   event.keysym_num == 65362: self.vy-=0.5   # Up
    elif event.keysym_num == 65364: self.vy+=0.5   # Down
    elif event.keysym_num == 65363: self.vx+=0.5   # Right
    elif event.keysym_num == 65361: self.vx-=0.5   # Left

w=Weltraum()











                    
