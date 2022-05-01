# ---------------------------------------------------
# Dateiname: vokabeltrainer.py
# 
# Python 3, 8. Auflage
# Kap. 8 
# Michael Weigend 2.6.2019
#----------------------------------------------------

import random

#Funktionsdefinitionen
def dict_laden(pfad):                               #1
    d = {}
    try:
       datei = open(pfad)
       liste = datei.readlines()
       for eintrag in liste:
            l_eintrag = eintrag.split()
            d[l_eintrag[0]] = l_eintrag[1:]
       datei.close()
    except:
        pass
    return d

def aufgabe(d):
    zufall = random.randint(0, len(d.keys())-1)
    vokabel = list(d.keys())[zufall]                #2
    print ('Wie lautet das deutsche Wort für',
            vokabel+'?')
    antwort = input()                               #3
    if antwort not in d[vokabel]:                   #4
        print('Leider falsch.')
        print(vokabel, 'bedeutet:', end=' ')
        for wort in d[vokabel]:
            print (wort, end=' ')
        print()
    else:                                           #5
        print('Richtig!')
        del d[vokabel] 

# Hauptprogramm
print('Vokabeltrainer')
print()
woerterbuch = dict_laden('woerterbuch.txt')
while woerterbuch:                                  #6
    aufgabe (woerterbuch)
print ('Sie haben alle Vokabeln gelernt.')

eingabe = input()




    
