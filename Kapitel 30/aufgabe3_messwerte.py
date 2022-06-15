#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  aufgabe3_messwerte.py
# Darstellung von Messwerten aus einer csv-Datei.
#
# Python 3,  mitp Verlag
# Kap. 30, Aufgabe 3
# Michael Weigend 11. 06. 2019
#----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

hours = np.arange(1, 25)
data = np.loadtxt("dmd2_17_07_2016.csv" , delimiter=";")
no, no2, o3, fs, wg, wr = data.T

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(hours, no + no2)
plt.title ("Stickstoffoxide (µg/m³)")
plt.xlabel("Uhrzeit")
plt.axis([1, 24, 0, 100]) 

plt.subplot(1, 2, 2)
plt.plot(hours, o3)
plt.title ("Ozon (µg/m³)")
plt.xlabel("Uhrzeit")
plt.axis([1, 24, 0, 100]) 
plt.show()
