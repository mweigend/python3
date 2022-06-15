#----------------------------------------------------
# Dateiname:  process_2.py
# Der Hauptprozess startet einen Prozess und wartet
# bis er beendet ist (join).
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 32
# Michael Weigend 24.10.2016
#----------------------------------------------------
from multiprocessing import Process

def hello():
    print("Hello")

if __name__ == "__main__":
   p = Process(target=hello)
   p.start()
   p.join()
   print("Prozess beendet")
   

