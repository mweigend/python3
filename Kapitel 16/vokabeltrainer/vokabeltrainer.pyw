#----------------------------------------------------
# Dateiname: vokabeltrainer.pyw
#
# Python 3, mitp Verlag
# Kap. 16
# Michael Weigend 5.6.2019
#----------------------------------------------------

from tkinter import *

class Karteikasten:
    def __init__(self, datei):
        self.__nochNichtGelernt = []
        f = open(datei, 'r', encoding='utf-8')
        wortschatz = f.readlines()                  #1
        f.close()
        for zeile in wortschatz:
            vokabel = zeile.split()                 #2
            self.__nochNichtGelernt.append(vokabel) #3

    def getNeueVokabel(self):
        if self.__nochNichtGelernt:                 #4
           return self.__nochNichtGelernt[0]

    def lerne (self): 
        del self.__nochNichtGelernt[0]

    def legeNachHinten(self):
        self.__nochNichtGelernt.append(
               self.__nochNichtGelernt[0])
        del self.__nochNichtGelernt[0]




class Vokabeltrainer:
  def __init__(self, datei):
    # neuen Karteikasten anlegen und erste Karte ziehen
    self.gelernt = 0 
    self.datei = datei                                   
    self.k = Karteikasten(datei)                      #1   
    self.aktVokabel = self.k.getNeueVokabel()
          
    # Widgets instanzieren
    self.fenster = Tk()    
    self.vokabel = StringVar()                        #2 
    self.vokabel.set(self.aktVokabel[0])
    self.titel = Label(master=self.fenster,
                    text='Vokabeltrainer',
                    font=('Comic Sans MS',14),fg='blue')
    self.rahmen = Frame(master=self.fenster,
                      relief=RIDGE,bd=2)
    self.englischLabel = Label(master=self.rahmen,
                        textvariable=self.vokabel,    #3
                        font=('Arial',14))
    self.deutschLabel = Label(master=self.rahmen,
                        text='Deutsch:')
    self.entry = Entry(master=self.rahmen, width=15)
    self.okButton = Button(master=self.rahmen,text='ok',
                           command=self.ok)           #4
    self.gelerntLabel = Label(master=self.fenster, 
                      width=10, bg='yellow',
                      text=str(self.gelernt)+' gelernt')
    self.rfLabel = Label(master=self.fenster, width=20)
    self.nochmalButton = Button(master=self.fenster,
                              text='noch einmal',
                              command=self.nochmal)   #5
    self.layout()
    self.fenster.mainloop()

  def layout(self):
    # Layout der Widgets  
    self.titel.pack()
    self.englischLabel.pack()
    self.deutschLabel.pack(side=LEFT)
    self.entry.pack(side=LEFT, padx=10, pady=10)
    self.okButton.pack(side=RIGHT, padx=10, pady=10)
    self.rahmen.pack()
    self.gelerntLabel.pack(side=LEFT, padx=10, pady=10)
    self.rfLabel.pack(side=LEFT)
    self.nochmalButton.pack(side=RIGHT,
                            padx=10, pady=10)

  def nochmal(self):
    self.k = Karteikasten(self.datei)                 #1
 
    self.aktVokabel = self.k.getNeueVokabel()         #2
    self.vokabel.set(self.aktVokabel[0])              #3
    self.gelernt = 0
    self.gelerntLabel.config(
        text = str(self.gelernt) + ' gelernt')        #4         
    self.rfLabel.config(text='')                      #5

  def ok(self):
    if self.entry.get() in self.aktVokabel[1:]:       #6
        self.rfLabel.config(text='Richtig!')
        self.k.lerne()
        self.fenster.after(1000, self.loeschen) 
        self.gelernt += 1
        self.gelerntLabel.config(
            text=str(self.gelernt) + ' gelernt') 

    else:                                             #7
        ausgabe = 'Falsch! Richtig ist:\n'
        ausgabe += ' '.join(self.aktVokabel[1:])
        self.rfLabel.config(text=ausgabe)
        self.k.legeNachHinten()
        self.fenster.after(3000, self.loeschen)

  def loeschen(self):                                 #8
      self.rfLabel.config(text='')
      self.entry.delete(0,15)
      self.aktVokabel = self.k.getNeueVokabel()
      if self.aktVokabel:
          self.vokabel.set(self.aktVokabel[0])
      else:
         self.rfLabel.config(text='Alles gelernt!') 

# Hauptprogramm
 
v = Vokabeltrainer('vokabeln.txt')


