#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  median_filter.py
# Medianfilter zur Aufbereitung eines Bildes mit
# vielen Pixelfehlern.
#
# Python 3,  mitp Verlag
# Kap. 30
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

import PIL 
import numpy as np
import matplotlib.pyplot as plt

FNAME = "elephant_damaged.png"

def medianfilter(a):
    h, w = a.shape
    b = np.zeros((h-2, w-2, 9))
    b[:, :, 0] = a[:-2, :-2]
    b[:, :, 1] = a[:-2,1:-1]
    b[:, :, 2] = a[:-2, 2:]
    b[:, :, 3] = a[1:-1, :-2]
    b[:, :, 4] = a[1:-1,1:-1]
    b[:, :, 5] = a[1:-1, 2:]
    b[:, :, 6] = a[2:, :-2]
    b[:, :, 7] = a[2:,1:-1]
    b[:, :, 8] = a[2:, 2:]
    return np.median(b, axis=2)

img = np.array(PIL.Image.open(FNAME))
plt.subplot(1, 2, 1)
plt.imshow(img,cmap=plt.cm.gray )
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(medianfilter(img), cmap=plt.cm.gray )
plt.axis("off")
plt.show()


