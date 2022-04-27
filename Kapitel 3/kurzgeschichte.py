#!/usr/bin/env python
# ---------------------------------------------------
# kurzgeschichte.py
# Python 3
# Kap. 3 Lösung Aufgabe 1
# Michael Weigend 01. 05.2022
#----------------------------------------------------

print("Dieses Programm schreibt eine Kurzgeschichte,",
      "in der Sie vorkommen.")
name = input("Wie lautet Ihr Vorname? ")
monat = input("In welchem Monat ist Ihr Geburtstag? ")
haarfarbe = input("Ihre Haarfarbe: ")
ort = input("Ihr Wohnort: ")
print()
print("Die Verabredung mit dem Kommissar")
print()
print("Es war ein grauer Morgen im", monat + ".")
print("Die Sonne war gerade erst aufgegangen",
      "und es war noch wenig Betrieb im Stadtzentrum von",
      ort+".")
print("Hauptkommissar Hartmann stand vor dem Bistro",
      "und schaute auf die Uhr.")
print("Wo bleibt", name, "nur? dachte er. Ist etwas schief gelaufen?")
print("Vielleicht hatte", name+"s",
      "Freundin Wind von der Sache bekommen", 
      "und seine Pläne durchkreuzt.")
print("Eine Person mit struweligen ", haarfarbe+"en",
      "Haaren näherte sich mit raschen Schritten.")
print("Der Kommissar atmete auf, als er den Menschen erkannte.")
print("Es war", name+".")
print("Jetzt konnte eigentlich nichts mehr schief gehen ...")
print()
input("Beenden mit <ENTER>")

