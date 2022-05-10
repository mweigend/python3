#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: zahl_eingabe.py
# 
# Python 3
# Michael Weigend 1. 10. 09
#----------------------------------------------------

print("Bitte geben Sie eine Zahl zwischen 1 und 10 ein.")
while True:
    zahl = input("Zahl: ")
    if 1 <= int(zahl) <= 10:
        break  # Zahl ist in Ordnung
    else:
        print ("Die Zahl muss zwischen 1 und 10 liegen.")
print("Danke für die Zahl.")

input()
        

