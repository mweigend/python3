#----------------------------------------------------
# Dateiname: plattform.py
# Ermittelt Python-Version und Systemplattform.
#
# Python 3  mitp Verlag
# Kap. 14
# Michael Weigend 5.6.2019
#----------------------------------------------------
# plattform.py
import sys
print('Ihre Systemplattform ist',sys.platform) 
print('Python-Version:')
print('Python '+ sys.version)
if sys.version_info.major < 2:                        #1
    print('Sie benötigen für dieses Skript eine neuere Version')
else:
    print('Die Python-Version ist für dieses Skript ausreichend.')



input('Beenden mit <ENTER>')
