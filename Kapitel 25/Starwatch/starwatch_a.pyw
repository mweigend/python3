#!/usr/bin/env python3
#----------------------------------------------------
# Dateiname:  starwatch_a.pyw
# Sterne zählen - verbesserte Version
# importiert das Modul stars_a
# 
# Python 3
# Kap. 25
# Michael Weigend 08.06.2019
#----------------------------------------------------
 
from tkinter import *
from stars_a import *                                   #1
from tkinter import filedialog

DEFAULT_PATH = "bilder/wagen.gif"

class Starwatch(object): 
  def __init__ (self):
    self.__createWidgets()  
    self.sky = Sky(self.image)                        #2
    self.__layout()     
    self.window.mainloop()

  def __createWidgets(self):
    self.window = Tk()
    self.window.title("Sterne z\xe4hlen")
    self.image = PhotoImage(file=DEFAULT_PATH)
    self.canvas = Canvas(master=self.window,
                      width="9c", height="5c")
    self.imageID = self.canvas.create_image(0, 0,
                      image = self.image, anchor=NW)
    self.buttonLoad = Button(master=self.window,
                             text="Laden",
                             command=self.load)
    self.buttonCount = Button(master=self.window,
                             text="Z\xe4hlen",
                             command=self.count)
    self.labelCount=Label(master=self.window, width=4,
                           fg="blue")

  def __layout(self):
    self.canvas.pack()
    self.buttonLoad.pack(side=LEFT)
    self.buttonCount.pack(side=LEFT)
    Label(master = self.window,
          text="Gez\xe4hlte Sterne:").pack(side=LEFT)
    self.labelCount.pack(side=LEFT)

  def load (self):
    path = filedialog.askopenfilename()               #3
    if path:
        self.image = PhotoImage(file=path)            #4
        self.canvas.itemconfigure(self.imageID,
                                    image=self.image)
        self.sky = Sky(self.image)
        self.window.mainloop()                        #5

  def count (self): 
    number = str(self.sky.count())                    #6          
    self.labelCount.config(text=number)               #7

sw = Starwatch()

