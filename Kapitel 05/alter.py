#!/usr/bin/env python3
# ---------------------------------------------------
# Dateiname: alter.py
# 
# Python 3
# Kap. 5 Lösung 2
# Michael Weigend 1. 10. 09
#----------------------------------------------------
#alter.py
print("Bitte geben Sie Ihr Alter an.")
alter = input("Alter: ")
if 14 <= int(alter) < 18:
    print("Sie sind nach deutschem Recht ein Jugendlicher.")
else:
    print("Sie sind nach deutschem Recht kein Jugendlicher.")

input()
