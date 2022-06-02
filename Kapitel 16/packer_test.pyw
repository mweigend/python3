#----------------------------------------------------
# Dateiname: packer_est.pyw
# Python 3, mitp Verlag
# Kap. 16
# Michael Weigend 5.6.2019
#----------------------------------------------------

from tkinter import *
fenster = Tk()
labels=[]
for i in range(4):
    labels.append(Label(master=fenster, text=str(i),
                   bg='white', font=('Arial', 50)))
labels[0].pack(side=TOP)
labels[1].pack(side=RIGHT)
labels[2].pack(side=RIGHT)
labels[3].pack(side=LEFT)
fenster.mainloop()




