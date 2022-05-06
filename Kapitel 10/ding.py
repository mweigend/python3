# ---------------------------------------------------
# Dateiname: ding.py
# Modul mit Definition der Klasse Ding
#
# Python 3
# Kap. 10 Lösung 1
# Michael Weigend  20. 9. 2009
#----------------------------------------------------

class Ding(object):
    """ Modell eines Gegenstandes aus einem Metall

    Öffentliche Methoden:
    getVolumen, getMasse, __str__()
    """
    _dichte = {'Au':('Gold',19.32),
              'Fe':('Eisen',7.87),
              'Ag':('Silber',10.5)}              #1

    def __init__(self, symbol, volumen):
        self.__volumen = float(volumen)
        self._symbol = symbol

    def getMasse(self):                          #2
        return self.__volumen*self._dichte[self._symbol][1]

    def getVolumen(self):
        return self.__volumen

    def __str__(self):                           #3
        beschreibung = 'Ein Ding aus '+ \
                       self._dichte[self._symbol][0] + \
                       ' mit einer Masse von ' + \
                       format(self.getMasse(), '.2f') + ' g'
        return beschreibung


# Hauptprogramm mit Anweisungen zum Testen der Klasse Ding
if __name__=='__main__': 
    krone=Ding('Au', 200)
    print ('Masse: ', krone.getMasse())
    print ('Volumen: ', krone.getVolumen())
    print (krone)
    input('Beenden mit <ENTER>')

# Die Testanweisungen werden nur ausgeführt, wenn dieses Skript
# gestartet wird. Beim Import der Klasse werden sie nicht
# ausgeführt.

                          
