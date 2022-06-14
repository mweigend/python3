#----------------------------------------------------
# Dateiname:  anfrage_interaktiv.py
#
# Interaktives Programm, das in der Datenbank
# nach Telefonnummern sucht
# 
# Python 3
# Kap. 24
# Michael Weigend 07.06.2019
#----------------------------------------------------
import sqlite3
verbindung = sqlite3.connect('tel.db')
c = verbindung.cursor()
ANFRAGE = ''' SELECT * FROM person
              WHERE name LIKE ?;'''
AUSGABE = 'Name: {}, Telefon: {}'

name = input('Name: ')
while name:      
    c.execute(ANFRAGE, ('%{}%'.format(name), ))
    for zeile in c:                        #1
        print(AUSGABE.format(zeile[0], zeile[1]))
    name = input('Name: ')

print('Auf Wiedersehen!')	
c.close()
verbindung.close()
