#----------------------------------------------------
# Dateiname:  wegesystem.py
# Repraesentation eines Wegesystems durch einen Graph
# 
# Python 3,  mitp Verlag
# Kap. 27
# Michael Weigend 08. 06. 2019
#----------------------------------------------------

# wegesystem.py
# Repräsentation eines Wegesystems durch einen Graph
class Knoten:
    def __init__(self,name,inhalt, next):
        self.name = name
        self.inhalt = inhalt
        self.next = next

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
            name, inhalt, next = zeile.split("$")    #2
            self.__knoten[name] = Knoten(name, inhalt,
                                       next.split()) #3

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

# Hauptprogramm
g = Graph("institut.txt")                            #8
print(g)


input('Beenden mit <ENTER>')



