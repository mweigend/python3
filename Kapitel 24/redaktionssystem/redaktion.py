#! /usr/bin/env python3                                    #1
#----------------------------------------------------
# Dateiname:  redaktion.py
#
# WSGI-Skript, das Teil eines online-Redaktionssystems ist.
# Das WSGI-Skript verarbeitet folgende Variablen,
# die vom aufrufenden Client gesendet werden:
# name, passwort, neuespass, neupass1, neupass2
# titel, text, haltbar (Anzahl der Tage)
#
# Ermöglicht wird die Änderung des Passwortes des Redakteurs
# und /oder die Edition eines Beitrages für das Online-Journal.
# 
# Python 3
# Kap. 24
# Michael Weigend 07.06.2022
#----------------------------------------------------

import sqlite3, cgi, hashlib, time, logging, sys

# Schablone für HTML-Seite
# Platzhalter {}: Name, Passwort, Text, Fehler im Beitrag,
# Fehler im Passwort

SEITE1 = '''
<html>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<head>
  <title>Python-Redaktionssystem</title>
</head>
<body bgcolor=#C0C0C0>
  <h2>Python-Redaktionssystem</h2>
  <form method="POST" >
    <input type="hidden" name="name" value="{}">     
    <input type="hidden" name="passwort" value="{}">
    <b>Titel: </b>
    <input type="Text" name="titel"
           size="50" maxlength="80"><br><br>
    <textarea name="text" cols="50" rows="8" >{}
    </textarea><br>
    <h4>Haltbarkeit</h4>
    <input type="Radio" name="haltbar" value="14"
     checked="checked">
    2 Wochen <br>
    <input type="Radio" name="haltbar" value="30">
    1 Monat <br>
    <input type="Radio" name="haltbar" value="90">
    3 Monate <br>
    <input type="Radio" name="haltbar" value="180">
     6 Monate <br>
    <h4> Passwortverwaltung</h4>
    <input type="Checkbox" name="neuespass" value="1">
    Passwort &auml;ndern<br>
    <input type="Password" name="neupass1" > Neues Passwort<br>
    <input type="Password" name="neupass2" > Passwort wiederholen<br>
    <input type="Submit" value="Absenden">
  </form>
  <i>{}<br>{}<br></i>    
</body></html>'''

# HTML-Seite mit Fehlermeldung bei falschem Login
SEITE2 = '''
<html>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<head><title>Rython-Redaktionssystem</title>
<meta http-equiv="Content-Type" content="charset=utf-8" />
</head>
<body bgcolor=#C0C0C0>
<h2> Python-Redaktionssystem</h2>
<form method="POST">
Name: <input type="Text" name="name" >&nbsp;
Passwort: <input type="Password"
name="passwort"><br><br>
<input type="Submit" value="Login">
</form>
<b> Login gescheitert! &Uuml;berpr&uuml;fen Sie Name und
Passwort.<b>
</body></html>'''

# Schablone für Webseite (Publikation)
# Platzhalter {}: Zeit und Beiträge
WEBSEITE = '''<html>
<head><title>Python-News</title></head>
<body>
<h1>Python-News</h1>
Letzte &Auml;nderung: {}
{} 
</body></html>'''

# Schablone für Beitrag
# Platzhalter {}: Titel, Autor und Text
BEITRAG = '''<h3>{}</h3>
<h4>von {}</h4>
<p>{}</p>'''

class Person:                                        #3
  def __init__(self, form, db):
    self.name = form.getvalue('name')
    self.pw = form.getvalue('passwort')
    self.db = db

  def id_ok(self):                                   #4
    try:
        verbindung = sqlite3.connect(self.db)
        c = verbindung.cursor()
        c.execute('''SELECT hash
                     FROM person
                     WHERE name = ?;''', (self.name,))
        print('Mit Datenbank verbunden.')
        for zeile in c:
            hash_db = zeile[0]                       #5
        pw_bytes = self.pw.encode('utf-8')           #6 
        hash_pw = hashlib.sha256(pw_bytes).digest()
        c.close()
        verbindung.close()
        return hash_db == hash_pw                    #7

    except:
        return False

  def aktualisiere_pw(self, form):                   #8
    neupw1 = form.getvalue('neupass1', '')
    neupw2 = form.getvalue('neupass2', '')
    if neupw1 == neupw2: 
        self.pw = neupw1
        verbindung = sqlite3.connect(self.db)
        c = verbindung.cursor()
        c.execute('''UPDATE person
                     SET hash = ?
                     WHERE name = ?;
                 ''',
                (hashlib.sha256(self.pw.encode('utf-8')).digest(),
                 self.name))
        verbindung.commit()
        c.close()
        verbindung.close()
        return 'Passwort ge&auml;ndert.'
    else:
        return 'Fehler! Passw&ouml;rter nicht gleich!'
    
class Beitrag:                               #9
    def __init__(self, form, autor, db):
      self.text = self.titel = ""
      self.db = db
      self.autor = autor
      if 'titel' in form.keys():
        self.text = form.getvalue('text')
        self.titel = form.getvalue('titel')
        sekunden = float(form.getvalue('haltbar')) *24*3600
        self.verfallsdatum = sekunden + time.time()

    def publiziere(self):
        if self.titel:                               #10
          verbindung = sqlite3.connect(self.db)
          c = verbindung.cursor()
          c.execute('''SELECT *
                       FROM beitrag
                       WHERE titel = ?;''',
                     (self.titel,))
          if not list(c):                           #11
            c.execute('''INSERT INTO beitrag
                         VALUES(?, ?, ?, ?);''',
                      (self.titel, self.text,
                       self.verfallsdatum,
                       self.autor.name))
            print('Gespeichert: ' + self.titel)
            verbindung.commit()
            self.text = ''
            self.titel = ''
            meldung = 'Beitrag wurde gespeichert.'
          else:
            meldung = 'Titel existiert bereits.'
          c.close()
          verbindung.close()
        else: meldung = ''
        return meldung

    def aktualisiere_news(self, news_pfad):
        # HTML-Datei mit Journal aktualisieren
        verbindung = sqlite3.connect(self.db)
        c = verbindung.cursor()
        beiträge = list(c.execute('''select * FROM beitrag;'''))
        pubtext = ''
        for (titel, text,  verfallsdatum, 
             autor) in beiträge:                   #12
          if time.time() < float(verfallsdatum):    
            pubtext += BEITRAG.format(titel, autor, text)
          else:                                     #13
            c.execute('''DELETE FROM beitrag
                         WHERE titel = ?;''', (titel,))
        verbindung.commit()
        c.close()
        verbindung.close()
        # Speichern
        f = open(news_pfad, 'w')
        f.write(WEBSEITE.format(time.asctime(), pubtext))
        f.close()

# Konstanten
DB = 'redaktion.db'
NEWS_PFAD = 'html/news.html'

# WSGI Applikationsfunktion
def application(environ, start_response):
  status = '200 OK' 
  form = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=environ,
            keep_blank_values=True)

  redakteur = Person(form, DB)                    #14
  beitrag = Beitrag(form, redakteur, DB)                         
  beitragfehler = ''                              #15
  pwfehler = ''
  if redakteur.id_ok():                           #16
      beitragfehler = beitrag.publiziere()
      beitrag.aktualisiere_news(NEWS_PFAD)
      if 'neuespass' in form.keys():
          pwfehler = redakteur.aktualisiere_pw(form)
      content_string = SEITE1.format(redakteur.name,
                                     redakteur.pw,
                                     beitrag.text,
                                     beitragfehler,
                                     pwfehler)
      content = content_string.encode('utf-8')  
  else:
      content = SEITE2.encode('utf-8')

  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(content)))]
  start_response(status, response_headers)
  return [content]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, application)
    print('Serving on port 8000... ')
    httpd.serve_forever()














                    
