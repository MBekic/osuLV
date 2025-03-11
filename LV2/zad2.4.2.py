import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter=",", skiprows=1)

#a
num_people = data.shape[0]
print(f"Ukupno mjerenih osoba: {num_people}")

#b
plt.scatter(data[:, 1], data[:, 2], alpha=0.1)
plt.xlabel("Visina (cm)")
plt.ylabel("Masa (kg)")
plt.title("Odnos visine i mase")
plt.show()

#c
plt.scatter(data[::50, 1], data[::50, 2], alpha=0.1)
plt.xlabel("Visina (cm)")
plt.ylabel("Masa (kg)")
plt.title("Odnos visine i mase (svaka 50.osoba)")
plt.show()

#d
min_height = np.min(data[:,1])
max_height = np.max(data[:,1])
avg_height = np.mean(data[:,1])

print(f"Minimalna visina: {min_height:.2f} cm")
print(f"Maksimalna visina: {max_height:.2f} cm")
print(f"Srednja visina: {avg_height:.2f} cm")

#e
m = (data[:,0]==1)
f = (data[:,0]==0)

men_heights = data[m, 1]
women_heights = data[f, 1]
print(f"Muskarci - Min: {np.min(men_heights):.2f} cm, Max: {np.max(men_heights):.2f} cm, Prosjek: {np.mean(men_heights):.2f} cm")
print(f"Zene - Min: {np.min(women_heights):.2f} cm, Max: {np.max(women_heights):.2f} cm, Prosjek: {np.mean(women_heights):.2f} cm")