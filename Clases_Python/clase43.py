import os
import random
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# ===================
# 0) Configuración general
# ===================

DATASET_DIR = "shapes_dataset"
CLASSES = ["circle", "square", "triangle"]

IMG_SIZE = (128, 128)

# Cantidad de imágenes por split
N_TRAIN = 400
N_VAL = 100
N_TEST = 100

# Entranamiento
BATCH_SIZE = 32
EPOCHS = 10
SEED = 42

# Para reproducibilidad
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)


# ===================
# 1) CARGA
# ===================

train_dir = os.path.join(DATASET_DIR, "train")
val_dir = os.path.join(DATASET_DIR, "val")
test_dir = os.path.join(DATASET_DIR, "test")

train_ds = tf.keras.utils.image_dataset_from_directory(
    train_dir,
    image_size = IMG_SIZE,
    batch_size = BATCH_SIZE,
    seed = SEED
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    val_dir,
    image_size = IMG_SIZE,
    batch_size = BATCH_SIZE,
    seed = SEED,
    shuffle = False
)

test_ds = tf.keras.utils.image_dataset_from_directory(
    test_dir,
    image_size = IMG_SIZE,
    batch_size = BATCH_SIZE,
    seed = SEED,
    shuffle = False
)

class_names = train_ds.class_names
num_classes = len(class_names)
print("Classes detectadas: ", class_names)

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.shuffle(1000, seed=SEED).prefetch(AUTOTUNE)
val_ds = val_ds.prefetch(AUTOTUNE)
test_ds = test_ds.prefetch(AUTOTUNE)

# ===================
# 2) VISUALIZACION MUESTRAS DEL DATASET
# ===================

plt.figure(figsize=(7,7))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[int(labels[i])])
        plt.axis("off")
plt.suptitle("Muestras del dataset (entrada)")
plt.tight_layout()
plt.show()

# ===================
# 3) CNN
# - Conv2D (Filtros) - MaxPooling (tamaños) - Capas (patrones)
# ===================

data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.05),
    layers.RandomZoom(0.10),
], name="augmentation")

model = keras.Sequential([
    layers.Input(shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),
    data_augmentation,
    layers.Rescaling(1./255),
    layers.Conv2D(16, 3, activation="relu", padding="same"),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, activation="relu", padding="same"),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation="relu", padding="same"),
    layers.MaxPooling2D(),
    # Clasificación Final
    layers.Flatten(),
    layers.Dense(64, activation="relu"),
    layers.Dropout(0.25),
    layers.Dense(num_classes, activation="softmax")
])

model.compile(
    optimizer = keras.optimizers.Adam(learning_rate=1e-3),
    loss = "sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# ===================
# 4) ENTRENAR (aqui es donde "aprende a ver nuestro modelo")
# ===================

callbacks = [
    keras.callbacks.EarlyStopping(monitor="val_loss", patience=3, restore_best_weights=True)
]

history = model.fit(
    train_ds,
    validation_data = val_ds,
    epochs = EPOCHS,
    callbacks = callbacks
)

# ===================
# 5) Grafica curvas (accuracy/loss)
# ===================

hist = history.history

plt.figure()
plt.plot(hist["loss"], label="train_loss")
plt.plot(hist["val_loss"], label="val_loss")
plt.title("Loss por época")
plt.xlabel("Época")
plt.ylabel("Loss")
plt.legend()
plt.show()

plt.figure()
plt.plot(hist["accuracy"], label="train_acc")
plt.plot(hist["val_accuracy"], label="val_acc")
plt.title("Accuracy por época")
plt.xlabel("Época")
plt.ylabel("accuracy")
plt.legend()
plt.show()