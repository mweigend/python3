#!/usr/bin/env python3
# Belegungen einer aussagenlogischen Formel

print("a b c  (a or b) and c")    # Überschrift
print("---------------------")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            x = (a or b) and c
            print(a, b, c, "   ", int(x))
input()
