#----------------------------------------------------
# Dateiname: laenge.py
# Modul mit Definition der Klasse Laenge
#
# Objektorientierte Programmierung mit Python
# Kap. 10 Lösung 3
# Michael Weigend 20.9.2009
#----------------------------------------------------

class Länge:
    """ Modell einer Strecke """
    __meter = {'mm': 0.001, 'cm':0.01, 'm':1, 'km':1000,
               'in':0.0254, 'ft':0.3048, 
               'yd':0.9143, 'mil':1609}               #1

    def __init__(self, betrag, einheit):
        self.__betrag = float(betrag)                 #2
        self.__einheit=einheit

    def getMeter(self):
        return self.__betrag*self.__meter[self.__einheit]

    def __add__(self, other):                         #3
        s = self.getMeter() + other.getMeter()
        return Länge(s/self.__meter[self.__einheit],
                     self.__einheit)
    def __gt__(self, other):                          #4
        return self.getMeter() > other.getMeter()
    
    def __ge__(self, other):                          #5
        return self.getMeter() >= other.getMeter()
    
    def __eq__(self, other):                          #6
        return self.getMeter() == other.getMeter()

    def __str__(self):
        return str(self.__betrag)+' ' + self.__einheit

# Hauptprogramm zum Testen 
print(Länge(12, 'cm') + Länge (2, 'in'))
erddurchmesser = Länge (12713.507, 'km')
print(erddurchmesser) 
print(Länge(0, 'mil') + erddurchmesser)
print(Länge(12, 'cm') > Länge (2, 'in'))
print(Länge(12, 'cm') >= Länge (2, 'in'))
print(Länge(12, 'cm') == Länge (2, 'in'))
print(Länge(12, 'cm') < Länge (2, 'in'))
print(Länge(12, 'cm') <= Länge (2, 'in'))

input('Beenden mit <ENTER>')

