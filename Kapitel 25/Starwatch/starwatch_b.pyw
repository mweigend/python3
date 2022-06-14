#!/usr/bin/env python3
#----------------------------------------------------
# Dateiname:  starwatch_b.pyw
# Sterne zählen
# importiert das Modul stars_b
# Lösung Aufgabe 3
# 
# Python 3
# Kap. 25
# Michael Weigend 08.06.2022
#----------------------------------------------------
from tkinter import *
from stars_b import *
from tkinter import filedialog

DEFAULT_PATH = "bilder/wagen.gif"

class Starwatch(object):  
  def __init__ (self):         
    self.r = 5              # Radius des Markierungskreises
    self.markID = None      # ID Markierung auf dem Canvas
    self.__createWidgets() 
    self.__layout()
    self.sky = Sky(self.image)
    self.window.mainloop()
        
  def __createWidgets(self):
    self.window = Tk()
    self.window.title("Sterne z\xe4hlen")

    self.image = PhotoImage(file=DEFAULT_PATH)
    self.canvas = Canvas(master=self.window,
                      width="9c", height="5c")
    self.imageID = self.canvas.create_image(0, 0,
                      image = self.image, anchor=NW)
    self.canvas.bind(sequence="<Button-1>",
                       func=self.markStar)
    self.buttonLoad = Button(master=self.window,
                             text="Laden",
                             command=self.load)
    self.buttonCount = Button(master=self.window,
                             text="Zählen",
                             command=self.count)
    self.labelCount=Label(master=self.window, width=4,
                           fg="blue")
    self.labelBrightness=Label(master=self.window,
                               width=5, fg="blue")
  def __layout(self):
    self.canvas.pack()
    self.buttonLoad.pack(side=LEFT)
    self.buttonCount.pack(side=LEFT)
    Label(master = self.window,
          text="Gezählte Sterne:").pack(side=LEFT)
    self.labelCount.pack(side=LEFT)
    Label(master = self.window,
          text="Helligkeit:").pack(side=LEFT)
    self.labelBrightness.pack(side=LEFT)
        
        
  def load (self):
    path = filedialog.askopenfilename()
    if path:
        self.image= PhotoImage(file=path)
        self.canvas.itemconfigure(self.imageID,
                                    image=self.image)
        self.sky = Sky(self.image)
        self.window.mainloop()

  def count (self):    
    number = str(self.sky.count())
    self.labelCount.config(text=number)

  def markStar(self, event):
    position = (event.x, event.y)
    x0, y0 = event.x - self.r, event.y - self.r
    x1, y1 = event.x + self.r, event.y + self.r
    self.canvas.delete(self.markID)
    self.markID = self.canvas.create_oval(x0, y0, x1, y1,
                                        outline="yellow")
    star=self.sky.getStar(position)
    if star:
        brightness=str(star.getBrightness())
        self.labelBrightness.config(text=brightness)
    else:  self.labelBrightness.config(text="---")
                          
sw = Starwatch()
