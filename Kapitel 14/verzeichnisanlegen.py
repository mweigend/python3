#----------------------------------------------------
# Dateiname: verzeichnisanlegen.py
#
# Python 3  mitp Verlag
# Kap. 14
# Michael Weigend 5.6.2019
#----------------------------------------------------
# verzeichnisanlegen.py
from os import makedirs
vorname = input('Vorname: ')
nachname = input('Nachname: ')
verzeichnisname = (vorname[:6]+nachname[:2]).lower()  #1
try:
    makedirs('/python/projekt/user/'+verzeichnisname) #2
    print('Verzeichnis angelegt')   
except:
    print('Verzeichnis existiert bereits')



input('Beenden mit <ENTER>')
