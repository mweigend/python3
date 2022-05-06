#----------------------------------------------------
# Dateiname: quader.py
# Modul mit Definition der Klasse Quader, die von
# Ding abgeleitet wird.
#
# Python 3
# Kap. 10 Lösung 2
# Michael Weigend 05.05.2022
#----------------------------------------------------
 
from ding import Ding
class Quader(Ding):
    def __init__(self, symbol, 
                 länge, breite, höhe):              #1
        Ding.__init__(self, symbol, länge*breite*höhe)
        self.__länge=float(länge)
        self.__breite=float(breite)
        self.__höhe=float(höhe)
        
    def __gt__(self, other):                          #2
        return self.getMasse() > other.getMasse()
    
    def __ge__(self, other):                          
        return self.getMasse() >= other.getMasse()
    
    def __eq__(self, other):                          
        return self.getMasse() == other.getMasse()

    def __str__(self):
        text = 'Ein Quader aus '+ \
                self._dichte[self._symbol][0]+ ', ' + \
                str(round(self.__länge, 2)) + ' cm mal '+ \
                str(round(self.__breite, 2)) + ' cm mal '+ \
                str(round(self.__höhe , 2)) + ' cm'
        return text
    
# Hauptprogramm mit Anweisungen zum Testen der Klasse Quader
silberbarren = Quader('Ag', 2, 3, 4)
print ('Masse: ',silberbarren.getMasse())
print ('Volumen: ',silberbarren.getVolumen())
print (silberbarren)
input('Beenden mit <ENTER>')
