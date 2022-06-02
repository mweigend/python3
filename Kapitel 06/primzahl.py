# ---------------------------------------------------
# Dateiname: primzahl.py
# Prüft, ob eine Zahl Primzahl ist
# Python 3
# Kap. 6 
# Michael Weigend Januar 2013
#----------------------------------------------------
def primzahl(zahl):
    if zahl <= 1:
        prim = False                   # 1 ist keine Primzahl
    elif zahl == 2:
        prim = True                    # 2 ist Primzahl
    else:
        for i in range(2, zahl//2 + 1):
            if zahl % i == 0:          # Teiler gefunden
                prim = False
                break
            else:
                prim = True            # kein Teiler gefunden
    return prim



            
if __name__ == '__main__':
    z = input('Zahl: ')

    print (primzahl (int(z)))
    input('Beenden mit <ENTER>')
