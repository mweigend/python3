#----------------------------------------------------
# Dateiname: rechteck_und_oval.pyw
# Objektorientierte Programmierung mit Python
# Kap. 17
# Michael Weigend 7.10.09
#----------------------------------------------------
from tkinter import *
fenster = Tk()
c = Canvas(fenster,width='8c', height='4c')
c.pack()
r = c.create_rectangle('1c','1c','4c','3c',fill='blue')
o = c.create_oval('1.5c','1.5c','6c','3.5c',fill='yellow')
fenster.mainloop()


