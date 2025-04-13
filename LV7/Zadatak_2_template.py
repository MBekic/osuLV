import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

# 1. Broj različitih boja 
n_unique_colors = len(np.unique(img_array, axis=0))
print(f"Broj različitih boja u slici: {n_unique_colors}")

# 2. Kvantizacija slike
K_list = [2, 5, 10, 20]
fig, axes = plt.subplots(2, 2, figsize=(5, 5))  # 2x2 subplot mreža

for idx, K in enumerate(K_list):
    kmeans = KMeans(n_clusters=K, random_state=0)
    kmeans.fit(img_array)
    labels = kmeans.predict(img_array)
    centers = kmeans.cluster_centers_

    # 3. Zamjena piksela pripadajućim centroidom
    img_array_aprox = centers[labels]
    img_kmeans = np.reshape(img_array_aprox, (w, h, d))

    # 4. vizualizacija
    ax = axes[idx // 2, idx % 2]  # pristup subplotu po indeksu
    ax.imshow(img_kmeans)
    ax.set_title(f"K = {K}")
    ax.axis('off')

plt.suptitle("Kvantizirane slike za različite K", fontsize=16)
plt.subplots_adjust(top=0.90)
plt.show()

# 5. 
import os
for image_name in ["test_2.jpg", "test_3.jpg", "test_4.jpg", "test_5.jpg", "test_6.jpg"]:
    image_path = f"imgs\\{image_name}"
    if os.path.exists(image_path):
        img = Image.imread(image_path)
        img = img.astype(np.float64) / 255
        w, h, d = img.shape
        img_array = np.reshape(img, (w * h, d))

        K = 5
        kmeans = KMeans(n_clusters=K, random_state=0)
        labels = kmeans.fit_predict(img_array)
        centers = kmeans.cluster_centers_
        img_quantized = centers[labels].reshape((w, h, d))

        plt.figure()
        plt.title(f"{image_name} kvantizacija (K = {K})")
        plt.imshow(img_quantized)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    else:
        print(f"Slika {image_name} nije pronađena.")

# 6. Lakat metoda: ovisnost J (inertia) o K 
inertias = []
K_values = range(1, 21)

for K in K_values:
    kmeans = KMeans(n_clusters=K, random_state=0)
    kmeans.fit(img_array)
    inertias.append(kmeans.inertia_)

plt.figure()
plt.plot(K_values, inertias, 'bo-')
plt.xlabel("Broj grupa K")
plt.ylabel("Inertia (J)")
plt.title("Lakat metoda – ovisnost J o K")
plt.grid(True)
plt.tight_layout()
plt.show()

# 7. Binarna slika za svaku grupu
K = 5
kmeans = KMeans(n_clusters=K, random_state=0)
labels = kmeans.fit_predict(img_array)

for grupa in range(K):
    mask = (labels == grupa).astype(np.uint8)
    binarna_slika = np.reshape(mask, (w, h))

    plt.figure()
    plt.title(f"Binarna slika – Grupa {grupa}")
    plt.imshow(binarna_slika, cmap='gray')
    plt.axis('off')
    plt.tight_layout()
    plt.show()