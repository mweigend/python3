#----------------------------------------------------
# Dateiname:  gemini1.pyw
# Gemini - Variante mit einem einzigen Eventhandler,
# der alle Tastaturereignisse bearbeitet.
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
    self.fenster.bind(sequence='<Any-KeyPress>',
                      func=self.bewege)           #1
    self.fenster.mainloop()   


  def bewege(self,event):
    if event.keysym_num == 65362:                #Up
       self.canvas.move(self.gemini7, 0, -3)
    elif event.keysym_num == 65364:              #Down
       self.canvas.move(self.gemini7, 0, 3)
    elif event.keysym_num == 65363:              #Right
       self.canvas.move(self.gemini7, 3, 0)
    elif event.keysym_num == 65361:              #Left
       self.canvas.move(self.gemini7, -3, 0)


s = Spielflaeche()




                    
