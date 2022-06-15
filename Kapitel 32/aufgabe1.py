#!/usr/bin/env python3
#----------------------------------------------------
# Dateiname:  kap32_aufgabe1.py
# In einem langen Text werden parallel von mehreren
# Prozessen die Vorkommen eines Suchbegriffs gezählt.
#
# Python 3,  mitp Verlag
# Kap. 32
# Michael Weigend 11. 06. 2019
#----------------------------------------------------
from multiprocessing import Process, Queue

def search(q, text, word):
    n = text.lower().count(word.lower()) 
    q.put(n)
            
if __name__ == '__main__':
    word = input("Suchbegriff: ")  
    f = open("marktwain.txt")
    text = f.read()
    f.close()
    q = Queue()
    n = len(text)
    chunks = [text[:n//4], text[n//4:n//2],
              text[n//2:3*n//4], text[3*n//4:]]

    processes = [Process(target=search, args=(q, chunk, word))
                 for chunk in chunks]
    for p in processes: p.start()
    n = 0
    for i in range(4):
        n += q.get()
    for p in processes:
        p.join()
    text = "Das Wort '{}' kommt {} Mal in Mark Twains Werk vor."
    print(text.format(word, n))                       #8 

