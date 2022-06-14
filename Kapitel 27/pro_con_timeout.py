#----------------------------------------------------
# Dateiname:  pro_con_timeout.py
# Simulation eines Producer-Consumer-Systems
# 
# Python 3,  mitp Verlag
# Kap. 27
# Michael Weigend 08. 06. 2019
#----------------------------------------------------

import threading, queue, time, random
NR_CONSUMERS = 2

class Producer(threading.Thread):                      #1
    def __init__(self, queue, name):
        self.__queue = queue                           
        self.__name = name
        threading.Thread.__init__(self)              

    def run(self):
        for i in range(5):
            item = self.__name + str(i)
            time.sleep(random.randint(1, 50)/100)      #2
            self.__queue.put(item)                     
            print("Auftrag " + item)

class Consumer(threading.Thread):
    def __init__(self, queue):
        self.__queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while True:
          try:
            item = self.__queue.get(timeout=2)          #3
            time.sleep(random.randint(1, 50)/100)       #4
            print("Auftrag {} wurde beendet.".format(item))
          except:
              print("Keine weiteren Aufträge gefunden.")
              break                                     #5

queue = queue.Queue(3)                              
for i in range(NR_CONSUMERS):
    Consumer(queue).start()                             #6

Producer(queue, "A").start()                            #7
Producer(queue, "B").start()



