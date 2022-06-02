#----------------------------------------------------
# Dateiname: fontstest.pyw
#
# Python 3, mitp Verlag
# Kap. 15
# Michael Weigend 5.6.2019
#----------------------------------------------------
from tkinter import*
fenster = Tk()
label1 = Label(fenster, text='Verdana 40',
             font=('Verdana', 40))
label1.pack()
label2 = Label(fenster, text='Times 30 bold',
             font=('Times', 30, 'bold'))
label2.pack()
label3 = Label(fenster, text='Comic Sans MS 20',
             font=('Comic Sans MS', 20))
label3.pack()
label4 = Label(fenster, 
               text='Courier 10 italic overstrike',
               font=('Courier',10, 'italic overstrike'))
label4.pack()
fenster.mainloop()

