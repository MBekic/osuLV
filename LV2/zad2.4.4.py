import numpy as np
import matplotlib.pyplot as plt

black = np.zeros((50, 50))  
white = np.ones((50, 50))   

top_row = np.hstack((black, white)) 
bottom_row = np.hstack((white, black)) 

checkerboard = np.vstack((top_row, bottom_row)) 

plt.imshow(checkerboard, cmap="gray", interpolation="nearest")
plt.axis([0,100,100,0])
plt.title("Zadatak 2.4.4.")
plt.show()
