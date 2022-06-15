#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  thermometer.py
# Von einem digitalen Messgerät, dass den Widerstand
# eines Pt-100-Thermometers misst, wird in regelmäßigen 
# Zeitabständen die Display-Anzeige (natürliche Zahl)
# übernommen und daraus die Temperatur berechnet.
# Die Werte werden in einer Datei gespeichert.
#
# Python 3,  mitp Verlag
# Kap. 31
# Michael Weigend 11. 06. 2019
#----------------------------------------------------
from dmm import get_digits
from time import sleep
f = open('daten.csv', mode='w')
t = 0
print('Wie lange soll gemessen werden?')
max_time = int(input('Sekunden: '))
print('In welchen Zeitabständen?')
dt = int(input('Sekunden: '))
f.write('Zeit (s); Temperatur (°C)\n')
while t < max_time:
    n = get_digits()
    temp = (n/10 - 100)/0.39
    f.write(' {};{:.1f};\n'.format(t, temp))
    print(' {:4d} Sekunden {:5.1f} °C '.format(t, temp))
    sleep(dt)
    t += dt
f.close()

