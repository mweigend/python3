# ---------------------------------------------------
# Dateiname: marathon.py
# Abspeichern der Ankunftzeiten von Rennläufern
# Python 3
# Kap. 9 Lösung 1
# Michael Weigend 8. 10. 09
#----------------------------------------------------
# marathon.py
import time
print("Marathon")
print()
nummer = "  "                                             #1
with open("daten.txt", "w") as daten:
    while nummer != "":
        nummer = input("Startnummer (Ende mit <Enter>): ")
        daten.write(nummer + ": " + time.asctime() + "\n")#2
        daten.flush()                                     #3
print()
print("Die Daten befinden sich in der Datei daten.txt")


                
    
