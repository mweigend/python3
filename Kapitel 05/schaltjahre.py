#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: schaltjahre.py
# 
# Python 3
# Kap. 5 Loesung 4
# Michael Weigend 1. 10. 09
#----------------------------------------------------
# schaltjahre.py
jahr = int(input("Geben Sie ein Jahr an: "))
if (jahr%400 == 0) or ((jahr%4 == 0) and not (jahr%100 == 0)):
    print("Es ist ein Schaltjahr.")
else:
    print("Es ist kein Schaltjahr.")
input("Beenden mit <Enter>")


