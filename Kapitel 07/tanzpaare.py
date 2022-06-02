#----------------------------------------------------
# Dateiname:  tanzpaare.py
# Eine Raumplan mit Mengen modellieren
# 
# Python 3
# Kap. 7 Lösung Aufgabe 5 
# Michael Weigend 15. 9. 2009
#----------------------------------------------------
damen = set("ABCD")
herren = set("abcd")
tanzlehrer = set("X")
tanzpaare = set(frozenset((d, h))
		for d in damen|tanzlehrer
		for h in herren|tanzlehrer
		if d != h)
for p in tanzpaare:
	print (tuple(p), end=" ")

