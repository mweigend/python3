# ---------------------------------------------------
# Dateiname: baum_1.py
# Rekursives Zeichnen eines Baums mit Turtle-Grafik
# Varinte mit unsymmetrischem Baum
# Python 3
# Kap. 6 Lösung 5a
# Michael Weigend Januar 2013
#----------------------------------------------------

from turtle import *

def baum(x):
    if x < 5: return      
    else:
         forward(x)
         left(30)        
         baum(x*0.7)     
         right(90)
         baum(x/2)       
         left(60)
         backward(x)     
    return

left(90)                 
baum(100)
hideturtle()
        
