#----------------------------------------------------
# Dateiname:  destillation1.pyw
# Grafischer Editor fuer chemische Versuchsaufbauten
# Python 3, mitp Verlag
# Kap. 18, Lösung 4
# Michael Weigend 5.6.2019
#----------------------------------------------------

from tkinter import *
basis = 'bilder/'

class Labor(object):
  def __init__(self):
    self.fenster=Tk()
    self.c=Canvas(self.fenster, bg='white',
                       width='10c', height='8c')   
    self.c.pack()
    self.selektiert=None                              #1
    g=[]                                              #2
    l=[('2c','4c', PhotoImage(file=basis+'kolben.gif')),
       ('4c','4c', PhotoImage(file=basis+'erlenmeyer.gif')),
       ('8c', '4c', PhotoImage(file=basis+'kuehler.gif'))]
    for (x,y, bild) in l:
      g.append(self.c.create_image(x, y,image=bild))  #3
    self.fenster.bind('<ButtonRelease-1>',self.drop)  #4
    self.c.bind('<1>', self.drag)
    self.c.bind('<Motion>', self.bewege)
    self.fenster.mainloop()

  def drag(self, event):
    self.selektiert=self.c.find_closest(event.x, event.y)[0]                                           #5
    self.x, self.y= event.x, event.y                  #6

  def bewege(self, event):
    if self.selektiert:
      dx, dy=event.x-self.x, event.y-self.y           #7
      self.x, self.y=event.x, event.y
      self.c.move(self.selektiert, dx, dy)            #8

  def drop(self, event):
    self.selektiert=None

l=Labor()





                    
