#----------------------------------------------------
# Dateiname: laengencheck.py
# Ermittelt die mittlere Satzlänge in einem Text
#
# Python 3 
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------
from re import *
def laengencheck(datei):
    re = compile('[.,;:!?]+\s')                       #1
    f = open(datei,'r')
    text = f.read()
    f.close()
    anzahl = len(re.split(text))                      #2
    laenge = float(len(text.split())) / anzahl        #3
    return laenge

print('Mittlere Satzlänge in der LICENCE-Datei:')
print(laengencheck('/python310/LICENSE.txt'), 'Wörter')


input('Beenden mit <ENTER>')
