#----------------------------------------------------
# Dateiname: labelgroesse.pyw
#
# Python 3, mitp Verlag
# Kap. 15
# Michael Weigend 5.6.2019
#----------------------------------------------------
from tkinter import *
fenster = Tk()
label1 = Label(fenster, text='gro\xdf',font=('Arial',40), 
             relief='groove', bg='yellow')
label2 = Label(fenster, text='klein',font=('Arial',10), 
             relief='groove', bg='yellow')
label1.pack()
label2.pack()
fenster.mainloop()  



