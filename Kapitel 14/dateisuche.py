#----------------------------------------------------
# Dateiname: dateisuche.py
#
# Python 3
# Kap. 14
# Michael Weigend 5.6.2019
#----------------------------------------------------
# dateisuche.py
from os import walk
from os.path import normcase, join, getmtime
from time import time, ctime

class Dateisucher:
  def __init__(self, start, zeit):
    self.durchlauf = walk(start)                          
    self.ergebnis = []
    zeitlimit = time()- zeit*3600                          #1
    for pfad, verzeichnisse, dateien in self.durchlauf:
      for datei in dateien:
        dateipfad = normcase(join(pfad, datei))            #2
        if getmtime(dateipfad) > zeitlimit:
          self.ergebnis.append(
              (getmtime(dateipfad), dateipfad))            #3

  def __str__(self):
    bericht = 'Datei und Zeitpunkt der letzten Änderung:\n\n'
    for zeit, pfad in self.ergebnis:
      bericht += '{}    {} \n'.format(pfad, ctime(zeit))   #5
    return bericht


#Hauptprogramm
start = input('Wurzel des Verzeichnisbaums: ')
zeit = int(input('Zeitraum (Stunden): '))
print(Dateisucher(start, zeit))
input('Beenden mit <ENTER>')
