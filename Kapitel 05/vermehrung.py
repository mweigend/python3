#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: vermehrung.py
# Simulation der Vermehrung von Bakterien
# Python 3
# Kap. 5 Loesung 7
# Michael Weigend 1. 10. 09
#----------------------------------------------------

print("Vermehrung von Bakterien")
bakterien = 100
for zeit in range(49):
    print("Stunde",zeit, "  ", bakterien, "Bakterien")
    bakterien *= 4


input("Beenden mit <ENTER>")

    
    
    
