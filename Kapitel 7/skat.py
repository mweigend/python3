# ---------------------------------------------------
# Dateiname: skat.py
# Mischen eines Skatspiels
# Python 3
# Kap. 7 Lösung 3
# Michael Weigend 8. 10. 09
#----------------------------------------------------

import random
farben = ['Kreuz', 'Pik', 'Herz', 'Karo']
werte = ['Ass', 'König', 'Dame', 'Bube', '10', '9', '8', '7']
spiel = [(f,w) for f in farben for w in werte]       #1
anzahl = random.randint(20, 40)
for i in range(anzahl):
    karte1 = random.randint(0, 31)                   #2
    karte2 = random.randint(0, 31)                   #3
    spiel[karte1], spiel[karte2] = spiel[karte2], spiel[karte1] 
print ("Gemischtes Skatspiel:")
print (spiel) 

input("Beenden mit <ENTER>")
