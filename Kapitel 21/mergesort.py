#----------------------------------------------------
# Dateiname:  mergesort.py 
# Modul mit Funktionen msort() und merge(), die eine Liste 
# nach dem mergesort-Algorithmus dokumentieren.
#
# Python 3  mitp Verlag
# Kap. 21
# Michael Weigend 7.6.2019
#----------------------------------------------------


import logging
logging.basicConfig(filename="tmp/logging.txt",level=logging.DEBUG,
                    filemode="w")


def merge(s1, s2):
  logging.debug("Starte merge({}, {}): ".format(
                    str(s1), str(s2)))
  if s1 == []: ergebnis = s2
  elif s2 == []: ergebnis = s1
  else:
      a, b = s1[0], s2[0]
      if a <= b: ergebnis = [a] + merge(s1[1:], s2)
      else: ergebnis = [b] + merge(s1, s2[1:])


  logging.debug("Ergebnis von merge({}, {}): {}".format(
                     str(s1), str(s2), str(ergebnis)))
  return ergebnis
  
          
def msort (s):
  logging.info("msort({})".format(str(s)))
  if len(s) <= 1: ergebnis = s
  else:
     n = len(s)//2
     s1 = s[:n]
     s2 = s[n:]
     ergebnis = merge(msort(s1), msort(s2))
  logging.info("Ergebnis von msort({}): {}".format(
                    str(s), str(ergebnis)))
  return ergebnis


if __name__ == "__main__":
    s = [7, 13, 15, 1, 12, 11, 3, 6, 10, 2, 8, 14, 0, 4, 9, 5]
    print(msort(s))
    
  
       
