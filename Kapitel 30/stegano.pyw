#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  stegano.py
# In einem Bild wird ein Text versteckt.
#
# Python 3,  mitp Verlag
# Kap. 30
# Michael Weigend 11. 06. 2019
#----------------------------------------------------
from tkinter import (filedialog, Tk, Label, Text,
                     Button, WORD, LEFT, W, END)
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
        self.saveButton=Button(master=self.window,
                               text="Datei speichern",
                               command=self.save)
        self.saveButton.pack(side=LEFT)
        self.hideButton=Button(master=self.window,
                               text="Text verstecken",
                               command=self.hide)
        self.hideButton.pack(side=LEFT)
        self.img = Image.open("Thailand_2.png")
        w, h = self.img.size
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.label.config(image=self.imgTk, width=w, height=h)
        self.window.mainloop()  

    def save(self):
        filename = filedialog.asksaveasfilename()
        if filename:
            self.img.save(filename)                

    def hide(self):
        a = np.array(self.img)
        b = a[:,:,1]
        b= b.clip(max=215)
        text = self.text.get(1.0, END).lower()
        numbers = np.array(self.encode(text))
        w, h = self.img.size
        numbers.resize(h, w)
        a[:,:,1] = b + numbers
        self.img = Image.fromarray(a)
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.label.config(image=self.imgTk)
       
    def encode(self, text):
        numbers = []
        for ch in text:
            try:
                numbers.append(LETTERS.index(ch))
            except:
                numbers.append(0)
        return numbers
 
App()



