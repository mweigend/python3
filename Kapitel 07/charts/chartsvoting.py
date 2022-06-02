# ---------------------------------------------------
# Dateiname: chartsvoting.py
# Abstimmen für eine Hitparade
# Python 3
# Kap. 7
# Michael Weigend 8. 10. 09
#----------------------------------------------------
import pickle
# Funktionsdefinitionen
def laden():
    try:
        f = open("charts.txt","rb")    #1
        charts = pickle.load(f)                    #2
        f.close()                                  #3
    except:
        charts = []                                #4
    return charts

def ausgabe(charts):
    print("Die Charts")
    print("----------")
    for i in range (len(charts)):
        eintrag = charts[i]
        print("Platz", i+1, ":", eintrag[1], "\t von",
               eintrag[2], "\t", eintrag[0], "Stimmen")

def voting(charts):
    if charts == []:
        print("Sorry, keine Wahl möglich.")
    else:                                        
        print("Die Charts")
        print()
        ausgabe(charts)
        print("Bitte wählen Sie Ihren Favoriten!",
              "(1 bis "+str(len(charts))+")")     
        wahl = int(input("Nummer: ")) - 1             #5
        charts[wahl][0] += 1                          #6
        charts.sort(reverse=True)                     #7
        print("Vielen Dank! Ihr Voting wird gespeichert.")

def speichern (charts):
    f = open("charts.txt", "wb")
    pickle.dump(charts, f)
    f.close()
  
# Hauptprogramm
charts = laden()
voting(charts)
speichern(charts)
print("Hier der neue Stand:")
ausgabe(charts)



input("Beenden mit <ENTER>")


