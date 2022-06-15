#!/usr/bin/env python3
#----------------------------------------------------
# Dateiname:  print_no_lock.py
# Parallele Prozesse geben einen Text aus
# ohne Synchronisation.
#
# Python 3,  mitp Verlag
# Kap. 32
# Michael Weigend 12. 06. 2019
#----------------------------------------------------
from multiprocessing import Process

def f(i):
    print ('Hallo!')
    print('Das ist Prozess', i)

if __name__ == '__main__':

    for i in range(10):
         Process(target=f, args=(i,)).start()

    
