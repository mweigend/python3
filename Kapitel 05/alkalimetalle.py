#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: alakalimetalle.py
# 
# Objektorientierte Programmierung mit Python 3
# Kap. 5 Lösung 3
# Michael Weigend 1. 10. 09
#----------------------------------------------------

print("Bitte geben Sie das Symbol eines Elementes an.")
element = input("Element: ")
if element in ["Li", "Na", "K", "Rb", "Cs"]:
    print("Es handelt sich um ein Alkalimetall.")
else:
    print("Es handelt sich nicht um ein Alkalimetall.")

input("Beenden mit <Enter>")
