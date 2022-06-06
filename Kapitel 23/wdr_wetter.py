#----------------------------------------------------
# Dateiname: wdr_wetter.py
# Liefert durch Webscraping eine Wettervorhersage.
#
# Python 3
# Kap. 23
# Michael Weigend 07.06.2022
#----------------------------------------------------
# wdr_wetter.py
from urllib.request import urlopen
from re import findall
WDR = 'https://www1.wdr.de/index.html'
with urlopen(WDR)as f:
    htmltext=(str(f.read()))

re = '<span class="max-temperature">Max: \d+'
text_list = findall(re, htmltext)
temp = [findall('\d+', text)[0] for text in text_list]
print('Wie warm wird es?')
print('Höchsttemperatur heute: {}°C'.format(temp[0]))
print('Höchsttemperatur morgen: {}°C'.format(temp[1]))
