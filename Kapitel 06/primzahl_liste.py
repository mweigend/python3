# ---------------------------------------------------
# Dateiname: primzahl_liste.py
# Berechnung von Primzahlen
# Python 3, Kap. 6 
# mitp 2018
# Michael Weigend 3.1.2018
#----------------------------------------------------
def primzahl (zahl):
     if zahl <= 1:
         return False
     if zahl == 2:
         return True
     else:
         for i in range(2, zahl//2 + 1):
            if zahl % i == 0:    # Teiler gefunden
                return False
         return True     

def eingabe(): 
    print("Ich ermittle alle Primzahlen in einem Intervall")
    a = int(input("Untere Intervallgrenze: "))
    b = int(input("Obere Intervallgrenze: "))
    return (a, b)

def verarbeitung(intervall):
    prim = []                                      #1
    for i in range(intervall[0], intervall[1]+1):
        if primzahl(i):
            prim += [i]                            #2
    return prim

def ausgabe(primzahlen): 
    print("Primzahlen:")
    for zahl in primzahlen:
        print(zahl, end=" ")                       #3

# Hauptprogramm
intervall = eingabe()
primzahlListe = verarbeitung(intervall)
ausgabe(primzahlListe)

input("Beenden mit <ENTER>")
