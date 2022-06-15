#----------------------------------------------------
# Dateiname:  zeitexperiment.py
# Der Zeitbeadrf für die parallele Ausführung von
# Prozessen wird gemessen.
#
# Python 3,  mitp Verlag
# Kap. 32
# Michael Weigend 12. 06. 2019
#----------------------------------------------------
from multiprocessing import Pool
from time import time, sleep

def square(x):
    sleep(1)                                          #1       
    return x**2

if __name__ == '__main__':
    p = Pool()                                        #2
    start = time()                                    #3
    numbers = range(8)                                #4
    result = p.map(square, numbers)                   #5 
    p.close()                                         #6
    p.join()            
    print(result, "Zeit parallel: ", time() - start)  #7
    start = time()                                    #8
    result = list(map(square, numbers))               #9
    print(result, "Zeit seriell: ", time() - start)
