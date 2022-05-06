#----------------------------------------------------
# Dateiname: flaeche_fehler.py
# Demonstration eines typischen Fehlers
#
# Objektorientierte Programmierung mit Python
# Kap. 10 
# Michael Weigend 05.05.2022
#----------------------------------------------------
 
class Rechteck: 
   def __init__(self, länge, breite):
       self.länge = länge
       self.breite = breite

   def fläche (self):
       return self.länge*self.breite

a = Rechteck(2, 1)
b = Rechteck(1, 2)
print(a.fläche == b.fläche)                          #1
print(a.fläche() == b.fläche()) 


