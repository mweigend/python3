#----------------------------------------------------
# Dateiname:  gemini.pyw
# Simulation des Kopplungsmanoevers von Gemini 6 und
# Gemini 7. Für jedes relevante Tastaturereignis (Taste gedrückt)
# wird ein eigener Event-Handler definiert.
#
# Python 3, mitp Verlag
# Kap. 18
# Michael Weigend 5.6.2019
#----------------------------------------------------


from tkinter import *

class Spielflaeche(object):
  def __init__(self):
    self.fenster = Tk()
    self.canvas = Canvas(self.fenster, 
                         width='10c', height='5c')    #1
    self.canvas.pack()                               
    h = PhotoImage(file='erde.gif')
    self.canvas.create_image(0,0,anchor=NW, image=h)  #2
    g7 = PhotoImage( file='gemini7d.gif')
    self.gemini7 = self.canvas.create_image(
                                   50,50,image=g7)    #3
    g6 = PhotoImage(file='gemini6.gif')
    self.canvas.create_image(300,30,image=g6)         #4
    self.fenster.bind('<KeyPress-Down>',self.runter)  #5
    self.fenster.bind('<KeyPress-Up>', self.rauf)
    self.fenster.bind('<KeyPress-Left>', self.links)
    self.fenster.bind('<KeyPress-Right>', self.rechts)
    self.fenster.mainloop() 

  def rauf(self, event):                               #6
    self.canvas.move(self.gemini7, 0, -3)           #7

  def runter(self, event):
    self.canvas.move(self.gemini7, 0, +3)

  def links(self, event):
    self.canvas.move(self.gemini7, -3, 0)

  def rechts(self, event):
    self.canvas.move(self.gemini7, 3, 0)

s = Spielflaeche()




                    
