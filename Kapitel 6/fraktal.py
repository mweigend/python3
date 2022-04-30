# ---------------------------------------------------
# Dateiname: baum_2.py
# Rekursives Zeichnen eines Baums mit Turtle-Grafik
# Variante mit rechten Winkeln
# Python 3
# Kap. 6 Lösung 5b
# Michael Weigend Januar 2013
#----------------------------------------------------

from turtle import *

def fraktal(x):
    if x < 5: return      
    else:
         forward(x)
         left(90)
         fraktal(x*0.5)      
         right(180)
         fraktal(x*0.5)      
         left(90)
         back(x)      
    return

left(90)                  
speed(0)
fraktal(100)
hideturtle()
        
