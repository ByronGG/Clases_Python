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

# ===================
# 6) Predicciones visuales
#   Mostramos algunas imágenes del test con su predicción
# ===================

def show_predictions_grid(model, ds, class_names, max_show=12):
    plt.figure(figsize=(10, 7))
    shown = 0

    for images, labels in ds.take(3):
        preds = model.predict(images, verbose = 0)
        pred_labes = np.argmax(preds, axis=1)
        probs = np.max(preds, axis=1)

        for i in range(images.shape[0]):
            ax = plt.subplot(3, 4, shown + 1)
            plt.imshow(images[i].numpy().astype("uint8"))

            true_name = class_names[int(labels[i])]
            pred_name = class_names[int(pred_labes[i])]
            plt.title(f"T:{true_name}\nP:{pred_name}({probs[i]:.2f})")

            shown +=1
            if shown >= max_show:
                plt.suptitle("Predicciones (Test)")
                plt.tight_layout()
                plt.show()
                return

show_predictions_grid(model, test_ds, class_names, max_show=12)

# ===================
# 7) Visualizar Filtros (Kernel) De la primera Conv2D
#    Esto muestra "que tipo de detector" aprendio la red (bordes, diagonales...)
# ===================

def plot_first_conv_kernels(model, max_kernels=16):
    # Busca la primera capa Conv2D
    conv_layer = None
    for layer in model.layers:
        if isinstance(layer, tf.keras.layers.Conv2D):
            conv_layer = layer
            break
    if conv_layer is None:
        raise ValueError("No se encontró ninguna capa Conv2D.")

    # Pesos: (kh, kw, in_channels, out_channels)
    W, b = conv_layer.get_weights()
    out_channels = W.shape[-1]
    n = min(max_kernels, out_channels)

    # Para visualizar: promediamos canales RGB => kernel 2D
    kernels_2d = W[:, :, :, :n].mean(axis=2)  # (kh, kw, n)

    # Normalizamos cada kernel a 0..1
    kernels_norm = []
    for i in range(n):
        k = kernels_2d[:, :, i]
        k = (k - k.min()) / (k.max() - k.min() + 1e-8)
        kernels_norm.append(k)
    kernels_norm = np.stack(kernels_norm, axis=0)  # (n, kh, kw)

    cols = int(np.ceil(np.sqrt(n)))
    rows = int(np.ceil(n / cols))

    plt.figure(figsize=(cols * 2.2, rows * 2.2))
    for i in range(n):
        ax = plt.subplot(rows, cols, i + 1)
        plt.imshow(kernels_norm[i], cmap="gray")
        plt.title(f"Kernel {i}")
        plt.axis("off")

    plt.suptitle("Filtros aprendidos (1ª Conv2D) — detectores básicos", y=1.02)
    plt.tight_layout()
    plt.show()

plot_first_conv_kernels(model, max_kernels=16)

# ============================================================
# 8) VISUALIZAR FEATURE MAPS (ACTIVACIONES)
#    Aquí ves “qué partes de la imagen activan” cada filtro.
#    - Capa 1: bordes/contornos
#    - Capa 2+: patrones más complejos
# ============================================================
def get_one_batch(ds):
    for images, labels in ds.take(1):
        return images, labels

def plot_feature_maps(model, image_batch, conv_layer_index=0, max_maps=16):
    """
    conv_layer_index:
      0 = primera Conv2D
      1 = segunda Conv2D
      2 = tercera Conv2D
    """
    conv_layers = [l for l in model.layers if isinstance(l, tf.keras.layers.Conv2D)]
    if not conv_layers:
        raise ValueError("No hay capas Conv2D.")

    if conv_layer_index < 0 or conv_layer_index >= len(conv_layers):
        raise ValueError(f"conv_layer_index inválido. Hay {len(conv_layers)} capas Conv2D.")

    target_layer = conv_layers[conv_layer_index]

    # Modelo que devuelve la salida (activaciones) de esa capa
    activation_model = tf.keras.Model(inputs=model.inputs, outputs=target_layer.output)

    activations = activation_model.predict(image_batch, verbose=0)  # (batch, h, w, ch)
    act = activations[0]  # tomamos la primera imagen del batch
    n_maps = min(max_maps, act.shape[-1])

    cols = int(np.ceil(np.sqrt(n_maps)))
    rows = int(np.ceil(n_maps / cols))

    plt.figure(figsize=(cols * 2.2, rows * 2.2))
    for i in range(n_maps):
        fmap = act[:, :, i]
        fmap = (fmap - fmap.min()) / (fmap.max() - fmap.min() + 1e-8)

        ax = plt.subplot(rows, cols, i + 1)
        plt.imshow(fmap, cmap="gray")
        plt.title(f"Map {i}")
        plt.axis("off")

    plt.suptitle(f"Feature maps — {target_layer.name} (qué 've' la CNN)", y=1.02)
    plt.tight_layout()
    plt.show()

# Tomamos un batch del test para visualizar activaciones
img_batch, lab_batch = get_one_batch(test_ds)

# Muestra la imagen original (la primera del batch)
plt.figure()
plt.imshow(img_batch[0].numpy().astype("uint8"))
plt.title(f"Imagen de ejemplo (label real): {class_names[int(lab_batch[0])]}")
plt.axis("off")
plt.show()

# Feature maps de la 1ª Conv2D (bordes/contornos)
plot_feature_maps(model, img_batch, conv_layer_index=0, max_maps=16)

# Feature maps de una capa más profunda (patrones más complejos)
plot_feature_maps(model, img_batch, conv_layer_index=1, max_maps=16)

print("\n[OK] Demo terminada: dataset, entrenamiento, predicciones, kernels y feature maps.")