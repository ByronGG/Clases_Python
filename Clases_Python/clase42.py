#CNN
"""
    Las CNN (Convolutional Neural Networks) son un tipo de red neuronal profunda especialmente diseñada para procesar datos con estructura de datos con estructura de cuadrícula, como imágenes.

    Componentes.
        - Capa convolucional (Conv Layer)
        Es el núcleo del CNN. Aplica filtro (o Kernel) - una pequeña matriz - que se desliza sobre la imagen muiltiplicando y suma valores.

        - Función de activaaciín (ReLU)
        Despues de cada convolucióin se aplica ReLU: convierte valores negativos en 0. Introduce no-linealidad para que la red pueda aprender patrones complejos.

        - Capa de Pooling
        Reduce el tamaño espacial del mapa de características. El más común es el Max Pooling, que toma el valor máximo de una ventana pequeña. Hjace el modelo más eficiente y con cierta toletancia.

        - Capa fully connected (FC)
        Al final, los mapas de características de "aplanan" y pasan por una red neuronal traducional que toma la decisión final (por ejemplo "es un perro" o "es un gato")

        Flujo típico de una CNN

        Imagen -> [Conv + ReLu] -> [Pooling] -> [Conv + ReLu] -> [Pooling] -> [Flatten] -> [FC] -> Salida

        Arquitecturas
        LeNet-5
        AlexNet
        VGG
        ResNet
        EfficientNet
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# ==================================
# 1) Preparar los datos
# ==================================

transforms = transforms.Compose([
    transforms.ToTensor(),  #Convierte imagen a tensor [0,1]
    transforms.Normalize((0.5,), (0.5,)) # Normaliza a [-1, 1]
])

train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transforms)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transforms)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(train_dataset, batch_size=64, shuffle=False)

# ==================================
# 2) Definir la arquitectura CNN
# ==================================

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self). __init__()

        # Bloque 1: Conv -> ReLu -> MaxPool
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1)
        # in_channels=1 porque MNIST es escala de grises
        # out_channels=32 significa que aprenderemos 32 filtros diferentes
        # kernel=size =3 -> filtro de 3x3

        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        # Reduce el tamaño espacial a la mitada 28x28 -> 14x14

        # Bloque 2: Conv -> ReLu -> MaxPool
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
        # Ahora tenemos 64 filtros, capturandoa patrones más complejos
        # 14x14 -> 7x7

        #Capas Fully Connected
        self.fc1 = nn.Linear(64 * 7 * 7, 128) # Aplamos : 64 canales * 7x7
        self.fc2 = nn.Linear(128, 10) # 10 canles (dígitos 0 - 9)

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5) # Regularización: apagar neronal al azar

    def forward(self, x):
        # x tiene forma [batch_size, 1, 28, 28]

        x = self.pool(self.relu(self.conv1(x))) # -> [batch, 32, 14, 14]
        x = self.pool(self.relu(self.conv2(x))) # -> [batch, 62, 7, 7]

        x = x.view(x.size(0), -1)

        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)

        return x # No aplicamos softmax aquí porque CrossEntropyloos lo incluye
    
# ==================================
# 3) Configurar Entrenamiento
# ==================================

