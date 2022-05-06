# ---------------------------------------------------
# Dateiname: oeffentlich_privat.py
# Beispiel für öffentliche und private Attribute 
# Python 3
# Kap. 10
# Michael Weigend 05.05.2022
#----------------------------------------------------
class C:
     def __init__ (self):
          self.__privat = "privat"
          self._privat = "schwach privat"
          self.öffentlich = "öffentlich"

c = C()
print(c.öffentlich)
print(c._privat)
print(c.__privat)


