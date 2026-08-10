# Clases_Python

Repositorio de apuntes y ejercicios de mis cursos de programación. Cada archivo es una **clase autocontenida**: primero la teoría explicada en comentarios (con diagramas, fórmulas y ejemplos de tablas), y después el código ejecutable que demuestra el tema.

La idea es que cualquier clase pueda abrirse, leerse y ejecutarse por sí sola, sin depender de las demás. Por eso hay conceptos que se repiten entre archivos: cada uno debe funcionar como material de estudio independiente.

## Cursos

| Curso | Carpeta | Clases | Alcance |
| --- | --- | --- | --- |
| Python | `Clases_Python/` | 43 | Fundamentos → estructuras de datos → algoritmos → Machine Learning → Deep Learning |
| C++ | `Clases_C++/` | 15 | Fundamentos, POO, STL y algoritmos de ordenamiento |
| SQL | `Clases_SQL/` | 8 | DDL, DML, DQL, JOINs, subconsultas y vistas |
| Flask | `Clases_Flask/` | 1 + proyecto | Microframework web: rutas, servidor de desarrollo |

Además:

- `Practicas/` — 8 ejercicios prácticos más largos, con el enunciado al inicio del archivo.
- `Proyecto/Memo.py` — Memorama jugable en terminal (matrices, `colorama`).

---

## Curso de Python

### Fundamentos (01–14)

| Clase | Tema |
| --- | --- |
| 01 | Funciones: de usuario, anidadas, built-in, `*args` |
| 02 | Estructuras de datos: listas, tuplas, sets, diccionarios |
| 03 | Cadenas de caracteres y sus métodos (`.replace()`, `.strip()`, …) |
| 04 | Variables globales y locales |
| 05 | Pilas (LIFO) y colas (FIFO) |
| 06 | Herencia y clases abstractas (`ABC`, `@abstractmethod`) |
| 07 | Excepciones y manejo de errores |
| 08 | Ficheros de texto (TXT) |
| 09 (p1/p2) | XML y protocolo HTTP (peticiones con `requests`) |
| 10 | Pruebas unitarias con `unittest` |
| 11 | Ciclos `for` |
| 12 | Listas por comprensión |
| 13 | Programación asíncrona (`asyncio`) |
| 14 | Listas anidadas y matrices |

### Librerías y herramientas (15–19)

| Clase | Tema |
| --- | --- |
| 15 | NumPy: arrays y operaciones vectorizadas |
| 16 | Matplotlib: gráficas de líneas, barras, dispersión, histogramas |
| 17 | Funciones lambda |
| 18 | Expresiones regulares (REGEX) |
| 19 | Interfaces gráficas con Tkinter |

### Árboles y grafos (21–27, 29–32, 34–35)

| Clase | Tema |
| --- | --- |
| 21 | Árboles binarios |
| 22 | Recorridos (inorden, preorden, postorden) |
| 23 | Valor máximo y mínimo en un árbol |
| 24 | Árboles espejo |
| 25 | Árboles balanceados |
| 26 | Árboles B y B+ |
| 27 | Árboles de sufijos |
| 29 | Grafos: representación y recorridos |
| 30 | Dijkstra (camino más corto) |
| 31 | Bellman-Ford (pesos negativos) |
| 32 | Floyd-Warshall (todos contra todos) |
| 34 | Kruskal (árbol generador mínimo) |
| 35 | DSU / Union-Find (conjuntos disjuntos) |

### Machine Learning (20, 28, 33, 36–41)

| Clase | Tema |
| --- | --- |
| 20 | Índice Gini como criterio de división |
| 28 | Árboles de decisión |
| 33 | Random Forest (ensambles) |
| 36 | Regresión logística y función sigmoide |
| 37 | Pipelines de preprocesamiento |
| 38 | Validación cruzada (cross-validation) |
| 39 (p1/p2) | KNN (K-Nearest Neighbors) |
| 40 | KNN aplicado a un sistema de recomendación |
| 41 | K-Means y centroides |

### Deep Learning (42–43)

| Clase | Tema |
| --- | --- |
| 42 | Redes neuronales convolucionales (CNN) |
| 43 | CNN de extremo a extremo: generación del dataset, entrenamiento y evaluación sobre `shapes_dataset/` |

---

## Curso de C++

| Clase | Tema |
| --- | --- |
| 01 (+ parte 2) | Tipos de datos, modificadores y operadores aritméticos |
| 02 | Entrada/salida, `getline` y validación del flujo de entrada |
| 03 | Ciclo `while` |
| 04 | Vectores: contenedor dinámico |
| 05 | Clases y objetos |
| 06 | Funciones |
| 07 | Ficheros (texto y binarios) |
| 08 | Arrays |
| 09 | Ordenamiento: Insertion Sort y Bubble Sort |
| 10 | Getters y setters (encapsulamiento) |
| 11 | Quicksort (divide y vencerás) |
| 12 | Vectores de la STL |
| 13 | Iteradores |
| 14 | Merge Sort |
| 15 | Expresiones lambda y funciones anónimas (C++11) |

`Clases_C++/Calculadora/` es un ejercicio de varios archivos (`main.cpp`, `Calculadora.h/.cpp`, `Operando.h/.cpp`) que aplica clases, encapsulamiento y separación en cabeceras.

Los diagramas de los algoritmos de ordenamiento (`burbuja.drawio`, `insertion_sort.drawio`, `quicksort.drawio`, `claseUML.drawio`) están en `Archivos/`.

---

## Curso de SQL

| Clase | Tema |
| --- | --- |
| 01 | Qué es SQL, las 5 categorías (DDL, DML, DQL, DCL, TCL) y buenas prácticas |
| 02 | Tipos de datos de las columnas |
| 03 | DDL: `CREATE`, `ALTER`, `DROP` |
| 04 | DML: `INSERT`, `UPDATE`, `DELETE` |
| 05 | DQL: `SELECT` a fondo |
| 06 | JOINs: `INNER`, `LEFT`, `RIGHT`, `FULL` |
| 07 | `SELF JOIN` y relaciones de una tabla consigo misma |
| 08 | Subconsultas (subqueries) y vistas (views) |

Son scripts didácticos: no apuntan a ninguna base de datos en particular. Para probarlos, ejecútalos sobre un esquema de pruebas en MySQL/MariaDB.

---

## Curso de Flask

- `Clases_Flask/Notas-Flask/Clase01.py` — teoría: qué es Flask, Werkzeug y Jinja2, instalación en entorno virtual y estructura mínima de un proyecto.
- `Clases_Flask/project_flask_traning/app.py` — aplicación de práctica con las rutas `/`, `/acerca` y `/contacto`.

---

## Prácticas

| Práctica | Enunciado |
| --- | --- |
| 01 | Invertir una cadena |
| 02 | Análisis de una frase ingresada por el usuario |
| 03 | Registro de estudiantes, calificaciones y estadísticas |
| 04 | Clase `TaskManager` (CRUD de tareas con ID, título, descripción y estado) |
| 05 | Inventario de productos electrónicos persistido en JSON |
| 06 | Reporte semanal de ventas a partir de un JSON |
| 07 | Resumen estadístico de calificaciones desde un CSV |
| 08 | Cadenas de suministro: costo recursivo y detección de ciclos en un grafo dirigido |

---

## Cómo ejecutar

### Python

```powershell
python Clases_Python\clase36.py
```

> **Importante:** las rutas a los archivos de datos están escritas de forma relativa. La mayoría de las clases y prácticas leen los datasets de la raíz del repositorio (`productos.json`, `clientes_10000.csv`, `shapes_dataset/`), así que deben ejecutarse **desde la raíz**. En cambio, las clases de ficheros usan archivos que viven en `Archivos/` (`ejemplo.txt`, `entrada.txt`, `salida.txt`), y necesitan ejecutarse **desde esa carpeta**. Si aparece un `FileNotFoundError`, casi siempre es la carpeta de trabajo, no un archivo faltante.

Dependencias según el tema: `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `tensorflow`, `torch`, `requests`, `colorama`, `pillow`.

### C++

Compilado con g++ de MSYS2 (UCRT). La tarea de VS Code (`.vscode/tasks.json`) compila el archivo activo con `Ctrl+Shift+B`:

```powershell
& C:\msys64\ucrt64\bin\g++.exe -g Clases_C++\clase11.cpp -o Clases_C++\clase11.exe
```

Los ejecutables ya compilados están en `Clases_C++/Ejecutables_C++/`.

### Flask

El entorno virtual `venv/` incluido está dedicado a Flask:

```powershell
.\venv\Scripts\Activate.ps1
python Clases_Flask\project_flask_traning\app.py
```

El servidor queda en <http://127.0.0.1:5000/> con `debug=True` (recarga automática; nunca usar así en producción).

---

## Datos

En la raíz están los datasets compartidos por varias clases y prácticas: `clientes_10000.csv`, `calificaciones_ampliado.csv`, `food_store_purchases.csv`, `raw_workorders.csv`, `inventario.json`, `ventas.json`, `productos.json`, `dependencias.json`, `tareas.json` y archivos Parquet.

Varios se generan con scripts:

```powershell
python generar_clientes.py     # clientes_10000.csv
python generador_dataset.py
python generar_figuras.py      # shapes_dataset/ (círculos, cuadrados y triángulos)
```

`data/MNIST/` contiene el dataset usado en las clases de redes neuronales, y `Archivos/` los archivos de ejemplo de las clases de entrada/salida.
