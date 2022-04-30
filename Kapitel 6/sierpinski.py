# ---------------------------------------------------
# Dateiname: sierpinski.py
# Farbiges Sierpinski-Dreieck mit Turtle-Grafik
# 
# Kap. 6 
# Michael Weigend Januar 2013
#----------------------------------------------------
from turtle import *
from random import randint
MAX = 400

def sierpinski(x):
    if x < 5:
        return
    fillcolor(x%255, (MAX-x)%255, x%255)
    begin_fill()
    fd(x)
    right(120)
    fd(x)
    right(120)
    fd(x)
    right(120)
    end_fill()
    sierpinski(x//2)
    fd(x//2)
    sierpinski(x//2)
    back(x//2)
    right(60)
    fd(x//2)
    left(60)
    sierpinski(x//2)
    right(60)
    back(x//2)
    left(60)

    return
    
speed(0)
colormode(255)
bgcolor(50, 0, 70)
hideturtle()
left(60)
sierpinski(MAX) 
