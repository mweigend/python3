# ---------------------------------------------------
# Dateiname: chartsmanager.py
# Erstellen einer Hitparade
# Python 3
# Kap. 7
# Michael Weigend 8. 10. 09
#----------------------------------------------------

# Funktionsdefinitionen
def eingabe(charts):
    print ("Eintragungen (mit ENTER beenden)")
    titel = input("Titel: ")
    while titel:                               #1
        interpret = input("Interpret: ")
        charts += [[0,titel, interpret]]
        titel = input("Titel: ")
    print()
    print("Vielen Dank. Die Liste wird gespeichert")

def speichern (charts):
    import pickle                              #2
    f = open("charts.txt", "wb")               #3
    pickle.dump(charts, f)                     #4
    f.close()                                  #5

def ausgabe(charts):
    print("Die Charts")
    print("----------")
    for i in range (len(charts)):              #6
        eintrag = charts[i]
        print("Platz", i+1, ":", eintrag[1], "\t von",
              eintrag[2], "\t", eintrag[0], "Stimmen")

# Hauptprogramm
print("Erstellen Sie eine Hitliste.")
charts = []
eingabe(charts)
ausgabe(charts)
speichern(charts)


input("Beenden mit <ENTER>")

