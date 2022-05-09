#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: grossbuchstaben.py
# Drucke alle Worte aus zwei grossen Buchstaben
# Python 3
# Kap. 5 Lösung 9
# Michael Weigend 1. 10. 09
#----------------------------------------------------

# grossbuchstaben.py
# Drucke alle Wörter aus zwei großen Buchstaben
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for a in alphabet:
    for b in alphabet:
         print(a+b, end=" ")
print()
input("Beenden mit <ENTER>")
