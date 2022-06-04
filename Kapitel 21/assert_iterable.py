#----------------------------------------------------
# Dateiname:  assert_iterable.py 
# Beispiel für assert-Anweisung zum Testen von Vorbedingungen
#
# Python 3  mitp Verlag
# Kap. 21
# Michael Weigend 7.6.2019
#----------------------------------------------------


def diversität(s):
   # liefert die Anzahl unterschiedlicher Elemente einer Kollektion
   assert hasattr(s, '__iter__')
   assert len(s) > 0
   menge = set(s)
   return len(menge)


if __name__ == '__main__':
   print(diversität('Barbara'))
   print(diversität(110))
         
      
   
   

         










                    
