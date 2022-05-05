#!/usr/bin/env python
# ------------------------------------------------------
# Dateiname: reise.py
# Berechnung des Kostenplans für eine Reise
#
# Python 3
# Kapitel 3
# Michael Weigend, 15.06.2022
#-----------------------------------------------------
print("Kostenplan für eine Reise")       
print("-------------------------")

# Eingabe
bus = float(input("Kosten für den Reisebus: "))
hotel = float(input("Hotelkosten pro Person: "))
events = float(input("Gesamtkosten für touristische Events: "))
personen = int(input("Anzahl der Teilnehmer: "))

# Verarbeitung
gesamtkosten = bus + events + personen*hotel
kostenProPerson = gesamtkosten/personen

# Ausgabe
print()
print("Die Gesamtkosten betragen", gesamtkosten, "EUR.")
print("Die Kosten pro Person sind", kostenProPerson, "EUR.")

input()

