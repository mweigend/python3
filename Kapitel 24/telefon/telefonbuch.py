#----------------------------------------------------
# Dateiname:  telefonbuch.py
#
# Aufbau einer kleinen Datenbank mit einer Tabelle.
# Sie modelliert ein Telefonbuch.
# Achtung! Bevor Sie das Programm startenVor jedem Start dieses
# Programms müssen Sie zuerst die Datenbankdatei tel.db löschen.
# Sie wird dann während des Programmlaufs wieder neu erzeugt.
# Python 3
# Kap. 24
# Michael Weigend 07.06.2022
#----------------------------------------------------
import sqlite3
verbindung = sqlite3.connect('tel.db')
c = verbindung.cursor()
c. execute('''CREATE TABLE person(name VARCHAR(50),
                                  telefon VARCHAR(20));''')

c.execute('''INSERT INTO person VALUES("Melanie Beck",
                                      "02302 89912");''')
c.execute('''INSERT INTO person VALUES ("Moritz Blau"  ,
                                        "0201 841111");''')
c.execute('''INSERT INTO person VALUES ("Tim Groß",
                                        "0251 199348");''')

verbindung.commit()
c.close()
verbindung.close()
