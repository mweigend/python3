from turtle import *


def spirale(x):
    if x < 5:
        return
    else:
        circle(x)
        right(10)
        spirale(x-10)

spirale(100)
