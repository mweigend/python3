#----------------------------------------------------
# Dateiname: tk_test.pyw
# Einführungsbeispiel für ein Programm mit GUI
#
# Python 3, mitp Verlag
# Kap. 15
# Michael Weigend 5.6.2019
#----------------------------------------------------
def grüßen():
    fenster.label.config(text='Hallo!')               #1

from tkinter import *
fenster = Tk()
fenster.label= Label(fenster,text='Begrüßung')
fenster.label.pack()
fenster.button = Button(master=fenster, 
                       text='Sage Hallo', 
                       command=grüßen)              #2
fenster.button.pack()                                 #3
fenster.mainloop() 




