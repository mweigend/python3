# ---------------------------------------------------
# Dateiname: geld1.py
# Klasse Geld mit privaten Attributen
# Python 3
# Kap. 10
# Michael Weigend 05.05.2022
#----------------------------------------------------
class Geld:
    __wechselkurs={'USD':0.84998,
                   'GBP':1.39480,
                   'EUR':1.0,
                   'JPY':0.007168} 
    def __init__(self, währung, betrag):
        self.__währung = währung
        self.__betrag = float(betrag)

    def getBetrag(self):
        return self.__betrag

    def getWährung(self):
        return self.__währung

    def getEuro(self):                                 
        return self.__betrag *   \
              self.__wechselkurs[self.__währung]
    
    def setBetrag(self, neuerBetrag):
        self.__betrag = float (neuerBetrag)

    def setWährung(self, neueWährung):
        if neueWährung in self.__wechselkurs.keys():
            alt = self.__wechselkurs[self.__währung]
            neu = self.__wechselkurs[neueWährung]
            self.__betrag = alt/neu * self.__betrag
            self.__währung = neueWährung
      
    def add (self, geld):                              
        summe_in_Euro = self.getEuro()+geld.getEuro()
        summe = Geld1(self.__währung,
             summe_in_Euro/self.__wechselkurs[self.__währung])
        return summe

# Ende der Klassendefinition
    

preis = Geld('USD', 1000)
preis.setWährung('EUR')
print(preis.getBetrag(), preis.getWährung())
