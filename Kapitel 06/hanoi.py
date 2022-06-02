# ---------------------------------------------------
# Dateiname: hanoi.py
# Rekursive Berechnung einer Lösung des Problems
# "Die Türme von Hanoi"
# Python 3
# Kap. 6 Lösung 4
# Michael Weigend 1. 10. 2021
#----------------------------------------------------

def bewege(n, von, nach, über):
        if n==1:
            print ('Lege eine Scheibe von', von, 'nach', nach,'.')
        else:
            bewege(n-1, von, über, nach)
            bewege(1, von, nach, über)
            bewege (n-1, über, nach, von)
        
    
bewege (5,1,2,3)
input("Beenden mit <ENTER>")
