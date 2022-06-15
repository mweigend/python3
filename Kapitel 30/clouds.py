#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  clouds.py
# Bestimmung des Bewölkungsgrades durch Auswertung eines Fotos.
# Es erscheinen nacheinander zwei Fenster.
# Damit das zweite Fenster erscheint, muss das erste
# geschlossen werden. Wenn auch das zweite Fenster geschlossen
# worden ist, sieht man in der Standardausgabe
# den Wolkenanteil als Zahl.
#
# Python 3,  mitp Verlag
# Kap. 30
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

import PIL 
import numpy as np
import matplotlib.pyplot as plt

img = np.array(PIL.Image.open("Wolken.png"))
#print(img)
img_blue = img[:, :, 2] / np.mean(img, axis=2)
plt.imshow(img_blue, cmap=plt.cm.gray)
plt.colorbar()
plt.show()

img_bw = img_blue > 1.3
plt.imshow(img_bw, cmap=plt.cm.gray)
plt.colorbar()
plt.show()
print(1 - np.mean(img_bw))










































