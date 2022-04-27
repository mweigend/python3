#!/usr/bin/env python
#-----------------------------------------------------
# Dateiname: binaerzahlen.py
# Vierstellige Binärzahlen werden ausgegeben
#
# Python 3
# Kapitel 3
# Michael Weigend, 15.06.2019
#-----------------------------------------------------

for i3 in [0, 1]:
    for i2 in [0, 1]:
        for i1 in [0, 1]:
            for i0 in [0, 1]:
                print(i3,i2, i1, i0, end="   ")
                # ende for i0 ...
            # ende for i1 ...
        print()
        # ende for i2 ...
    # ende for i3 ...

input()


