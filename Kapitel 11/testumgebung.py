#----------------------------------------------------
# Dateiname: testumgebung.py
# Testumgebung für die Klasse Geld
#
# Python 3
# Kap. 11 
# Michael Weigend 3.6.2019
#----------------------------------------------------
import sys
sys.path.append('module')
sys.path.append(r'c:\projekt\module')
from geld import Geld 
print('Test der Klasse Geld')
print()
anweisung = input('Anweisung: ')
while anweisung !=  '':
    try:
        exec(anweisung)  # Anweisung wird ausgeführt
    except:
        print ('Fehler: ' + str(sys.exc_info()[0]))
    anweisung = input('Anweisung: ')
print('Ende des Tests')
