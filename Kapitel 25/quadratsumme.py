#----------------------------------------------------
# Dateiname: quadratsumme.py
# Test einer Funktion mit Hilfe des Docstrings
# und der Funktion doctest.testmod()
#
# Python 3,  mitp Verlag
# Kap. 25
# Michael Weigend 08. 06. 2019
#----------------------------------------------------

def quadratsumme (s):
     """ Summe der Quadrate der Elemente einer Zahlenliste

     >>> quadratsumme([1, 2, 3])      # 1 + 4 + 9
     14
     >>> quadratsumme([10, 10, 10])   # 100 + 100 + 100
     300
     >>> quadratsumme([])
     0
     >>> quadratsumme()
     0
     """
     summe = 0
     for n in s:
        summe = summe + n**2
     return summe

if __name__ == "__main__":                     #1
    import doctest
    doctest.testmod(verbose=True)


