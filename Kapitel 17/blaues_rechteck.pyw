#----------------------------------------------------
# Dateiname: blaues_rechteck.pyw
# Python 3  mitp Verlag
# Kap. 17
# Michael Weigend 5.6.2019
#----------------------------------------------------
from tkinter import *
fenster = Tk()
c = Canvas(fenster,width='8c', height='4c')
c.pack()
rechteck = c.create_rectangle('1c','1c','4c','3c',
                              fill='blue')     
fenster.mainloop()

