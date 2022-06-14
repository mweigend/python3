#----------------------------------------------------
# Dateiname:  warteschlange.py
# Implementierung einer Warteschlange beim TÜV
# 
# Python 3,  mitp Verlag
# Kap. 27
# Michael Weigend 08. 06. 2019
#----------------------------------------------------

from queue_ import Queue                  # selbst gemachte Queue
menuetext = """(N)euerKunde
(A)bfertigen des nächsten Kunden
(E)nde
"""
print("Warten beim TÜV")                      
print()
warteschlange = Queue()                                        #1
wahl = "x"
while not ((wahl in "eE") and    warteschlange.empty()):
    print(menuetext)
    wahl = input('Auswahl: ')
    if wahl in "nN":
        kennzeichen = input("Kennzeichen: ")
        warteschlange.enqueue(kennzeichen)                     #2 
    elif wahl in "aA":
        if not warteschlange.empty():
            print("Der nächste ist: ",
                 warteschlange.dequeue())                      #3
        else:
            print("Warteschlange ist leer")  
    elif (wahl in "eE") and not warteschlange.empty():
        print ("Es warten noch Kunden!")                       #4
print("Ich wünsche einen schönen Feierabend! ")
