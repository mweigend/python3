#----------------------------------------------------
# Dateiname:  queue_.py
# Implementierung das Abstrakten Datentyps Schlange (Queue)
# 
# Python 3,  mitp Verlag
# Kap. 27
# Michael Weigend 08. 06. 2019
#----------------------------------------------------

class Queue:
    def __init__(self):
        self.__content=[]

    def empty(self):
        return self.__content ==[]

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


