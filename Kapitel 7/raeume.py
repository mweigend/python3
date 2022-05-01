#----------------------------------------------------
# Dateiname:  raeume.py
# Eine Raumplan mit Mengen modellieren
# 
# Python 3
# Kap. 7.5.2 
# Michael Weigend 15. 2. 2005
#----------------------------------------------------

def findeNachbarraeume(plan, raum):
    """ Menge aller Nachbarräume"""
    raeume, tueren = plan
    t_raum = set(t for t in tueren if raum in t)      #1
    nachbarraeume = set()                             #2
    for t in t_raum:
        nachbarraeume = nachbarraeume | t             #3
    return nachbarraeume - set([raum])                #4

def vereinige (plan1, plan2):
    """ füge zwei Pläne zusammen """
    return (plan1[0] | plan2[0], plan1[1] | plan2[1]) #5

V1 = {1, 2, 3, 4, 5}
E1 = set(frozenset(t)                                 #6
         for t in [(1, 2),(2, 3), (2, 4),(3, 4),(4, 5)])
raumplan1 = (V1, E1)                                  #7

V2 = {4, 5, 6, 7}
E2 = set(frozenset(t)
         for t in [(5, 4), (5, 6),(5 ,7), (6, 7)])
raumplan2 = (V2, E2)

gesamtplan = vereinige(raumplan1, raumplan2)
nachbarraeume = findeNachbarraeume(gesamtplan, 2)
print ("Räume des Gesamtplans:")
for r in gesamtplan[0]: print (r, end=" ")
print()
print ("Türen des Gesamtplans:")
for t in gesamtplan[1]: print(tuple(t), end=" ")
print()
print("Nachbarräume von Raum 2:")
for r in nachbarraeume: print (r, end=" ")


