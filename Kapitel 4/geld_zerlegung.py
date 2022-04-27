#!/usr/bin/env python
# ---------------------------------------------------
# Dateiname: charts.py
# 
# Zerlegung eines Geldbetrages in Scheine und Münzen
#
# Python 3,  mitp Verlag
# Kap. 4, Lösung 4
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

geld = input("Geldbetrag in Euro: ")
geld = round(int(geld))
zwanziger = geld // 20
geld = geld % 20
zehner  =geld // 10
geld = geld % 10
fünfer = geld // 5
geld = geld % 5
zweier = geld // 2
einer = geld % 2
print("Der Betrag setzt sich wie folgt zusammen:")
print(zwanziger, "mal 20 Euro")
print(zehner, "mal 10 Euro")
print(fünfer, "mal 5 Euro")
print(zweier, "mal 2 Euro")
print(einer, "mal 1 Euro")

