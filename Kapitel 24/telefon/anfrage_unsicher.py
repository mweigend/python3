#----------------------------------------------------
# Dateiname:  anfrage_unsicher.py
#
# Unsicheres Programm, das in der Datenbank
# nach Telefonnummern sucht.
# Das Programm ist unsicher, weil es
# SQL-Injections erlaubt.
# 
# Python 3
# Kap. 24
# Michael Weigend 07.06.222
#----------------------------------------------------
import sqlite3
verbindung = sqlite3.connect('tel.db')
c = verbindung.cursor()
name = input('Name: ')
print(name)
anfrage = ''' SELECT * FROM person
              WHERE name ="{}";'''       #1
c.execute(anfrage.format(name))          #2                   
print(list(c))	
c.close()
verbindung.close()
