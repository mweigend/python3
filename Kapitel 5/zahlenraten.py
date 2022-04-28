#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: zahlenraten.py
# 
# Python 3
# Kap. 5 Lösung 5
# Michael Weigend 1. 10. 09
#----------------------------------------------------

import random
zufallszahl = random.randint(0,100)
print("Raten Sie eine Zahl!")
zahl = -1
while zahl != zufallszahl:
    zahl = int(input("Zahl: "))
    if zahl == zufallszahl:
        print("Sie haben die Zahl gefunden!")
    elif zahl < zufallszahl:
        print("Zu klein!")
    else:
        print("Zu groß!")


input("Beenden mit <ENTER>")
