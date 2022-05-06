# ---------------------------------------------------
# Dateiname: geld2.py
# Klasse Geld mit Überladung der Operatoren +, <, >, == 
# Python 3
# Kap. 10
# Michael Weigend 05.05.2022
#----------------------------------------------------
class Geld(object):  
    __wechselkurs = {'USD':0.84998,
                     'GBP':1.39480,
                     'EUR':1.0,
                     'JPY':0.007168}         

    def __init__(self, währung, betrag):            
        self.währung = währung
        self.betrag = float(betrag)
    def getEuro(self):                                
        return self.betrag*self.__wechselkurs[self.währung]

    def __add__ (self, geld):                        #1
        a = self.getEuro()
        b = geld.getEuro()
        faktor = 1.0/self.__wechselkurs[self.währung]
        summe = Geld (self.währung, (a+b)*faktor )   #2
        return summe

    def __lt__(self, other):                         #3
        a = self.getEuro () 
        b = other.getEuro ()
        return a < b                                 #4

    def __le__(self, other):
        a = self.getEuro () 
        b = other.getEuro ()
        return a <= b

    def __eq__(self, other):
        a = self.getEuro () 
        b = other.getEuro ()
        return a == b

    def __str__(self):                               #5
        return self.währung + ' ' + str(round(self.betrag, 2))

if __name__ == '__main__':
    # Klasse testen

    print(Geld('USD', 100))
    hotelkosten = Geld('USD', 130)
    mietwagen = Geld('EUR',100)
    print(mietwagen + hotelkosten)
    if mietwagen > hotelkosten:
            print('Der Mietwagen ist teurer')
    else:
            print('Der Mietwagen ist nicht teurer')  
