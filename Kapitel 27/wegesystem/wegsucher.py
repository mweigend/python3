#----------------------------------------------------
# Dateiname:  wegsucher.py
# Implermentierung eines elektronischen Wegweisers.
# Das Wegesystem wird durch einen Graphen repräsentiert.
# Der wiederum wird durch ein Dictionary dargestellt, in dem
# jedem Knotennamen (Schlüssel) die Adjazenzliste (Wert)
# zugeordnet wird.
# 
# Python 3,  mitp Verlag
# Kap. 27
# Michael Weigend 08. 06. 2019
#----------------------------------------------------

# Klassendefinitionen

class Queue:
    def __init__(self):
        self.__liste=[]

    def empty(self):
        return self.__liste ==[]

    def enqueue(self, objekt):
        self.__liste+=[objekt]

    def dequeue(self):
        if not self.empty():
            objekt=self.__liste[0]
            del self.__liste[0]
            return objekt
    def front (self):
        if not self.empty():
            return self.__liste[0]

class Stack:
    def __init__(self):
        self.__liste=[]

    def push(self, objekt):
        self.__liste=[objekt]+self.__liste

    def top(self):
        if not self.empty():
            return self.__liste[0]

    def pop(self):
        if not self.empty():
            element=self.__liste[0]
            del self.__liste[0]
            return element
        
    def empty(self):
        return self.__liste==[]

class Knoten:
    def __init__(self,name,inhalt, next_):
        self.name = name
        self.inhalt = inhalt
        self.next = next_

    def __str__(self):
        return "{}: {} {}". format(self.name, self.inhalt,
                                   str(self.next))  

class Graph:
    def __init__(self, datei):
        self.__knoten = {}
        self.lade(datei)

    def lade (self, datei):
        f = open(datei, "r", encoding="utf-8")
        zeilenliste = f.readlines()                  #1
        f.close()        
        for zeile in zeilenliste:
            name, inhalt, next_ = zeile.split("$")    #2
            self.__knoten[name] = Knoten(name, inhalt,
                                       next_.split()) #3

    def __contains__(self, name):
        return name in self.__knoten.keys()          #4
   
    def getAlleKnoten(self):                         #5
        return self.__knoten.values()

    def getKnoten(self, name):                       #6
        if name in self:
            return self.__knoten[name]

    def __str__(self):                               #7
        beschreibung = ""
        for k in self.__knoten.values():
            beschreibung += str(k)+ "\n"
        return beschreibung
 

    def getWeg(self, start, ziel):
        """ liefert Weg von Knoten start zu Knoten ziel als Stack"""
        s = Queue()                                              #1
        besucht = [start]                                        #2
        aktuell = start
        s.enqueue(start)                           
        while aktuell != ziel and not s.empty():                 #3   
            aktuell=s.dequeue()
            for name in aktuell.next:                            #4
                k = self.getKnoten(name)
                if k not in besucht:
                    k.previous = aktuell                         #5
                    s.enqueue(k)
                    besucht.append(k)                            #6
        if aktuell == ziel:     # Weg gefunden
            weg = Stack()                                        #7 
            weg.push(ziel)
            k = ziel
            while k != start:
                weg.push(k.previous)
                k = k.previous
            return weg                            

    def sucheKnoten(self, wort):
        """ liefert Knoten, in dessen Inhalt wort vorkommt"""
        
        for k in self.getAlleKnoten():
            if k.inhalt.count(wort) > 0:                     #8
                return k 

# Hauptprogramm

g = Graph("institut.txt")
print(g)
print ("Hallo, ich bin der digitale Wegweiser des Instituts.")
print ("Wohin wollen Sie? ")
wort = input("Ziel: ")
while wort:
    ziel = g.sucheKnoten(wort)
    if ziel:
        weg = g.getWeg(g.getKnoten("F21"), ziel)             #9
        print("Wegbeschreibung: ")
        while not weg.empty():
            print(weg.pop().inhalt)                          #10
    else:
        print("Ziel ist nicht erreichbar.")
    wort = input("Ziel: ")
print("Auf Wiedersehen! ")


input('Beenden mit <ENTER>')



