#----------------------------------------------------
# Dateiname:  anfrage_alle_daten.py
#
# Alle Zeilen einer Tabelle werden ausgegeben.
# 
# Python 3
# Kap. 24
# Michael Weigend 07.06.2022
#----------------------------------------------------
import sqlite3
verbindung = sqlite3.connect('tel.db')
c = verbindung.cursor()
c.execute('SELECT * FROM person;')
for zeile in c:                        #1
	print(zeile)
c.close()
verbindung.close()
