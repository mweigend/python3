#----------------------------------------------------
# Dateiname:  stacktest.py
# Implementierung des abstrakten Datentps Stack
# als Klasse mit kleinem Hauptprogramm zum Testen.
# Der Benutzer gibt eine Zeichenkette ein, die Buchstaben
# werden in umgekehrter Reihenfolge wieder ausgegeben.
# 
# Python 3,  mitp Verlag
# Kap. 27
# Michael Weigend 08. 06. 2019
#----------------------------------------------------

# stacktext.py
class Stack:
    def __init__(self):                               #1
        self.__content = []

    def push(self, item):                             #2
        self.__content = [item] + self.__content

    def top(self):                                    #3
        if not self.empty():
            return self.__content[0]  
            
    def pop(self):                                    #4
        if not self.empty():
            item = self.__content[0]
            del self.__content[0]
            return item

    def empty(self):
        return self.__content == []                   #5

# Hauptprogramm zum Testen des Stacks
from stack import *
wort = input("Wort: ")
stapel = Stack()
for zeichen in wort:
    stapel.push(zeichen)

while not stapel.empty():
    print(stapel.pop(), end=" ") 



