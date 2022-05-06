# ---------------------------------------------------
# Dateiname: newint.py
# Klasse Stack, von Basisklasse list abgeleitet
# Objektorientierte Programmierung mit Python
# Kap. 10
# Michael Weigend 20.4.2006
#----------------------------------------------------
class NewInt(int):
    def __init__(self, number):
        int.__init__(self, number)

    def __in__(self, other):
        return str(self) in str(other)




