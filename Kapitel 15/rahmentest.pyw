#----------------------------------------------------
# Dateiname: rahmentest.pyw
#
# Python 3, mitp Verlag
# Kap. 15
# Michael Weigend 5.6.2019
#----------------------------------------------------
# rahmentest.pyw
from tkinter import *
fenster = Tk()
rahmentypen = [SUNKEN, RAISED, GROOVE, RIDGE, FLAT]
for rahmen in rahmentypen:
    label = Label(fenster, text=str(rahmen),
                  font=('Arial',10),
                  bd=4, relief=rahmen, padx=10)
    label.pack()
fenster.mainloop()


