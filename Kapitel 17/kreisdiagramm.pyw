#----------------------------------------------------
# Dateiname: kreisdiagramm.pyw
# Visualisierung zweier Zahlen mit Kreisdiagramm
# Objektorientierte Programmierung mit Python
# Kap. 17
# Michael Weigend 8. 10. 09
#----------------------------------------------------

from tkinter import *
class Kreisdiagramm(object):
  def __init__ (self):
    self.fenster = Tk()
    self.fenster.title('Kreisdiagramm')
    self.anzeige = Anzeige(self.fenster)              #1
    self.eingabe = Eingabe(self.fenster, self.anzeige)#2
    self.fenster.mainloop()

class Anzeige:
  def __init__ (self, fenster):
    self.c = Canvas(master=fenster,
                  width='4c',height='4c')             #3              
    self.c.pack(side=RIGHT)
    self.teil1 = self.c.create_arc(
        '0.5c', '0.5c','3.5c','3.5c', fill='blue',
         style=PIESLICE, start=90,extent=180)         #4
    self.teil2 = self.c.create_arc(
        '0.5c','0.5c','3.5c','3.5c', fill='red',
         style=PIESLICE, start=90,extent=-180)

  def aktualisiere(self, z1, z2):                     #5
    summe = z1 + z2
    w1 = 360*z1/summe
    w2 = -(360-w1)
    self.c.itemconfigure(self.teil1, extent=w1)       #6
    self.c.itemconfigure(self.teil2, extent=w2)

class Eingabe(object):
    def __init__ (self, fenster, anzeige):
        self.anzeige = anzeige
        self.f = Frame(fenster, relief=GROOVE, bd=2)  #7
        self.f.pack(padx=5, pady=5)
        self.f1 = Frame(self.f)                        
        self.f2 = Frame(self.f)
        self.f1.pack()
        self.f2.pack()
        Label(self.f1,text='Anzahl 1:').pack(side=LEFT)
        Label(self.f2,text='Anzahl 2:').pack(side=LEFT)
        self.e1 = Entry(self.f1,width=8)
        self.e1.pack(side=LEFT,padx=5, pady=2)
        self.e2 = Entry(self.f2,width=8)
        self.e2.pack(side=LEFT,padx=5, pady=2)
        Label(self.f1, 
             width=2,bg='blue').pack(side=LEFT)
        Label(self.f2, width=2,bg='red').pack(side=LEFT)
        self.ok = Button(self.f,text='OK',
                         command=self.aktualisiere)   #8
        self.ok.pack(side=LEFT, padx=5, pady=5)

    def aktualisiere(self):                           #9
      if self.e1.get() and self.e2.get():
        z1 = int(self.e1.get())
        z2 = int(self.e2.get())
        self.anzeige.aktualisiere(z1, z2)  

k = Kreisdiagramm()
                    
