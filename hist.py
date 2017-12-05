import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('rede_hidro.png')

hist = {x: 0 for x in range(256)}

for cell in img.flatten():
	hist[cell] = hist[cell] + 1

# print hist

plt.bar(hist.keys(), hist.values(), color='black')
plt.show()
