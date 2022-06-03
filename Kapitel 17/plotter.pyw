#----------------------------------------------------
# Dateiname:  plotter.pyw
# Einfacher Funktionsplotter
# Objektorientierte Programmierung mit Python
# Kap. 17 Lösung 2
# Michael Weigend 2.10.09
#----------------------------------------------------


from tkinter import *
class Plotter(object):
  def __init__(self):
    fenster = Tk()
    f = Frame(fenster)                                #1
    f.pack(padx=5, pady=5)
    self.term = StringVar()                           #2
    self.term.set('0')
    Label(f, text='f(x)= ').pack(side=LEFT)
    self.e = Entry(f, width=12, textvariable=self.term,
                   font=('courier', 10))                
    self.e.pack(side=LEFT)
    Button(f, text=' Plot ',
           command=self.plot).pack(side=RIGHT, padx=5)
    self.c = Canvas(fenster, width=160, height=160, bg='white')                                           #3
    self.c.pack(pady=5)                               #4
    self.c.create_line(10,80,150,80, arrow=LAST, fill='blue')
    self.c.create_line(80,10,80,150, arrow=FIRST, fill='blue')
    self.c.create_text(90,90,text='1')                #5
    self.linie = self.c.create_line(30, 80, 130, 80, width=2)
    fenster.mainloop()

  def plot(self):
      f = {}
      try:                                            
        for x in range(-5, 6, 1):
            f[x] = 80 -10 * eval(self.term.get())     #6
        self.c.coords(self.linie,
             30, f[-5], 40, f[-4], 50, f[-3], 60, f[-2],
             70, f[-1], 80, f[0], 90, f[1], 100, f[2],
             110, f[3], 120, f[4], 130, f[5])         #7
      except: self.term.set('Ung\xfcltig!')           #8

p = Plotter()



                    
