#----------------------------------------------------
# Dateiname:  zaehler.pyw
# Zaähler mit Methode, die in eigenem Thread läuft
# Python 3  mitp Verlag
# Kap. 20
# Michael Weigend 7.6.2022
#----------------------------------------------------

from time import *
from tkinter import *
import _thread          
class Zähler:
    def __init__(self):
        self.f  = Tk()
        self.zahl = StringVar()
        Label(self.f, textvariable=self.zahl).pack()
        Button(self.f,command=self.zählenThread,
               text=' Los! ').pack()              #1
        self.f.mainloop()

    def zählenThread(self):
        _thread.start_new_thread(self.zählen,())  #2
      
    def zählen(self):
        for i in range(11):
            self.zahl.set(str(i))
            sleep(1)

Zähler()







                    
