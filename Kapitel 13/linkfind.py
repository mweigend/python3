#----------------------------------------------------
# Dateiname: linkfind.py
# Suche nach Hyperlinks in einem Text
#
# Python 3
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------
# linkfind.py
from re import *
def linkfind(datei):
    r = compile('https?://.+html?', I)           #1
    with open(datei,'r') as stream:
        text = stream.read()
    return r.findall(text)                       #2

linkliste = linkfind('/Python310/LICENSE.txt')
print('Links in der Python-LICENSE-Datei:')
for link in linkliste: 
    print(link)

