#----------------------------------------------------
# Dateiname: verzeichnis.py
# Gibt Namen der Dateien im Arbeitsverzeichnis aus
#
# Python 3  mitp Verlag
# Kap. 14
# Michael Weigend 5.6.2019
#----------------------------------------------------
import os
for datei in os.listdir(os.getcwd()):
      zeile = '{datei:>30}{bytes:>10} byte'.format(
                       datei=datei,
                       bytes=os.path.getsize(datei))
      print(zeile)

