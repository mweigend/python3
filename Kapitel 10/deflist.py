# ---------------------------------------------------
# Dateiname: Defist.py
# Klasse NewList, von Basisklasse list abgeleitet
# Objektorientierte Programmierung mit Python
# Kap. 10
# Michael Weigend 20.4.2006
#----------------------------------------------------
class Defaultlist(list):
    def __init__(self, s=[], default=0):
        self.default = default
        list.__init__(self, s)

    def __getitem__(self, index):
        try:
            return list.__getitem__(self, index)
        except IndexError:
            return self.default

    def __add__ (self, other):
        result = list.__add__ (self, other)
        return Defaultlist(result, self.default)


        
if __name__ == "__main__":
    # Klasse testen
    p = ["Merkur", "Venus", "Erde"]
    planeten = Defaultlist(p, "unbekannter Planet")
    print(planeten)
    print(planeten[2])
    print(planeten[3])
    
   
    
    





