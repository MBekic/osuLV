import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,3,1])
y=np.array([1,2,2,1,1])
plt.plot(x,y,'r', linewidth=1, marker="*", markersize=5)
plt.axis([0,4,0,3])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Zadatak 1')
plt.show()