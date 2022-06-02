# ---------------------------------------------------
# Dateiname: heron.py
# Wurzelberechnung nach Heron
# Python 3
# Kap. 6 Lösung 3
# Michael Weigend Januar 2013
#----------------------------------------------------
def wurzel(x, n=10):
    if n == 1:
        return 1
    else:
        return 0.5*(wurzel(x,n-1)+float(x)/wurzel(x,n-1))
    
print (wurzel(2))
input("Beenden mit <ENTER>")
