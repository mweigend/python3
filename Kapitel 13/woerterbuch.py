#----------------------------------------------------
# Dateiname: woerterbuch.py
# Wörter und ihre Häufigkeit in einem Text
#
# Python 3
# Kap. 13
# Michael Weigend 09.05.2022
#----------------------------------------------------
 
# woerterbuch.py
def wörter(text): 
    text = text.lower()
    for p in '.,:-?!;':
        text = text.replace(p,'')                 #1
    liste = text.split()                          #2
    wörterbuch = []
    while liste:                                  #3
        wort = liste[0]
        anzahl = 0
        while wort in liste:                      #4
            liste.remove(wort)
            anzahl += 1
        wörterbuch += [(wort,anzahl)]            #5
        wörterbuch.sort()                        #6
    return wörterbuch

# Aufruf zum Testen der Funktion 
print(wörter('Brautkleid bleibt Brautkleid, Blaukraut bleibt Blaukraut'))

input('Beenden mit <ENTER>')
