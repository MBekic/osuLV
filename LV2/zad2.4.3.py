import numpy as np
import matplotlib.pyplot as plt

#a
img=plt.imread("road.jpg")
plt.imshow(img, cmap="gray", alpha=0.5)
plt.show()

#b
quarter_img = img[106:212,:640]
plt.imshow(quarter_img, cmap="gray")
plt.show()

#c
rotated = np.rot90(img)
plt.imshow(rotated, cmap="gray")
plt.show()

#d
mirrored = np.flip(img)
plt.imshow(mirrored, cmap="gray")
plt.show()