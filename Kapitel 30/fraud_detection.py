#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  fraud_detection.py
# Die Daten in der Datei groesse.dat(Größenangaben)
# werden mit einer Normalverteilung verglichen.
#
# Python 3,  mitp Verlag
# Kap. 30
# Michael Weigend 11. 06. 2019
#----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

mean = 165.4
sd = 4.5
bins=np.arange(140, 200, 2)

data = np.loadtxt("groesse.dat").ravel()
normal = mean + sd * np.random.randn(1000000)

plt.figure(1)
plt.subplot(2,1,1)
plt.hist(normal, bins, density=1, facecolor="b", alpha=0.75)               
plt.title("Körpergröße - Normalverteilung")
plt.grid(True)

plt.subplot(2,1,2)
plt.hist(data, bins, density=1, facecolor="r", alpha=0.50)               
plt.title("Körpergröße - Stichprobe")
plt.grid(True)
plt.show()

