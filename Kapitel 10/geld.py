# ---------------------------------------------------
# Dateiname: geld.py
# Modul mit Definition der Klasse Geld
# Python 3
# Kap. 10
# Michael Weigend 05.05.2022
#----------------------------------------------------
class Geld:                                           #1
    wechselkurs ={'USD':0.84998,
                  'GBP':1.39480,
                  'EUR':1.0,
                  'JPY':0.007168}                     #2
 

    def __init__(self, währung, betrag):              #3
        self.währung = währung
        self.betrag = float(betrag)
    def getEuro(self):                                #4
        return self.betrag*self.wechselkurs[self.währung]
      
    def add (self, geld):                             #5
        summe_in_Euro = self.getEuro()+geld.getEuro()
        summe = Geld(self.währung,
              summe_in_Euro/self.wechselkurs[self.währung]) 
        return summe                                  
