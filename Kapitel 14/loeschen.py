#----------------------------------------------------
# Dateiname: loeschen.py
#
# Objektorientierte Programmierung mit Python
# Python 3  mitp Verlag
# Kap. 14
# Michael Weigend 5.6.2019
#----------------------------------------------------
from os import *
verzeichnis = input('Verzeichnis: ')
if verzeichnis == "":
    verzeichnis = "."
zähler = 0
chdir(verzeichnis)                               #1 
print ('Gelöschte Dateien:')
for datei in listdir(verzeichnis):
    if datei.split('.')[-1] == 'old':            #2
        remove(datei)                            #3
        print (datei)
        zähler += 1
print ('Es wurden {} Dateien gelöscht.'.format(zähler))


input('Beenden mit <ENTER>')
