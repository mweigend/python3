#!/usr/bin/env python3
#----------------------------------------------------
# Dateiname:  print_lock.py
# Parallele Prozesse geben einen Text aus
# mit Synchronisation.
#
# Python 3,  mitp Verlag
# Kap. 32
# Michael Weigend 12. 06. 2019
#----------------------------------------------------
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    print('Das ist Prozess', i)
    l.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(4):
         Process(target=f, args=(lock, i)).start()

    
