#!/usr/bin/env python3
# Belegungen einer aussagenlogischen Formel
# ---------------------------------------------------
# Dateiname: aussagenlogische_formel.py
# Belegungen einer aussagenlogischen Formel
# Python 3
# Kap. 5 
# Michael Weigend 1. 10. 09
#----------------------------------------------------

print("a b c  (a or b) and c")    # Überschrift
print("---------------------")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            x = (a or b) and c
            print(a, b, c, "   ", int(x))
input()
