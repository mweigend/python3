#----------------------------------------------------
# Dateiname: tagnacht.pyw
#
# Python 3, mitp Verlag
# Kap. 15
# Michael Weigend 5.6.2019
#----------------------------------------------------
from tkinter import *
fenster = Tk()
labelnacht = Label(fenster, text='Nacht',
                  font=('Arial',20),
                  fg='white',bg='black', width=10)
labelnacht.pack()
labeltag = Label(fenster, text='Tag',
                font=('Arial',20),
                fg='#000000', bg='#ffffff', width=10)
labeltag.pack()
fenster.mainloop()


