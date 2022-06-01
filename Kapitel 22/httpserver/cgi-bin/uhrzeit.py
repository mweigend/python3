#! /python310/python.exe
#----------------------------------------------------
# Dateiname:  uhrzeit.py 
# CGI-Skript, das html-Seite mit aktueller Uhrzeit ausgibt
# Achtung!
# Die erste Zeile (Shebang-Zeile) muss angepasst werden!
# Bei Unix-Systemen lautet sie so:
#!/usr/bin/env python3   
#
# Python 3
# Kap. 22
# Michael Weigend 22.05.2022
#----------------------------------------------------
SCHABLONE = """Content-type: text/html; char-set=utf-8

<html>
  <body>
    <h2>Die aktuelle Uhrzeit </h2>
      Es ist {} Uhr und {} {}.
  </body>
</html>"""         #1
    
import cgitb
cgitb.enable()
from time import localtime
zeit = localtime()
h = zeit[3]
m = zeit[4]
if m == 1:
    m_text = "Minute"
else:
    m_text = "Minuten"

print(SCHABLONE.format(h, m, m_text))
