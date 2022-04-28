#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: ulam.py
# Berechnung der (3a+1)-Folge von Ulam
# Python 3
# Kap. 5 Lösung 11
# Michael Weigend 1. 10. 09
#----------------------------------------------------

print("Berechnung der (3a + 1)-Folge von Ulam") 
a = int(input("Startwert: "))
while a != 1:
    print(a)
    if a%2 == 0:
        a = a//2
    else:
        a = 3*a + 1
print(a)      # Ausgabe des letzten Elementes der Folge


input("Beenden mit <ENTER>")
