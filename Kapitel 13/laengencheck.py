#----------------------------------------------------
# Dateiname: laengencheck.py
# Ermittelt die mittlere Satzlänge in einem Text
#
# Python 3 
# Kap. 13
# Michael Weigend 04.05.2022
#----------------------------------------------------
# laengencheck.py
from re import *
def längencheck(datei):
    r = compile('[.,;:!?]+\s')                       #1
    with open(datei,'r') as stream:
        text = stream.read()

    anzahl = len(r.split(text))                      #2
    länge = float(len(text.split())) / anzahl        #3
    return länge

print('Mittlere Satzlänge in der LICENSE-Datei:')
print(längencheck('/Python310/LICENSE.txt'), 'Wörter')

