#!/usr/bin/env python3
#----------------------------------------------------
# Dateiname:  httpd.py 
# HTTP-Server, der CGI-Skripte verarbeiten kann.
# Die CGI-Skripte müssen in einem Unterverzeichnis des
# Verzeichnisses sein, in dem die Programmdatei des Servers ist.
# Dieses Unterverzeichnis hat den Namen cgi-bin.
#
# Python 3 
# Kap. 22
# Michael Weigend 17. 2. 2019
#----------------------------------------------------


from http.server import HTTPServer, CGIHTTPRequestHandler
PORT = 8000
serveradresse =("", PORT)                             #1
server=HTTPServer(serveradresse,
                  CGIHTTPRequestHandler)              #2
server.serve_forever()                                #3
print("Serving on port ", PORT)













                    
