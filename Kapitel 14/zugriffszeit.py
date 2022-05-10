#----------------------------------------------------
# Dateiname: zugriffszeit.py
# Ermittelt, wie lange die README-Datei
# nicht mehr gelesen worden ist.
#
# Python 3  mitp Verlag
# Kap. 14
# Michael Weigend 5.6.2019
#----------------------------------------------------
import time
import os
AUSGABE = '''Die LICENSE-Datei ist seit {} Minuten
nicht mehr gelesen worden.'''
zugriffszeit = os.path.getatime('/python310/LICENSE.txt')
aktuelleZeit = time.time()    # Sekunden seit dem 1.1.1970
ausgabe = AUSGABE.format(int((aktuelleZeit-zugriffszeit)/60))
print(ausgabe)




input('Beenden mit <ENTER>')
