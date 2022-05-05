# ---------------------------------------------------
# Dateiname: telemanager.py
# Verwaltung von Telefonnummern 
# Python 3
# Kap. 9 Lösung 3
# Michael Weigend 8. 10. 09
#----------------------------------------------------
import pickle

def erzeugeTel():
    try:                                      #1
        with open("tel.dat", "rb") as f:
            t = pickle.load(f)
    except:
        t = {}                                #2
    return t

def recherche():                              #3
    name = input("Name: ")
    if name in tel.keys():
        print("Nummer: ", tel[name])
    else:
        print("Name unbekannt")

def verabschiedung():                         #4
     print("Danke, dass Sie dieses Produkt verwendet haben.")
     with open('tel.dat', 'wb') as f:
         pickle.dump(tel, f)

def menue():
    eingabe = ""                              #5
    while eingabe not in[ "e" , "E"]:         #6  
        print()
        print("(S)uche nach Telefonnummer")
        print("(N)eue Nummer eintragen")
        print("(A)lle Nummern ausgeben")
        print("(E)nde")
        print
        eingabe = input("Ihre Wahl: ")
        if eingabe in["S", "s"]: recherche()   #7
        elif eingabe in["A", "a"]: ausgeben()
        elif eingabe in["N", "n"]: neu()

def ausgeben():
    print("Name", "Nummer", sep="\t")          #8
    print(30*"_")
    for k in tel.keys():
        print(k, tel[k], sep="\t")

def neu():
    global tel                                 #9
    name = input("Name: ")
    nummer = input("Nummer: ")
    tel[name] = nummer
    print("Neuer Eintrag gespeichert")

# Hauptprogramm
 
tel = erzeugeTel()                             #10
menue()
verabschiedung()
input("Beenden mit <ENTER>")
