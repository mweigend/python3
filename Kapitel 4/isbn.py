#!/usr/bin/env python
# ---------------------------------------------------
# Dateiname: isbn.py
# Berechnung der ISBN-Prüfziffer
#
# Objektorientierte Programmierung mit Python 3
# Kap. 4 Lösung 4
# Michael Weigend 1. 10. 09
#----------------------------------------------------
 

eingabe = input("Geben Sie eine neunstellige ganze Zahl ein: ")
nummer = int(eingabe)
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
summe = z1+2*z2+3*z3+4*z4+5*z5+6*z6+7*z7+8*z8+9*z9
prüfziffer = summe%11
print ("Prüfziffer:", prüfziffer)

input("Beenden mit <ENTER>")
           
