#----------------------------------------------------
# Dateiname: staumelder.py
# Generiert Staumeldungen
#
# Python 3
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------
# 
from random import *

muster1 = '''Ein Stau von {laenge} km Länge
erwartet Sie auf der {autobahn} Richtung {richtung}
vor {abfahrt}.\n\n'''                               #1

muster2 = '''Auf der {autobahn} Richtung {richtung}
vor {abfahrt} {laenge} km Stau.\n\n'''
muster = [muster1, muster2]                          #2                

class StauBericht(object):                   
    def __init__(self, stauliste, muster):           #3
        self.stauliste = stauliste    
        self.muster = muster

    def meldeStau(self, stau):
        autobahn, richtung, abfahrt, laenge = stau
        zufall = randint(0, len(self.muster) - 1)    #4
        meldung = self.muster[zufall].format(
                                  autobahn=autobahn,
                                  richtung=richtung,
                                  abfahrt=abfahrt,
                                  laenge=laenge)     #5                                  
        return meldung

    def __str__(self):                               #6
        bericht = ''
        for stau in self.stauliste:
            bericht += self.meldeStau(stau)
        return bericht

# Hauptprogramm
staus = [('A1','Köln', 'dem Westhofener Kreuz', 4),
       ('A40', 'Dortmund', 'der Abfahrt Bochum Zentrum', 6)]

print(StauBericht(staus, muster))

input("<ENTER>")
