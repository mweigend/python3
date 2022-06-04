
#----------------------------------------------------
# Dateiname:  assert_liste.py 
# Beispiel für assert-Anweisung zum Testen von Vorbedingungen
#
# Python 3  mitp Verlag
# Kap. 21
# Michael Weigend 7.6.2019
#----------------------------------------------------


def entferneMin(s):
   assert type(s) == list
   assert len(s) > 0
   m = min(s)
   s.remove(m) 
   
   
if __name__ == '__main__':
   zahlen = [1, 2, 2, 3, 1, 8, 9, 100]
   print(zahlen)
   entferneMin(zahlen)
   print(zahlen)
   entferneMin([])
         










                    
