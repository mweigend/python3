#!/usr/bin/enc python3
#----------------------------------------------------
# Dateiname:  wdj.py 
# Modul mit Klasse Responder zur Wahl des "Wortes des Jahres"
# 
# Python 3
# Kap. 25
# Michael Weigend 08.06.2019
#----------------------------------------------------

import cgi                                            #1
from ranking import *

START = """
<html>
<head>
<title>Wort des Jahres</title>
</head>
<body bgcolor =#C0C0C0>
<font face="VERDANA,ARIAL,HELVETICA">
<h2>Suche nach dem Wort des Jahres</h2>
Bitte geben Sie Ihren Vorschlag ein und klicken
Sie auf die Schaltfl&auml;che.
<form method="POST">
  Mein Wort des Jahres:
  <input type="Text" name="word"  size="25"/> <br/>
  <input type="Submit" value="Abschicken"/>
</form>
</font>
</body>
</html>"""                                            #2

                                                     
RESPONSE = """
<html>
<head><title>Wort des Jahres</title></head>
<body >
<font face="VERDANA,ARIAL,HELVETICA">
<h2> Danke f&uuml;r Ihr Votum!</h2>
Hier sind die bisherigen Favoriten: <br/>
{} <br/>
Ihr Vorschlag <i>{}</i> steht auf Platz {}.<br/>
</font>
</body>
</html>"""                                             #3                                                                   

PATH = "words.txt"

class Responder:
  def __init__ (self, datafile):               
    self.ranking = Ranking(datafile)                   #4

  def __call__(self, environ, start_response):         #5
    if environ["REQUEST_METHOD"] == "POST":
        form = cgi.FieldStorage(
            fp=environ["wsgi.input"],             
            environ=environ,
            keep_blank_values=True)                    #6
        word = form.getvalue("word")                   #7                    
        self.ranking.add(word)                         #8
        self.ranking.save()
        topFive = self.ranking.getTop(5)               #9
        rank = self.ranking.getRank(word)
        content = RESPONSE.format(topFive, word, rank) #10 
    else:
        content = START                                #11   
    response_headers = [
         ("Content-type", "text/html; charset=utf-8"),
         ("Content-Length", str(len(content)))] 
    status = "200 OK"    
    start_response(status, response_headers)
    return [content.encode('utf-8')] 

application = Responder(PATH)                          #12
                               
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, application)
    print('Serving on port 8000... ')
    httpd.serve_forever()


