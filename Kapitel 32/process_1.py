#!/usr/bin/env python3
#----------------------------------------------------
# Dateiname:  process_1.py
# Zwei parallele Prozesse werden ausgeführt und die
# Prozess-IDs ausgegeben.
#
# Python 3,  mitp Verlag
# Kap. 32
# Michael Weigend 12. 06. 2019
#----------------------------------------------------
from multiprocessing import Process
import os

def hello():
    print("Prozess-ID: {}, Name: {}".format(
               os.getpid(), __name__))    #1

if __name__ == "__main__":
   p1 = Process(target=hello)             #2
   p1.start()                             #3
   p2 = Process(target=hello)
   p2.start()
   hello()                                #4
   

