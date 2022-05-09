#----------------------------------------------------
# Dateiname: linkfind.py
# Suche nach Hyperlinks in einem Text
#
# Python 3
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------
from re import *
def linkfind(datei):
    re = compile('http://.+html?', I)                #1
    f = open(datei,'r')
    text = f.read()
    f.close()
    return re.findall(text)                          #2

linkliste = linkfind('/python310/LICENSE.txt')
print('Links in der Python-LICENSE-Datei:')
for link in linkliste: print(link)


input('Beenden mit <ENTER>')
