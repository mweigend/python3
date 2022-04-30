# ---------------------------------------------------
# Dateiname: baum_2.py
# Rekursives Zeichnen eines Baums mit Turtle-Grafik
# Variante mit rechten Winkeln
# Python 3
# Kap. 6 Lösung 5b
# Michael Weigend Januar 2013
#----------------------------------------------------

from turtle import *

def baum(x):
    if x < 5: return      
    else:
         forward(x)
         left(90)
         baum(x*0.5)      
         right(180)
         baum(x*0.5)      
         left(90)
         back(x)      
    return

left(90)                  
speed(0)
baum(100)
hideturtle()
        
