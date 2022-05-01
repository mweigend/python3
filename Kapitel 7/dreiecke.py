# ---------------------------------------------------
# Dateiname: dreiecke.py
# Python 3
# Kap. 7 Aufgabe 4
# Michael Weigend 1. 10. 03
#----------------------------------------------------
dreiecke = set(frozenset((a, b, c)) 
                   for a in range(1,20)
                   for b in range(1,20)
                   for c in range(1,20)
                   if a**2 + b**2 == c**2)
for d in dreiecke:
    print (tuple(d), end=" ")


input("Beenden mit <ENTER>")


