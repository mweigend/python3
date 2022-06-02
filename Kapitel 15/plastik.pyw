#----------------------------------------------------
# Dateiname: plastik.pyw
#
# Python 3, mitp Verlag
# Kap. 15, Lösung 3
# Michael Weigend 5.6.2019
#----------------------------------------------------
 
from tkinter import *

class Plastik(object):
  def __init__(self):
    self.fenster = Tk()
    self.fenster.title('Kunststoff')
    self.schwimmt, self.brennt = IntVar(), IntVar()   #1
    self.russt, self.duftet, self.tropft = IntVar(), IntVar(), IntVar()
    self.ausgabe = StringVar()

    Label(self.fenster, text='Dichte',width=24,
          font=('Arial', 12), fg='blue').pack()
    Radiobutton(self.fenster, text='schwimmt', value= 1,
                       variable=self.schwimmt).pack() #2
    Radiobutton(self.fenster, text='schwimmt nicht',
               value= 0, variable=self.schwimmt).pack() 
    Label(self.fenster, text='Brennbarkeit',width=24,
          font=('Arial', 12),fg='blue').pack()
    Radiobutton(self.fenster, text='brennt', value= 1,
                variable=self.brennt).pack()
    Radiobutton(self.fenster, text='brennt nicht',
                value=0, variable=self.brennt).pack()
    Label(self.fenster, 
          text='Verhalten beim Verbrennen',
          width=24, font=('Arial', 12), 
          fg='blue').pack()
    Checkbutton(self.fenster, text='rußende Flamme',
            offvalue=0, onvalue=1, 
            variable=self.russt).pack()               #3
    Checkbutton(self.fenster, text='tropft',
                offvalue=0, onvalue=1, 
                variable=self.tropft).pack()
    Checkbutton(self.fenster, text='duftet nach Wachs',
               offvalue=0, onvalue=1,
               variable=self.duftet).pack()
    Button(self.fenster, text='Auswertung',
        command=self.auswertung).pack()
    Label(self.fenster,font=('Arial', 12), 
          width=24, height=2,
          bg='yellow',textvariable=self.ausgabe).pack()

    self.fenster.mainloop()

  def auswertung(self):
    s, b = self.schwimmt.get(), self.brennt.get()     #4
    d, t = self.duftet.get(), self.tropft.get()
    r = self.russt.get()
    if s and b and d and t and not r:
        self.ausgabe.set('Es ist Polyethylen (PE).')
    elif not s and b and not d and not t and r:
        self.ausgabe.set('Es ist Polystyrol(PS).')
    elif not (s or b or d or r or t):
        self.ausgabe.set('Es ist Polyvinylchlorid (PVC).')
    else:
        self.ausgabe.set('Kunststoff unbekannt.')

p = Plastik() 



 



