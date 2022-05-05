# ---------------------------------------------------
# Dateiname: caesar.py
# Verschlüsselung mit Verschiebechiffre (Caesars Algorithmus)
# Objektorientierte Programmierung mit Python
# Achtung! Das Programm muss mit zwei Kommandozeilenargumenten
# aufgerufen werden (z.B. python caesar.py Bein 2)
# Kap. 9 
# Michael Weigend 8. 10. 09
#----------------------------------------------------
# caesar.py
import sys
klartext = sys.argv[1]             #1
n = int(sys.argv[2])     
chiffriert = ""
klartext = klartext.upper()        #2
for c in klartext:
    nr = ord(c) + n                #3
    if nr > ord("Z"):              #4
        nr -= 25
    if c != " ":
        chiffriert += chr(nr)
    else:
        chiffriert += " "          #5
print(chiffriert)

