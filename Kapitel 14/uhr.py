#----------------------------------------------------
# Dateiname: uhr.py
# Simple Uhr
#
# Python 3  mitp Verlag
# Kap. 14
# Michael Weigend 5.6.2019
#----------------------------------------------------
from time import ctime, sleep
for i in range(5):
    print (ctime().split()[3])   #1
    sleep(1)                     # eine Sekunde schlafen



