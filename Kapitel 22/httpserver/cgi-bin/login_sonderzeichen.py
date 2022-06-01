#! /Python310/python.exe                               #1

#----------------------------------------------------
# Dateiname:  login_sonderzeichen.py 
# CGI-Skript, das Formular mit Login-Name und Passwort
# bearbeitet
# Achtung!
# Die erste Zeile (Shebang-Zeile) muss angepasst werden!
# Bei Unix-Systemen lautet sie:
#!/usr/bin/env python3  
#
# Python 3
# Kap. 22
# Michael Weigend 22.05.2022
#----------------------------------------------------
                           
import cgi, cgitb
cgitb.enable()
HTML = {ord('ä'): '&auml;', ord('ö'): '&ouml;',
        ord('ü'): '&uuml;', ord('Ä'): '&Auml;',
        ord('Ö'): '&Ouml;', ord('Ü'): '&Uuml;',
        ord('ß'): '&szlig;'}                          #1



SCHABLONE = '''Content-type: text/html; charset=utf-8

<html>
<head><title> Login-Seite </title></head>
<body>
<h3>Herzlich willkommen, {} {}!</h3>
</body>
</html>'''                                           #2                                          

form = cgi.FieldStorage()                            #3
vorname = form.getvalue('vorname')                   #4
name = form.getvalue('name')
print(SCHABLONE.format(vorname.translate(HTML),
                  name.translate(HTML)))               #5













                    
