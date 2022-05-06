# ---------------------------------------------------
# Dateiname: statisch.py
# Beispiel für die Definition statischer Methoden
# Python 3
# Kap. 10
# Michael Weigend 2.6.2019
#----------------------------------------------------
class Statistik:
    def mittelwert(s):
        if s:
            return float(sum(s)) / len(s)

    def spannweite(s):
        # größte minus kleinste Zahl der Zahlenliste s
        if s:
            return max(s) - min(s)

    def median(s):
        if s:
            s1 = sorted(s)
            if len(s)%2==0: # Länge ist gerade
                return (s1[len(s)//2-1] + s1[len(s)//2])/2.0
            else:
                return s1[(len(s)-1)//2]

    
    mittelwert = staticmethod(mittelwert)
    spannweite = staticmethod(spannweite)
    median = staticmethod(median)
    

s = [1, 4, 9, 11, 5]
print(Statistik.mittelwert(s))
print(Statistik.median(s))
print(Statistik.spannweite(s))

