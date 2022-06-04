#----------------------------------------------------
# Dateiname:  primfak.py
# Modul mit Funktion primfak(), die eine
# natuerliche Zahl in Primfaktoren zerlegt.
# Prüfung von Vor- und Nachbedingung.
#
# Python 3  mitp Verlag
# Kap. 21
# Michael Weigend 7.6.2019
#----------------------------------------------------

def primfak(zahl):
      # Prüfe Vorbedingung
      assert type(zahl) == int and zahl > 0
      x = zahl
      fak = [1]
      faktor = 2
      while x > 1:
          while x % faktor == 0:
              fak.append(faktor)
              x /= faktor
          faktor += 1
      # Prüfe Nachbedingung
      produkt = 1
      for i in fak: produkt *= i
      assert produkt == zahl
      return fak

if __name__== '__main__':
    print (primfak(6))
    print (primfak(-2))                            













                    
