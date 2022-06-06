#----------------------------------------------------
# Dateiname: sucher.py
# Befragt Suchmaschine, wieviele Web-Dokumente sie zu
# einem Suchbegriff findet.
#
# Python 3
# Kap. 23
# Michael Weigend 07.06.2022
#----------------------------------------------------

# sucher.py
import requests                  
from re import findall
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +\
             'AppleWebKit/537.36 (KHTML, like Gecko) '    +\
             'Chrome/100.0.4896.127 Safari/537.36'               #1
HEADERS = {'User-Agent': USER_AGENT}                             #2

def suche (suchwort):
    r = requests.get('https://www.google.de/search?q=' + suchwort,
                     headers=HEADERS)                            #3
    if r.status_code == 200:                                     #4
      textstelle = findall('Ungefähr.+? Ergeb', r.text)[0]          #5
      zahl = findall(' .+ ', textstelle)[0]                      #6
      return 'Google findet {} Ergebnisse.'.format(zahl)         #7
    else:
      return 'Fehler'                                            #8

# Hauptprogramm
suchwort = input('Suchwort: ')
while suchwort:
    ergebnis = suche(suchwort)
    print(ergebnis)
    suchwort = input('Suchwort: ')
print('Auf Wiedersehen ...')





                    
