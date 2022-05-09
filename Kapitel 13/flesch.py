#----------------------------------------------------
# Dateiname: flesch.py
# Flesch-Analyse eines Textes
#
# Python 3
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------

from re import *
class Flesch:
    def __init__(self, datei):
        self.datei = datei
        f  = open(datei,'r')
        self.text = f.read()
        f.close()

    def anzahlWorte(self):
        return len(self.text.split())                 #1

    def anzahlSätze(self):
        re = compile('[!?.;:]+\s')                    #2           
        return len(re.split(self.text))

    def anzahlSilben(self):
        re = compile('[aeiou]+', I)                   #3
        return len (re.split(self.text))

    def readability (self):
        asl = float(self.anzahlWorte())/self.anzahlSätze()
        asw = float(self.anzahlSilben())/self.anzahlWorte()
        return int(206.835 - 1.015*asl - 84.6*asw)

    def __str__(self):
        text = 'Lesbarkeitsindex der Datei {} nach Flesch: {}'
        return text.format(self.datei, self.readability())

if __name__ == '__main__':
      print(Flesch('/python310/LICENSE.txt'))
      input('Beenden mit <ENTER>')
