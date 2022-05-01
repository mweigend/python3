#----------------------------------------------------
# Dateiname:  woerterbuch.py
# 
# 
# Python 3
# Kap. 8 
# Michael Weigend 2.6.2019
#----------------------------------------------------
def erschaffeWoerterbuch():
# Aufbau eines englisch-deutschen Wörterbuchs
    d = {}
    englisch = input('Englisches Wort: ')
    while englisch:                                  #1
         deutsch = input('Deutsche Übersetzung: ')
         d[englisch] = deutsch
         englisch = input('Englisches Wort: ')
    return d

print (erschaffeWoerterbuch())


