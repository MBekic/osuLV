import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.cluster import KMeans, AgglomerativeClustering


def generate_data(n_samples, flagc):
    # 3 grupe
    if flagc == 1:
        random_state = 365
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
    
    # 3 grupe
    elif flagc == 2:
        random_state = 148
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)

    # 4 grupe 
    elif flagc == 3:
        random_state = 148
        X, y = make_blobs(n_samples=n_samples,
                        centers = 4,
                        cluster_std=np.array([1.0, 2.5, 0.5, 3.0]),
                        random_state=random_state)
    # 2 grupe
    elif flagc == 4:
        X, y = make_circles(n_samples=n_samples, factor=.5, noise=.05)
    
    # 2 grupe  
    elif flagc == 5:
        X, y = make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

## generiranje podatkovnih primjera
#X = generate_data(500, 1)
#
## prikazi primjere u obliku dijagrama rasprsenja
#plt.figure()
#plt.scatter(X[:,0],X[:,1])
#plt.xlabel('$x_1$')
#plt.ylabel('$x_2$')
#plt.title('podatkovni primjeri')
#plt.show()

#1.zad
fig, axes = plt.subplots(1, 5, figsize=(20, 4))

for i in range(5):
    X = generate_data(500, i + 1)
    ax = axes[i]
    ax.scatter(X[:, 0], X[:, 1])
    ax.set_title(f'flagc={i + 1}')
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')

plt.tight_layout()
plt.suptitle('Primjeri generiranih podataka za različite načine (flagc)', fontsize=16, y=1.05)
plt.show()

#2 i 3. zad
fig, axes = plt.subplots(5, 4, figsize=(5, 5))

for i, flagc in enumerate(range(1, 6)):  # 1 do 5
    X = generate_data(500, flagc)

    for j, k in enumerate(range(2, 6)):  

        kmeans = KMeans(n_clusters=k, random_state=0)
        y_kmeans = kmeans.fit_predict(X)

        ax = axes[i, j]
        ax.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', s=10)
        ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
                   s=100, c='red', marker='x')
        ax.set_title(f'flagc={flagc}, K={k}', fontsize=9)
        ax.set_xticks([])
        ax.set_yticks([])

plt.tight_layout()
plt.suptitle('K-means klasteriranje za različite podatke i vrijednosti K', fontsize=18, y=1.02)
plt.show()