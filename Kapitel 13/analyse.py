#----------------------------------------------------
# Dateiname: analyse.py
# Ausgabe eines Analyseergebnisses
#
# Python 3
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------
# analyse.py
from time import *
class Analyse:
    def __init__(self, titel, anionen, kationen):
        self.__titel = titel
        self.__an = anionen
        self.__kat = kationen

    def __str__(self):
        text= self.__titel.center(40)+'\n'              #1
        text += ('Datum: '+asctime()).center(40)+'\n\n' #2
        text+='Kationen (mg/l)'.ljust(20)               #3
        text+='Anionen (mg/l)'.ljust(20)+'\n'          
        text+=40*'-'+'\n'                               #4
        i=0
        while i<max(len(self.__an), len(self.__kat)):   #5
            if i<len(self.__kat):                      
               text += "{k[0]} ({k[1]})".format(k=self.__kat[i]).ljust(20)
            else: text+=20*' '
            if i<len(self.__an):
               text += "{a[0]} ({a[1]})\n".format(a=self.__an[i])
            else: text+=20*' '+'\n'
            i+=1
        return text

sprudel=Analyse('Analyse von Sprudelwasser',
                [('Chlorid',40), ('Sulfat',38),
                 ('Hydrogencarbonat', 1816)],
                [('Natrium', 118), ('Kalium', 11),
                 ('Magnesium', 108), ('Calcium', 348)])

print (sprudel)


input('Beenden mit <ENTER>')
