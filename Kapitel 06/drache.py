# ---------------------------------------------------
# Dateiname: drache.py
# Rekursive Funktion mit Turtle-Grafik
# Python 3
# Kap. 6 
# Michael Weigend Januar 2013
#----------------------------------------------------
from turtle import *


def drachen(länge, stufe):
    if stufe == 0:
        fd(länge)
        back(länge)
        return
    else:
        left(45)
        drachen(länge/1.4142, stufe-1)
        right(45)
        up()
        fd(länge)
        down()
        left(135)
        drachen(länge/1.41, stufe-1)
        up()
        right(135) 
        back(länge) 
        down()
        return

speed(0)
hideturtle()
drachen(200, 12)
