#----------------------------------------------------
# Dateiname: beenden.py
#
# Python 3
# Kap. 14
# Michael Weigend 20.08.2016
#----------------------------------------------------
import sys

antwort = input('Programm beenden? (j/n)')
if antwort == 'j':
    sys.exit(0) 
print('Programm läuft weiter')
