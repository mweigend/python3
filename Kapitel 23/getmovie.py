#----------------------------------------------------
# Dateiname: getmovie.py
# Filme finden und herunterladen
# heruntergeladen.
# Achten Sie darauf, dass ein Unterverzeichnis Filme existiert,
# in dem die Filme gespeichert werden.
#
# Python 3
# Kap. 23
# Michael Weigend 04.06.2022
#----------------------------------------------------
# getmovie.py
from urllib.request import urlopen
from re import findall

PLANET = 'https://www.planet-schule.de/sf/filme-online.php?seite=2'
PATH = 'Filme/'

selected = [] # Liste der ausgeählten Filme

with urlopen(PLANET)as f:
    htmltext=(str(f.read()))
movies = findall('https://dlplanet.+?\.mp4', htmltext)

for url in movies: # Filme auswählen
    print(url.split('/')[-1])
    response = input('Diesen Film herunterladen? (j/n)')
    if response == 'j':
        selected.append(url)
        
for url in selected: # Filme herunterladen und speichern
    print('Download von {}...'.format(url.split('/')[-1]))
    with urlopen(url) as f:
        data = f.read()
    print ('... fertig.')
    path = PATH + url.split('/')[-1]
    with open(path, 'wb') as movie:
        movie.write(data)
           
            
    

