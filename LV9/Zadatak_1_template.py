import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from matplotlib import pyplot as plt


# ucitaj CIFAR-10 podatkovni skup
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# prikazi 9 slika iz skupa za ucenje
plt.figure()
for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.xticks([]),plt.yticks([])
    plt.imshow(X_train[i])

plt.show()


# pripremi podatke (skaliraj ih na raspon [0,1]])
X_train_n = X_train.astype('float32')/ 255.0
X_test_n = X_test.astype('float32')/ 255.0

# 1-od-K kodiranje
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

## CNN mreza
#model = keras.Sequential()
#model.add(layers.Input(shape=(32,32,3)))
#model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'))
#model.add(layers.MaxPooling2D(pool_size=(2, 2)))
#model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same'))
#model.add(layers.MaxPooling2D(pool_size=(2, 2)))
#model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same'))
#model.add(layers.MaxPooling2D(pool_size=(2, 2)))
#model.add(layers.Flatten())
#model.add(layers.Dense(500, activation='relu'))
#model.add(layers.Dense(10, activation='softmax'))
#
#model.summary()
#
## definiraj listu s funkcijama povratnog poziva
#my_callbacks = [
#    keras.callbacks.TensorBoard(log_dir = 'logs/cnn',
#                                update_freq = 100)
#]
#
#model.compile(optimizer='adam',
#                loss='categorical_crossentropy',
#                metrics=['accuracy'])
#
#model.fit(X_train_n,
#            y_train,
#            epochs = 10,
#            batch_size = 64,
#            callbacks = my_callbacks,
#            validation_split = 0.1)
#
#
#score = model.evaluate(X_test_n, y_test, verbose=0)
#print(f'Tocnost na testnom skupu podataka: {100.0*score[1]:.2f}')

# python -m tensorboard.main --logdir=logs/cnn --port=6606 -> ovo je za pokretanje tensorboarda

#zad 2
# CNN mreža sa Dropout slojevima
model = keras.Sequential()
model.add(layers.Input(shape=(32, 32, 3)))
model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Dropout(0.25))  # Dodan Dropout sloj

model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Dropout(0.25))  # Dodan Dropout sloj

model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Dropout(0.25))  # Dodan Dropout sloj

model.add(layers.Flatten())
model.add(layers.Dense(500, activation='relu'))
model.add(layers.Dropout(0.5))  # Dodan Dropout sloj nakon Dense sloja
model.add(layers.Dense(10, activation='softmax'))

model.summary()

my_callbacks = [
    keras.callbacks.TensorBoard(log_dir='logs/cnn_dropout',  # Novi direktorij za TensorBoard
                                update_freq=100),
    keras.callbacks.EarlyStopping(monitor='val_loss',  # Praćenje gubitka na validaciji
                                  patience=5,  # Broj epoha bez smanjenja gubitka
                                  verbose=1,  # Prikaz poruka kad se treniranje zaustavi
                                  restore_best_weights=True)  # Vrati najbolje težine
]


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train_n,
          y_train,
          epochs=50,
          batch_size=64,
          callbacks=my_callbacks,
          validation_split=0.1)

score = model.evaluate(X_test_n, y_test, verbose=0)
print(f'Točnost na testnom skupu podataka: {100.0 * score[1]:.2f}')


#4.zad:
#1. Veličina serije (batch_size)
#Prevelika (npr. 1024) → brža konvergencija, ali lošija generalizacija
#
#Premala (npr. 8) → bučan trening, može pomoći pri generalizaciji, ali traje dugo
#
#2. Stopa učenja (learning rate)
#Prevelika (npr. 0.1) → model ne konvergira
#
#Premala (npr. 1e-6) → učenje presporo
#
#3. Manja mreža (izbacivanje slojeva)
#Manja mreža → brže trenira, ali može imati nižu točnost jer manje reprezentativna moć
#
#4. Smanjen skup za učenje (npr. 50%)
#Manje podataka → veći rizik overfittinga, niža točnost testiranja