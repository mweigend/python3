#----------------------------------------------------
# Dateiname: ozon.pyw
# Recherchiert auf der Website des Landesumweltamtes
# nach der aktuellen Ozon-Konzentration am angegebenen Ort.
#
# Python 3, 8. Auflage, mitp 2019
# Kap. 23 Lösung 1
# Michael Weigend 24.03.2019
#----------------------------------------------------

from urllib.request import urlopen
from re import findall
from tkinter import (Tk, StringVar, Frame, Label,
                    Button, LEFT, Entry)
SCHABLONE = '''Die Ozonkonzentration der Luft
am Standort {} beträgt 
{} Mikrogramm pro Kubikmeter
(gemessen in Bodennähe).'''                           #1

URL = 'https://www.lanuv.nrw.de/fileadmin/lanuv/luft/immissionen/aktluftqual/eu_o3_akt.htm'

class Ozoncheck:                                      #2
  def __init__ (self, ort):
    try:
      self.ort = ort
      f = urlopen(URL)             #4
      self.htmltext = str(f.read())
      f.close()
      self.ergebnis = self.auswerten()
    except:
      self.ergebnis = ''

  def auswerten(self):
     re1 = self.ort + '.*?</tr>'                      #5
     re2 = '<td .+?</td></tr>'
     re3 = '\d+'
     zeile = findall(re1, self.htmltext)[0]           #6
     letztesStück = findall(re2, zeile)[0]
     return findall(re3, letztesStück)[0]

  def __str__(self):
      return self.ergebnis

class App:
  def __init__(self):
    meinfont = ('Arial', 10)
    self.fenster = Tk()
    self.ort = StringVar()
    self.ergebnis = StringVar()
    self.fenster.title('Ozon-Check')
    self.frame = Frame(self.fenster)
    Label(self.frame, font=meinfont,
          text='Ort: ').pack(side=LEFT)
    Entry(self.frame, font=meinfont,
          textvariable=self.ort).pack(side=LEFT)
    Button(self.frame, font=meinfont, text=' Ozon ',
           command=self.ozoncheck).pack(side=LEFT, padx=5)
    self.frame.pack(padx=5, pady=5)
    Label(self.fenster, font=meinfont,height=4,
          textvariable=self.ergebnis).pack()
    self.fenster.mainloop()

  def ozoncheck(self):                                #7
    zahl = str(Ozoncheck(self.ort.get()))
    if zahl:
      self.ergebnis.set(SCHABLONE.format(self.ort.get(), zahl))
    else:
      self.ergebnis.set(
      'Ihre Anfrage konnte nicht \n bearbeitet werden.')

App()

