#----------------------------------------------------
# Dateiname: platzbedarf.py
# Die Klasse modelliert den Platzbedarf der Verzeichnisse eines
# Verzeichnisbaums
#
# Python 3  mitp Verlag
# Kap. 14
# Michael Weigend 5.6.2019
#----------------------------------------------------
import os                                               
from os.path import join, getsize

ABSCHLUSSBERICHT =  '''Ich habe {} Verzeichnisse durchsucht.
Der gesamte Speicherbedarf beträgt {} Bytes.'''              #1

class Platzbedarf(object):
  def __init__(self, wurzel):
    self.ergebnis = []                                       #2
    liste = os.walk(wurzel)
    for verzeichnis, unterverzeichnisse, dateien in liste:
       groesse =  sum([getsize(join(verzeichnis, name))
                for name in dateien])                        #3
       self. ergebnis.append((verzeichnis, groesse))

  def __str__(self):
    bericht = ''
    for verzeichnis, speicherplatz in self.ergebnis:
        bericht +=  ('{} ({} Byte)\n'.format(
               verzeichnis, speicherplatz))
    bericht += ABSCHLUSSBERICHT.format(len(self.ergebnis),
                   sum([i[1] for i in self.ergebnis]))       #4
    return bericht

# Hauptprogramm
if __name__ == '__main__':
    print(Platzbedarf('/python310'))
    input('Beenden mit <ENTER>')
