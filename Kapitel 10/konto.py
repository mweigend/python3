# ---------------------------------------------------
# Dateiname: konto.py
# Modul mit Implementierung der Klasse Konto. Sie wird von
# der Klasse Geld abgeleitet und modelliert ein Bankkonto
#
# Python 3,  Kap. 10 
# Michael Weigend 20.2.2021
#----------------------------------------------------
# konto.py
import time
from geld2 import Geld                                #1
class Konto(Geld):
    """ Spezialisierung der Klasse Geld zur Verwaltung eines Kontos
        Öffentliche Attribute:
           geerbt: währung, betrag, wechselkurs

        Öffentliche Methoden und Überladungen:
           geerbt: __add__(), __lt__(),
                   __le__(), __eq__(), getEuro()
           überschrieben: __str__()
           Erweiterungen:
             einzahlen(), auszahlen(), druckeKontoauszug() 
    """
    def __init__(self, währung, inhaber):
        Geld.__init__(self,währung, 0)               #2
        self.__inhaber = inhaber                      #3
        self.__kontoauszug = [str(self)]              #4

    def einzahlen(self,währung, betrag):             #5          
        einzahlung = Geld(währung,betrag)
        self.betrag =(self+einzahlung).betrag         #6
        eintrag = time.asctime()+' ' +str(einzahlung) +\
                ' neuer Kontostand: '+ self.währung + \
        ' ' + str(round(self.betrag, 2))
        self.__kontoauszug += [eintrag]               #7

    def auszahlen(self, währung, betrag): 
        self.einzahlen(währung, -betrag)

    def druckeKontoauszug(self):                      #8
        for i in self.__kontoauszug:
            print(i)
        self.__kontoauszug = [str(self)]

    def __str__(self):                                #9
        return 'Konto von ' + self.__inhaber + \
               ':\nKontostand am ' + time.asctime() + \
               ': ' + self.währung + ' ' +\
                str(round(self.betrag, 2))
                

# Ende der Klassendefinition

if __name__ == '__main__':
    
    # Klasse testen
    konto = Konto('EUR', 'Tim Wegner')
    konto.einzahlen('EUR', 1200)
    time.sleep(2)
    konto.auszahlen('USD', 50)
    konto.einzahlen('GBP', 30.30)
    print(konto)
    konto.druckeKontoauszug()


