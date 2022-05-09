#----------------------------------------------------
# Dateiname: tabelle.py
# Ausgabe eines Analyseergebnisses
#
# Python 3
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------
tabelle=''
for i in range(1, 6):
    tabelle +='{a:>10}{b:>10}{c:>10}\n'.format(
        a=i, b=i**2, c=i**3)
    

print (tabelle)


input('Beenden mit <ENTER>')
