#----------------------------------------------------
# Dateiname: robot.py
# Suchroboter
# Achtung! Programm hat relativ lange Laufzeit.
#
# Python 3 mitp Verlag
# Kap. 14
# Michael Weigend 5.6.2019
#----------------------------------------------------
from os  import walk                                         #1
from os.path import join, normcase
SUCHBERICHT='''Suchbericht
-----------
Suchbegriff: {}
Wurzel des Verzeichnisbaums: {}
{}
Es wurden {} Dateien durchsucht.
{} Dateien waren nicht lesbar.
'''

class suchRobot(object):
  def __init__(self, suchwort, wurzel):
    self.ergebnis = []
    self.suchwort = suchwort
    self.wurzel = wurzel
    self.nicht_lesbar = 0
    self.durchsucht = 0
    liste = walk(wurzel)                           #2
    for pfad, verzeichnisse, dateien in liste:    
      for datei in dateien:
        self.durchsucht += 1
        try:
          f = open(join(pfad, datei), 'r')      #2
          text = f.read()
          f.close()         
          n = text.count(suchwort)                      #3
          if n > 0:
            p = normcase(join(pfad, datei))           #4
            self.ergebnis += [(n, p)]                #5
        except:
          self.nicht_lesbar += 1
    self.ergebnis.sort(reverse=True)


  def __str__(self):                               #7
    tabelle = ""
    for (n, pfad) in self.ergebnis:
     tabelle += '{} ({} Vorkommen )\n'.format(
            pfad, n, self.suchwort)
    return SUCHBERICHT.format(self.suchwort,
                              self.wurzel,
                              tabelle,
                              self.durchsucht,
                              self.nicht_lesbar)

# Hauptprogramm
suchwort= input('Suchwort: ')
wurzel = input('Wurzelverzeichnis: ')
bot = suchRobot(suchwort, wurzel)           
print (bot)



input('Beenden mit <ENTER>')
