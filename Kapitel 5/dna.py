#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: dna.py
# Drucke alle DNA-Sequenzen mit vier Basenpaaren
# Python 3
# Kap. 5 Loesung 10
# Michael Weigend 1. 10. 09
#----------------------------------------------------

basen = ["AT", "TA", "GC", "CG"]
for a in basen:
    for b in basen:
        for c in basen:
            for d in basen:
                print(a, b, c, d)


input("Beenden mit <ENTER>")
                    
       
                
