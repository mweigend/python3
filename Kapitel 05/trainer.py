#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: trainer.py
# Multiplikationstrainer
# Python 3
# Kap. 5 Loesung 12
# Michael Weigend 1. 6. 2019
#----------------------------------------------------
import random                                         #1
import time
print("Multiplikationstrainer")
print("----------------------")
startzeit = time.time()
for i in range(5):
    a = random.randint(1,20)                          #2
    b  = random.randint(1,10)
    ergebnis =- 1                                     #3
    while ergebnis != a * b:
        ergebnis = int(input(str(a) + "*" + str(b) + "=")) #4
        if ergebnis == a * b:
            print("Richtig!")
        else:
            print("Falsch! Versuchen Sie es noch einmal!")
zeit = int(time.time() - startzeit)
print("Für die Aufgaben haben Sie", zeit, "Sekunden benötigt.")


input("Beenden mit <ENTER>")
            

    
    

