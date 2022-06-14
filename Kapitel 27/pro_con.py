#----------------------------------------------------
# Dateiname:  pro_con.py
# Simulation eines Producer-Consumer-Systems
# 
# Python 3,  mitp Verlag
# Kap. 27
# Michael Weigend 08. 06. 2019
#----------------------------------------------------

import threading, queue, time, random
NR_CONSUMERS = 2

class Consumer(threading.Thread):
    def __init__(self, queue):                  
        self.__queue = queue
        threading.Thread.__init__(self)             #1

    def run(self):
        while True:
            item = self.__queue.get()               #2
            if item is None:
                self.__queue.task_done()
                break                               #3
            else:
                time.sleep(random.randint(1, 50)/100)
                print("Auftrag {} wurde beendet.".format(item))
                self.__queue.task_done()            #4

queue = queue.Queue(3)                              #5
for i in range(NR_CONSUMERS):
    Consumer(queue).start()                         #6

for i in range(10):
    queue.put(i)                                    #7

for i in range(NR_CONSUMERS):                       #8
    queue.put(None)

queue.join()                                        #9
print ("Alle Aufträge erledigt.")


