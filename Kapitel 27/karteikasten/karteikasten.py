#----------------------------------------------------
# Dateiname:  karteikasten.py
# Simulation eines Karteikastens zum Vokabellernen.
# 
# Python 3,  mitp Verlag
# Kap. 27
# Michael Weigend 08. 06. 2019
#----------------------------------------------------

# Klassendefinitionen

# karteikasten.py

class Queue:
    def __init__(self):
        self.__content = []

    def empty(self):
        return self.__content == []

    def enqueue(self, item):
        self.__content += [item]

    def dequeue(self):
        if not self.empty():
            item = self.__content[0]
            del self.__content[0]
            return item

    def front (self):
        if not self.empty():
            return self.__content[0]

class Karteikasten:
    def __init__(self, datei):
        self.__gelernt = Queue()
        self.__nichtGelernt = Queue()
        f = open(datei, 'r')
        wortschatz = f.readlines()                   #1
        for zeile in wortschatz:
            vokabel = zeile.split()                  #2
            self.__nichtGelernt.enqueue(vokabel)     #3

    def getNeueVokabel(self):
        return self.__nichtGelernt.front()

    def lerne (self):                                #4
        self.__gelernt.enqueue(self.__nichtGelernt.dequeue())

    def legeNachHinten(self):
        """ Vorderes Objekt wird nach hinten gelegt"""
        self.__nichtGelernt.enqueue(self.__nichtGelernt.dequeue())

# Hauptprogramm
print('Vokabeltrainer')
print()
k = Karteikasten('vokabeln.txt')
vokabel = k.getNeueVokabel()
while vokabel:
    print ('Englisch: ', vokabel[0])
    uebersetzung = input('Deutsch: ')
    if uebersetzung in vokabel[1:]:                  #5
        print('Richtig!')
        k.lerne()
    else:
        print('Falsch! Richtige Übersetzungen sind:')
        print(vokabel[1:])
        k.legeNachHinten()
    vokabel = k.getNeueVokabel()
print('Alles gelernt!')

input("Beenden mit <ENTER>")



