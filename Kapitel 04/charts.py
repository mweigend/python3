#!/usr/bin/env python
# ---------------------------------------------------
# Dateiname: charts.py
# 
# Python 3,  mitp Verlag
# Kap. 4, Lösung 4
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

# charts.py
print("Bitte geben Sie die ersten Titel der Charts ein!")
charts = []
titel = input("Titel: ")
charts += [titel]
titel = input("Titel: ")
charts += [titel]
titel = input("Titel: ")
charts += [titel]
print
print("Hier sind die ersten drei Titel der Charts:")
print("Platz 1:", charts[0])
print("Platz 2:", charts[1])
print("Platz 3:", charts[2])
print()  # leere Zeile
input("Beenden mit <ENTER>")

