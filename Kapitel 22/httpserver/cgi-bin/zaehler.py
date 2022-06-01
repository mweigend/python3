#! /Python310/python.exe                               #1

#----------------------------------------------------
# Dateiname:  zaehler.py 
# CGI-Skript, das eine html-Seite generiert. Es merkt sich
# in einem Cookie, wie oft der Client diese Seite schon besucht hat.
# Achtung!
# Die erste Zeile (Shebang-Zeile) muss angepasst werden!
# Bei Unix-Systemen lautet sie:
#!/usr/bin/env python3  
# 
# Python 3
# Kap. 22
# Michael Weigend 22.05.2022
#----------------------------------------------------
 
import  os
from http.cookies import SimpleCookie
# Stringkonstanten
antwort1 = """<h3> Willkommen!</h3>
Sie besuchen diese Seite zum ersten Mal."""
antwort2 = """<h3> Sch&ouml;n, dass Sie wieder hier sind!</h3>
Sie besuchen zum {}. Mal diese Seite."""
httpPaket = """Content-Type: text/html
{}

<html>
<head><title>Z&auml;hler</title></head>
<body>
{}
</body>
</html>"""                                             #1

class Zaehler(object):
  def __init__(self):
    self.c = SimpleCookie()                            #2
    try:
      self.c.load(os.environ["HTTP_COOKIE"])           #3
      self.c["zaehler"] = int(self.c["zaehler"].value)+1
    except:
      self.c["zaehler"] = 1                            #4
    self.besuche=self.c["zaehler"].value
    
  def __str__(self):
    if self.besuche == '1': antwort = antwort1         #5
    else: antwort = antwort2.format(self.besuche)      #6
    return httpPaket.format(self.c, antwort)           #7

print(Zaehler())















                    
