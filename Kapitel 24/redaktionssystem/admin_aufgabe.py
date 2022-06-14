#----------------------------------------------------
# Dateiname:  admin_azfgabe.py
# Administration eines Redaktionssystems.
#
# Funktionen:
# Datenbank-Dateien für User und Beiträge werden initialisiert
# Einrichtung eines neuen Benutzers
# Entfernen eines Benutzers aus der Datenbank
#
# Hinweis: Dieses Skript muss so gespeichert werden, dass nur
# der Administrator Zugriffsrechte hat 
# 
# Python 3
# Kap. 24  Lösung 2
# Michael Weigend 11.06.2022
#----------------------------------------------------

import sqlite3, hashlib
DB_PFAD = 'redaktion.db'

def db_einrichten():
    verbindung = sqlite3.connect(DB_PFAD)
    c = verbindung.cursor()
    try:
        c.execute("SELECT * FROM person")
        c.execute("SELECT * FROM beitrag")
    except:
        # Tabellen existieren noch nicht
        c.execute('''CREATE TABLE
                       person(name VARCHAR(50),
                              hash BINARY(32));''')
        c.execute('''CREATE TABLE
                       beitrag(titel VARCHAR(100),
                               text VARCHAR(1000),
                               verfallsdatum FLOAT,
                               autor VARCHAR(50));''')
        verbindung.commit()
    return verbindung, c

def user_ausgeben(c):
# Ausgabe aller User-Namen
    print('Liste der User-Namen:')
    c.execute('SELECT * FROM person;')
    for name, pw_hash in c:
        print (name)

def user_einfügen(c):
# Neuer User wird eingefügt, falls Name noch nicht existiert
    print ('Neue User anlegen. (Name ist provisorisches Passwort.)')
    name = input('Neuer User: ')
    if list(c.execute('''SELECT *
                         FROM person
                         WHERE name = ?;''', (name,))):
        print('Name existiert bereits.')
    else:
        m = hashlib.sha256(name.encode('utf-8'))
        c.execute('''INSERT INTO person
                     VALUES(?, ?);''',
                    (name, m.digest()))


def user_löschen(c):
# User löschen
    name = input('Name: ')
    if list(c.execute('''SELECT *
                         FROM person
                         WHERE name = ?;''', (name,))):    #1
        c.execute('''DELETE FROM person
                        WHERE name = ?;''', (name,))       #2
        print(name, 'wurde aus der Datenbank entfernt.')
    else:
        print(name, 'existiert nicht in der Datenbank.')
    

# Hauptprogramm
verbindung, c = db_einrichten()
wahl = 'x'
while wahl not in ['e', 'E']:
    user_ausgeben(c)  
    print ('-----------------------------')
    print ('(n)eu    (l)öschen    (E)nde')
    wahl = input ('Wahl: ')
    if wahl in ['n', 'N']:
        user_einfügen(c)
    elif wahl in ['l', 'L']:
        user_löschen(c)
    verbindung.commit()                                     #3
print ('Auf Wiedersehen...')
c.close()
verbindung.close()

        
