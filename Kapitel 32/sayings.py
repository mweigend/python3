#----------------------------------------------------
# Dateiname:  sayings.py
# In einem Producer-Consumer-System
# werden Sprüche aus zwei Teilen produziert.
#
# Python 3,  mitp Verlag
# Kap. 32
# Michael Weigend 12. 06. 2019
#----------------------------------------------------
from multiprocessing import Process, Queue
from random import choice

BEGINNINGS = ["Aller Anfang", "Morgenstund", "Der frühe Vogel"]
ENDINGS = ["ist schwer.", "hat Gold im Mund.", "fängt den Wurm."]

def produce(q, beginnings):
    for i in range(3):
        q.put(choice(beginnings))

def consume(q, endings):
    while True:
        try:
           beginning = q.get(timeout=2)
           print(beginning, choice(endings))
        except:
            break

if __name__ == "__main__":
    q = Queue(maxsize=3)
    producers = [Process(target=produce, args = (q, BEGINNINGS))
                for i in range(2)]
    consumers = [Process(target=consume, args = (q, ENDINGS))
                for i in range(2)]
    
    for p in producers + consumers: p.start()
    for p in producers + consumers: p.join()
    

    
