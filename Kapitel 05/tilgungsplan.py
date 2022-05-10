#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: tilgungsplan.py
# 
# Python 3
# Kap. 5 Lösung 6
# Michael Weigend 1. 03. 2017
#----------------------------------------------------
import time 
print("Berechnung des Tilgungsplans für einen Kredit")
print()
schulden = float(input("Kreditsumme in Euro: "))
zinssatz = float(input("Zinssatz (Prozent pro Jahr): "))
rueckzahlung  = float(input ("Jährliche Rückzahlung in Euro: "))
jahr = time.localtime()[0]
while schulden > rueckzahlung:
    zinsen = schulden * zinssatz/100
    tilgung = rueckzahlung - zinsen
    schulden = schulden - tilgung
    jahr += 1
    print(jahr,  " Zinsen:", round(zinsen), "EUR",
         " Tilgung:", round(tilgung), "EUR", " Restschulden:",
         round(schulden), "EUR")
print("Restforderung:", round(schulden), "Euro")


input("Beenden mit <ENTER>")
    
    
