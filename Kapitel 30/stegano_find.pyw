#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  stegano.py
# Ein Text, der in einem Bild versteckt ist,
# wird wiedergewonnen.
#
# Python 3,  mitp Verlag
# Kap. 30, Aufgabe 4
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

from tkinter import Tk, Label, Button, Text, filedialog, WORD, W, LEFT, END
from PIL import Image, ImageTk
import numpy as np
LETTERS = " abcdefghijklmnopqrstuvwxyzßäöü"

class App:
    def __init__(self):
        self.window = Tk()
        self.label = Label(self.window)
        self.label.pack()
        self.text = Text(self.window, width=50, height=5,
                         wrap=WORD)
        self.text.pack(anchor=W)
        self.loadButton=Button(master=self.window,
                               text="Bild laden und Text finden",
                               command=self.load)
        self.loadButton.pack(side=LEFT)
        self.original = Image.open("Thailand_2.png")
        w, h = self.original.size
        self.imgTk = ImageTk.PhotoImage(self.original)
        self.label.config(image=self.imgTk, width=w, height=h)
        self.window.mainloop()  

    def load(self):
        filename = filedialog.askopenfilename()
        if not filename:
            return
        img = Image.open(filename)
        a =  np.array(img)
        self.imgTk = ImageTk.PhotoImage(img)
        self.label.config(image=self.imgTk)
        a_o = np.array(self.original)
        if a.shape != a_o.shape:
            self.text.insert(END, "Bild passt nicht!")
            return
        green_o = a_o[:,:,1].clip(max=215)
        green = a[:,:,1]
        numbers = (green - green_o).ravel()
        self.text.delete(1.0, END)
        secret = ""
        for i in numbers:
            secret += LETTERS[i]
            if len(secret) > 3:
                if secret[-3:] == "   ":
                    self.text.insert(END, secret)
                    return
     
App()



