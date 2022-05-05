#----------------------------------------------------
# Dateiname:  test_finally.py
# Auch wenn das Speichern einer Datei nicht gelingt, wird sie
# in jedem Fall im Unterverzeichis temp gespeichert
# Kap. 9
# Michael Weigend 22.04.2022
#----------------------------------------------------

daten = input('Daten: ')
verzeichnis = input('Verzeichnis: ')
dateiname = input('Dateiname: ')
try:
    f = open(verzeichnis + '/' + dateiname, 'w')     #1
    f.write(daten)
    f.close()
    print('Daten gespeichert')
finally:
    f = open('temp/daten.bak', 'w')
    f.write(daten)
    f.close()
    print('Sicherheitskopie im Verzeichnis "temp"')
print('Programm beendet')











                    
