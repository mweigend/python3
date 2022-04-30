# spirale_0.py
from turtle import *

def spirale(x):
    forward(x)
    right(90)
    spirale(0.9*x) # rekursiver Aufruf
    return


spirale(200)
