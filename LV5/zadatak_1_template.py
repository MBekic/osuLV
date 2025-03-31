import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Generiranje umjetnog binarnog klasifikacijskog problema
X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# Podjela na skup za učenje i testiranje
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# a) Prikaz podataka
plt.figure(figsize=(8, 6))
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', edgecolors='k', label='Trening')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='coolwarm', marker='x', label='Test')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Podaci za učenje i testiranje")
plt.legend()
plt.show()
#boje - y_train i y_test razlicite klase 
    #određuje kojoj klasi pripada podatak(0 ili 1)

# b) Izgradnja modela logističke regresije
model = LogisticRegression() #pravocrtna granica odluke - razdvajanje klase (0 i 1) pomocu vjv
model.fit(X_train, y_train) #trening podataka -> model uči parametre (00, 01, 02 -> granice odluke) zbog razdvjanaja klasa

# c) Prikaz granice odluke
coef = model.coef_[0]
intercept = model.intercept_[0]
#coef_[0] → Lista s dvije vrijednosti [θ1, θ2]
#intercept_ → Skalarnu vrijednost θ0

x_vals = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
y_vals = -(coef[0] * x_vals + intercept) / coef[1]

plt.figure(figsize=(8, 6))
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', edgecolors='k', label='Trening')
plt.plot(x_vals, y_vals, 'k--', label='Granica odluke')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Granica odluke modela")
plt.legend()
plt.show()

# d) Klasifikacija testnog skupa
y_pred = model.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Matrica zabune:\n{conf_matrix}")
print(f"Tocnost: {accuracy:.2f}".encode('utf-8', errors='ignore').decode('utf-8'))
print(f"Preciznost: {precision:.2f}".encode('utf-8', errors='ignore').decode('utf-8')) #21/(21+2)
print(f"Odziv: {recall:.2f}".encode('utf-8', errors='ignore').decode('utf-8')) #21/(21+1)

# e) Prikaz dobro i pogrešno klasificiranih primjera
plt.figure(figsize=(8, 6))
for i in range(len(X_test)):
    color = 'green' if y_test[i] == y_pred[i] else 'black'
    plt.scatter(X_test[i, 0], X_test[i, 1], color=color, edgecolors='k')

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Testni podaci - zeleno: točno, crno: pogrešno klasificirani")
plt.show()
