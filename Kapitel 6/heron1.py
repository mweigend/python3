# ---------------------------------------------------
# Dateiname: heron1.py
# Wurzelberechnung nach Heron - schnellere Version
# Python 3
# Kap. 6 Lösung 3
# Michael Weigend Januar 2013
#----------------------------------------------------
def wurzel(x, n=20):
    if n == 1:
        return 1
    else:
        vorigeNäherung = wurzel(x,n-1)
        return 0.5*(vorigeNäherung+float(x)/vorigeNäherung)
    
print (wurzel(2))
input("Beenden mit <ENTER>")
