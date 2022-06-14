#----------------------------------------------------
# Dateiname:  admin.py
# Administration eines Redaktionssystems.
# Die Datenbank-Tabellen für User und Beiträge werden initialisiert
# (falls sie nich nicht existieren).  
# Ausserdem wird die Einrichtung neuer Benutzer ermöglicht.
#
# Dieses Skript muss so gespeichert werden, dass nur
# der Administrator Zugriffsrechte hat 
# 
# Python 3
# Kap. 24  
# Michael Weigend 12.06.2022
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

def user_einfügen(c, name):
# Neuer User wird eingefügt, falls Name noch nicht existiert
    if list(c.execute('''SELECT *
                         FROM person
                         WHERE name = ?;''', (name,))):
        print('Name existiert bereits.')
    else:
        m = hashlib.sha256(name.encode('utf-8'))
        c.execute('''INSERT INTO person
                     VALUES(?, ?);''',
                    (name, m.digest()))
        verbindung.commit()

# Hauptprogramm
verbindung, c = db_einrichten()
user_ausgeben(c)
print ('Neue User anlegen. (Name ist provisorisches Passwort.)')
name = input('Neuer User (Ende mit RETURN): ')
while name:
     user_einfügen(c, name)
     name = input('Neuer User (Ende mit RETURN): ')

print('Datenbank wurde aktualisiert.')
user_ausgeben(c)
c.close()
verbindung.close()

        
