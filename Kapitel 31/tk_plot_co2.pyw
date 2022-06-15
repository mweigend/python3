#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  tk_plot_co2.py
# CO2-Messwerte werden eingegeben und im Diagramm angezeigt.
#
# Python 3,  mitp Verlag
# Kap. 31
# Michael Weigend 11. 06. 2022
#----------------------------------------------------
import matplotlib
matplotlib.use('TkAgg')                               #1
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
from tkinter import Tk, Label, Button, Entry, LEFT, BOTH
from time import time

class Plotter:                                        #2
    def __init__(self):     
        self.f = Figure(figsize=(5,4), dpi=100)       #3
        self.a = self.f.add_subplot(111)              #4
        self.a.set_ylim(0, 3000)                      #5
        self.a.set_xlim(0, 30)
        self.a.grid(b=True)                           #6
        self.t_vector = []                            #7
        self.c_vector = []                            #8
        self.start = time()                           #9
        # Widgets
        self.window = Tk()
        self.canvas = FigureCanvasTkAgg(self.f,
                             master=self.window)     #10
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=BOTH,
                                        expand=True) #11
        self.toolbar = NavigationToolbar2Tk(
                          self.canvas, self.window)  #12                                                    
        self.label_c = Label(master=self.window,
                         text=" Kohlendioxid (ppm):")
        self.label_c.pack(side=LEFT)
        self.entry_c = Entry(master=self.window, width=4)
        self.entry_c.pack(side=LEFT)
        self.button = Button(master=self.window, text='Ok',
                             command=self.new_value)
        self.button.pack(side=LEFT)
        self.window.mainloop()

    def new_value(self):                             #13
        c = float(self.entry_c.get())
        t = (time()-self.start)/60                   #14
        self.t_vector.append(t)                      #15
        self.c_vector.append(c)
        self.a.plot(self.t_vector,self.c_vector,"-b.")
        self.canvas.draw()
Plotter()                                            
