#!/usr/bin/env python
# ---------------------------------------------------
# Dateiname: isbn.py
# Prüfung einer ISBN-13-Nummer
#
# Objektorientierte Programmierung mit Python 3
# Kap. 4 Lösung 4
# Michael Weigend 28.04.2022
#----------------------------------------------------
 

eingabe = input("Geben Sie eine 13-stellige ganze Zahl ein: ")
nummer = int(eingabe)
z13 = nummer%10
nummer = nummer//10
z12 = nummer%10
nummer = nummer//10
z11 = nummer%10
nummer = nummer//10
z10 = nummer%10
nummer = nummer//10
z9 = nummer%10
nummer = nummer//10
z8 = nummer%10
nummer = nummer//10
z7 = nummer%10
nummer = nummer//10
z6 = nummer%10
nummer = nummer//10
z5 = nummer%10
nummer = nummer//10
z4 = nummer%10
nummer = nummer//10
z3 = nummer%10
nummer = nummer//10
z2 = nummer%10
nummer = nummer//10
z1 = nummer

summe_ungerade = z1 + z3 + z5 + z7 + z9 + z11 + z13
summe_gerade = z2 + z4 + z6 + z8 + z10 + z12
quersumme = summe_ungerade + 3 * summe_gerade
test = quersumme & 10

if test == 0:
    print('Gültige ISBN-13-Nummer')
else:
    print('Keine gültige ISBN-13-Nummer')


input("Beenden mit <ENTER>")
           
