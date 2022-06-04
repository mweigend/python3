#----------------------------------------------------
# Dateiname:  qsort1.py 
# Modul mit Funktion quicksort(), die eine Liste sortiert
# Einige Programmzeilen sind auskommentiert
# Python 3  mitp Verlag
# Kap. 21
# Michael Weigend 7.6.2022
#----------------------------------------------------


import random
def quicksort(s):
##  if len(s) > 0:                                      #1
##      print ("Ich sortiere: ", s)
##      print ("Element zum Spalten der Liste: ",s[0])

  if len(s) <= 1: return s
  else:
    return quicksort( [ x for x in s[1:] if x < s[0]])\
        + [s[0] ]  \
        + quicksort( [ y for y in s[1:] if y >= s[0]])

if __name__== '__main__':                             #2
    s = [random.randint(0, 100) for i in range(8)] 
    print (quicksort(s))
    input('Beenden mit <ENTER>')











                    
