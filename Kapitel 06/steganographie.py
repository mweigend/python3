# ---------------------------------------------------
# Dateiname: steganographie.py
# Verstecken eines Textes
# Python 3
# Kap. 6 Lösung 2
# Michael Weigend Januar 2013
#----------------------------------------------------

def zufallsbuchstabe():
        buchstaben = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        import random
        return buchstaben[random.randint(0, 25)]

def verstecke(s, n=1):
    textGross = s.upper()
    versteckt = ''
    for c in textGross:
        versteckt += c
        for i in range(n):
            versteckt += zufallsbuchstabe()
    return versteckt

print ('Um acht an der Uhr')
print ()
print (verstecke('Um acht an der Uhr'))
print (verstecke ('Um acht an der Uhr',2))
input ("Beenden mit <ENTER>")
