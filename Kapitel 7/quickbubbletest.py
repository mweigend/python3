# ---------------------------------------------------
# Dateiname: quickbubbletest.py
# Bubblesort und Quicksort im Vergleich
# Python 3
# Kap. 7 
# Michael Weigend 1. 10. 03
#----------------------------------------------------

def bubblesort(liste):
    s = liste[:]
    if len(s) == 1:
        return s
    for i in range(len(s)):                  
        for j in range (len(s)-1):
            if s[j]>s[j+1]:
                s[j], s[j+1]=  s[j+1], s[j] # vertauschen
    return s   

def quicksort(s):
     if len(s) <= 1: return s
     else:
        return quicksort( [ x for x in s[1:] if x < s[0]])\
        + [s[0] ]  \
        + quicksort( [ y for y in s[1:] if y >= s[0]])
    
def test(sort, s):                                        # 1
    import time
    start = time.time()                                   # 2
    print (sort, "läuft ...")
    t = eval(sort+"(s)")                                  # 3
    zeit = int((time.time()-start)*1000)                  # 4
    print ("Benötigte Zeit:", zeit, "Millisekunden")

# Hauptprogramm
import random
print ("Bubblesort und Quicksort im Vergleich")
max = int(input("Länge der zu sortiernden Liste (100-2000): ") )
s = [random.randint(0, 100000) for i in range(max)]       # 5
test ("quicksort", s)
test ("bubblesort", s)
input("Beenden mit <ENTER>")


