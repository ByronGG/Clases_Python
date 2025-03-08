"""
    Matplotlib es una biblioteca de Python utilizada para la visualización de datos. Permite crear gráficos de diferentes tipos, como líneas, barras, dispersión (scatter), histogramas, gráficos 3D, entre otros.
    Se diseñó para proporcionar una interfaz similar a MATLAB, lo que la hace sencilla de usar y flexible para diferentes tipos de gráficos.

    Conceptos Claves en Matplotlib
        - Figura (Figure) → Es el lienzo donde se colocan los gráficos.
        - Ejes (Axes) → Son los espacios dentro de la figura donde se dibujan los gráficos.
        - Rangos de Ejes (Axis) → Controlan los límites y escalas del gráfico.
        - Leyendas (Legend) → Muestra etiquetas de las curvas o datos.
        - Estilos (Style) → Permiten cambiar la apariencia de los gráficos.

        marker='o' -> Muestra puntos de los datos
        linestyle='-' -> Típo de línea (puede ser '--', ':', '-.', ect)
        color='b' -> Color de la línea (puede ser 'r', 'g', 'k', etc)

        bins=30 -> Número de divisiones en el histograma
        edgecolor -> Borde negro en cada barra

        labels=etiquetas -> Asigna nombres a las secciones
        autopct="%1.1f%%" -> Muestra el porcentaje con 1 decimal
        colors=['red', 'blue', 'yellow', 'violet'] -> Lista de colores personalizados

        FuncAnimation(fig, update, frames=....) -> Crea la animación
        init_frames=init -> Configuracion inicial
        blit=True -> Optimiza la animación

        fill_between(x, y, alpha=0.3) -> Rellena area bajo la curva
        alpha=0.3 -> Transparencia del sombreado (más cerca del 0 es más tenue y más cerca del 1 es más solido)
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animiation
import mplcursors

x = [1, 2, 3 ,4, 5]
y = [10, 15, 7, 20, 13]

plt.plot(x, y, marker='o', linestyle='-.', color='r') # Gráfico de línea
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title(" Ejemplo ")
plt.legend()
plt.show()


print("------------------------------------------------------------------------------------")

catergorias = ["A", "B", "C", "D", "E"]
valores = [20, 35, 30, 25, 40]

plt.bar(catergorias, valores, color='c')
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Gráfico de Barras")
plt.show()

print("------------------------------------------------------------------------------------")

x = np.random.rand(50) # 50 valores aleatorios en X
y = np.random.rand(50) # 50 valores aleatorios en Y

plt.scatter(x, y, color='r', marker='x')  # Puntos rojos con forma de X
plt.title("Gráfico de Dispersión")
plt.show()

print("------------------------------------------------------------------------------------")

datos = np.random.randn(1000) # 1000 datos aleatorios con distribución normal

plt.hist(datos, bins=30, color='g', edgecolor='black') # 30 divisiones
plt.title("Histograma de Datos")
plt.show()

print("------------------------------------------------------------------------------------")

etiquetas = ["A", "B", "C", "D"]
valores = [25, 35, 20, 20]

plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", colors=['red', 'blue', 'yellow', 'violet'])
plt.title("Gráffico Circular")
plt.show()

print("------------------------------------------------------------------------------------")

x = [1, 2, 3, 4, 5]
y1 = [9, 11, 14, 18, 30]
y2 = [200, 500, 1500, 2000, 11000]

plt.plot(x, y1, label="Serie 1", color='b')
plt.plot(x, y2, label="Serie 2", color='r')

plt.legend() # Agregar una leyenda
plt.show()

print("------------------------------------------------------------------------------------")

plt.figure(figsize=(10, 5)) # Tamaño de la figura

plt.subplot(1, 2, 1) # Fila 1, 2 Columnas, gráfico en la posición 1
plt.plot([1, 2, 3], [1, 4, 9], marker='o', color='r')
plt.title("Gráfico 1")

plt.subplot(1, 2, 2) # Fila 1, 2 Columnas, gráfico en la posición 2
plt.plot(["A", "B", "C"], [5, 7, 3], linestyle='--', marker='x', color='g')
plt.title("Gráfico 2")

plt.tight_layout() # Ajusta los espacios automaticamente
plt.show()


print("------------------------------------------------------------------------------------")

fig, ax1 = plt.subplots()

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x) * 10

ax1.plot(x, y1, 'r-.', label='Seno')
ax1.set_xlabel("Eje X")
ax1.set_ylabel("Seno", color='g')

ax2 = ax1.twinx() # Segundo eje Y
ax2.plot(x, y2, "b--", label='Coseno x10')
ax2.set_ylabel("Coseno x10", color='b')

plt.title("Múltples Ejes Y")
plt.show()

print("------------------------------------------------------------------------------------")

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y) # La función numpy.meshgrid devuelve una lista de matrices de coordenadas a partir de vectores de coordenadas.
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.title("Gráfico 3D")
plt.show()

print("------------------------------------------------------------------------------------")

fig, ax = plt.subplots()

xdata, ydata = [], []
ln, = plt.plot([], [])

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame) * 5 + 5)
    ln.set_data(xdata, ydata)
    return ln,

ani = animiation.FuncAnimation(fig, update, frames=np.linspace(0, 10, 100),
                                init_func=init, blit=True)

plt.show()


print("------------------------------------------------------------------------------------")

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, 'r:', label="Seno")
plt.title("Gráfico Interactivo")

mplcursors.cursor() # Activa interacción en el cursos

plt.show()

print("------------------------------------------------------------------------------------")

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, 'k', label="Seno")
plt.fill_between(x, y, alpha=0.3, color='g')
plt.legend()
plt.show()