# ---------------------------------------------------
# Dateiname: newlist.py
# Klasse NewList, von Basisklasse list abgeleitet
# Objektorientierte Programmierung mit Python
# Kap. 10
# Michael Weigend 20.4.2006
#----------------------------------------------------
class Newlist(list):
    def __init__(self, s=[]):
        s = list(s)
        list.__init__(self, s )

    def range(self):
        try:
            return max(self) - min(self)
        except: return 0
        




