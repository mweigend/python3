# ---------------------------------------------------
# Dateiname: const.py
# Klasse mit Property für Konstante
# Objektorientierte Programmierung mit Python
# Kap. 10
# Michael Weigend 20.9.2009
#----------------------------------------------------
class Const:
    def __init__(self, x):
        self.__x = x

    def getX (self):
        return self.__x

    x = property(getX)
