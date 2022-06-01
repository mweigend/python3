#! /python310/python.exe                              #1

#----------------------------------------------------
# Dateiname:  cgitb_test.py
# Test des Debugging-Features cgitb
# Achtung!
# Die erste Zeile (Shebang-Zeile) muss angepasst werden!
# Bei Unix-Systemen lautet sie:
#!/usr/bin/env python3    
#
# Python 3 
# Kap. 22
# Michael Weigend 22.06.2020
#----------------------------------------------------
                           

import cgitb
cgitb.enable()
print ("Content-Type: text/html")
print ()
print ("<html><h1>cgitb-Test</h1>")
print (unbekannter_Name)
print ("</html>")














                    
