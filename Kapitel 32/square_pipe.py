#----------------------------------------------------
# Dateiname:  square_pipe.py
# Von einem digitalen Messgerät, dass den Widerstand
# eines Pt-100-Thermometers misst, wird die Display-Anzeige
# (natürliche Zahl) übernommen und daraus die Temperatur berechnet
# und angezeigt.
#
# Python 3,  mitp Verlag
# Kap. 32
# Michael Weigend 12. 06. 2019
#----------------------------------------------------
from multiprocessing import Process, Pipe

def square(i, b):                                             #1                
    b.send(i**2)

if __name__ == '__main__':
   a, b = Pipe()
   p = Process(target=square, args=(3, b))
   p.start()
   result = a.recv()
   p.join()
   print("Ergebnis:", result)
