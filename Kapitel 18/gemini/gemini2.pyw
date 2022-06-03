#----------------------------------------------------
# Dateiname:  gemini2.pyw
# Gemini - Variante mit Treffermeldung
# Python 3, mitp Verlag
# Kap. 18, Lösung 2
# Michael Weigend 5.6.2019
#----------------------------------------------------

from tkinter import *

class Spielflaeche(object):
  def __init__(self):
    self.fenster = Tk()
    self.canvas = Canvas(self.fenster, 
                         width='10c', height='5c')     
    self.canvas.pack()                               
    h = PhotoImage(file='erde.gif')
    self.canvas.create_image(0,0,anchor=NW, image=h)   
    g7 = PhotoImage(file='gemini7d.gif')
    self.gemini7 = self.canvas.create_image(
                                   50,50,image=g7)     
    g6 = PhotoImage(file='gemini6.gif')
    self.canvas.create_image(300,30,image=g6)          
    self.fenster.bind(sequence='<Any-KeyPress>',
                      func=self.bewege)                
    self.fenster.mainloop()   


  def bewege(self,event):
    if event.keysym_num == 65362:              #Up
       self.canvas.move(self.gemini7, 0, -3)
    elif event.keysym_num == 65364:            #Down
       self.canvas.move(self.gemini7, 0, 3)
    elif event.keysym_num == 65363:            #Right
       self.canvas.move(self.gemini7, 3, 0)
    elif event.keysym_num == 65361:            #Left
       self.canvas.move(self.gemini7, -3, 0)
    x, y = tuple(self.canvas.coords(self.gemini7))
    if 250 < x < 260 and 28 < y < 32:                 #1
      self.canvas.create_text(120,40,
                  text='Rendezvous gelungen!',
                  font=('Arial', 16), fill='white')   #2



s = Spielflaeche()




                    
