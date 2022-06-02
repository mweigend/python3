#----------------------------------------------------
# Dateiname: hangman.pyw
# Wörterraten
# Python 3, mitp Verlag
# Kap. 16, Lösung 4
# Michael Weigend 5.6.2019
#----------------------------------------------------

# hangman.pyw
import random 
from tkinter import *

class Wortgenerator:
    def __init__ (self, datei):                      #1
        self.wortliste=[]
        f=open(datei, 'r', encoding='utf-8')
        liste=f.read().split()
        f.close()
        for wort in liste:
            if wort.isalpha()and  len(wort)>5:       #2
                self.wortliste.append(wort.upper())

    def getWort(self):
    # liefert aus der internen Wortliste ein Zufallswort
        return random.choice(self.wortliste)

class Sprache:
    def __init__(self, master):
        self.master=master
        self.rahmen =Frame()
        self.datei=StringVar()
        self.deutschRadio=Radiobutton(self.rahmen,
                          value='clavigo.txt',
                          text='Deutsch',
                          variable=self.datei)
        self.deutschRadio.select()
        self.englRadio=Radiobutton(self.rahmen,
                            value='marktwain.txt',
                            text='Englisch',
                            variable=self.datei)    
        self.deutschRadio.pack()
        self.englRadio.pack()
        self.wg=Wortgenerator(self.datei.get())     #3

    def getDatei(self):
        return self.datei.get()

    def neuerWG (self):
        self.wg=Wortgenerator(self.datei.get())

class NeuButton:
    def __init__(self,master, punkte, sprache, ausgabe):
        self.ausgabe=ausgabe
        self.punkte=punkte
        self.sprache=sprache
        self.button=Button(master, text='Neu',
                           command= self.neuesSpiel)
 
    def neuesSpiel(self):
        self.sprache.neuerWG()
        self.punkte.setPunkte(20)
        self.ausgabe.neuesWort()

class Punkte:
    def __init__(self, master, p):
        self.punkte=p
        self.label=Label(master,text=str(p),
                     font=('Arial',20), bg='yellow')

    def aktualisiere(self, wert):                   #4
        self.punkte+=wert
        self.label.config(text= str(self.punkte))

    def setPunkte(self, punkte):
        self.punkte=punkte
        self.label.config(text= str(self.punkte))

class Ausgabe:
    def __init__(self, master,sprache):             #5
        self.sprache=sprache
        self.wort=self.sprache.wg.getWort()
        self.ausgabe=len(self.wort)*'-'
        self.label=Label(master,text=self.ausgabe,
                         font=('Courier',20), 
                         bg='white')

    def neuesWort(self):                            
        self.wort=self.sprache.wg.getWort()
        self.ausgabe=len(self.wort)*'-'
        self.label.config(text=len(self.wort)*'-')

    def aktualisiere(self, wort):
        self.ausgabe=wort
        self.label.config(text=wort)

class OKButton:          
  def __init__(self, master, eingabe, ausgabe,
                 punkte, wortgenerator):
    self.eingabe= eingabe
    self.ausgabe=ausgabe
    self.punkte=punkte
    self.wg=wortgenerator
    self.button=Button(master, text='OK',
                       command= self.pruefe)
 
  def pruefe(self):                                 #6
    z=self.eingabe.get().upper()
    ausgabeliste=list(self.ausgabe.ausgabe)         #7
    self.eingabe.delete(0)                          #8
    if z in self.ausgabe.wort and z not in self.ausgabe.ausgabe:                               #9
        # ausgabe aktualisieren und Pluspunkte
        for i in range(len(self.ausgabe.wort)): 
            if self.ausgabe.wort[i]==z:
                ausgabeliste[i]=z
        self.ausgabe.aktualisiere(''.join(ausgabeliste))
        self.punkte.aktualisiere(1)                 #10
        # Wenn Wort vollstaendig, erzeuge neues Wort
        if '-' not in self.ausgabe.ausgabe:         #11
            self.button.after(2000, 
                              self.ausgabe.neuesWort)
            self.punkte.aktualisiere(5)

    else: self.punkte.aktualisiere(-1)

class Spiel:
    def __init__ (self):
        # Unterobjekte
        self.fenster=Tk()
        self.sprache=Sprache(self.fenster)
        self.titel=Label(self.fenster,
                         text='Wörterraten',
                         font=('Arial',20))
        self.labelEingabe=Label(text='Buchstabe:')
        self.punkte=Punkte(self.fenster,20)
        self.ausgabe=Ausgabe(self.fenster, self.sprache)
        self.neu=NeuButton(self.fenster, self.punkte,
                           self.sprache, self.ausgabe)
        self.eingabe=Entry(self.fenster, width=2,font=('Arial',20))
        self.ok=OKButton(self.fenster, self.eingabe, self.ausgabe,
                         self.punkte, self.sprache.wg)
        self.layout()

    def layout(self): 
        self.titel.grid(column=0,row=0,columnspan=2)
        self.punkte.label.grid(column=3,row=0)
        self.ausgabe.label.grid(column=0,row=1, columnspan=3)
        self.sprache.rahmen.grid(column=0,row=2, padx=10)
        self.neu.button.grid(column=1,row=2)
        self.eingabe.grid(column=2,row=2, padx=20)
        self.ok.button.grid(column=3,row=2)
        self.fenster.mainloop()

#Hauptprogramm
spiel=Spiel()
