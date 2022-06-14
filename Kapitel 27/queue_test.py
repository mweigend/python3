#----------------------------------------------------
# Dateiname:  queue_test.py
# Simulation eines Producer-Consumer-Systems
# 
# Python 3,  mitp Verlag
# Kap. 27
# Michael Weigend 08. 06. 2019
#----------------------------------------------------
#queue_test.py
from queue_ import Queue

q = Queue()

for i in range(5):
    q.enqueue(i)

while not q.empty():
    item = q.dequeue()
    print (item, end=" ")

    


