# Memorama por Terminal
import random
import os
import time

def crear_tablero(tam):
    simbolos = list(range(1, (tam**2)//2 + 1)) * 2# Tamaño 4 -> (16)//2 + 1 -> 8 + 1 -> 9 [1,2,3,4,5,6,7,9] * 2 -> [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
    random.shuffle(simbolos)
    tablero = [] # Crear la matriz de tablero
    for i in range(tam):
        fila = simbolos[i*tam : (i+1) * tam]
        tablero.append(fila)
    return tablero

def mostrar_tablero(tablero, reveladas):
    os.system('cls' if os.name == 'nt' else 'clear') # Limpieza Patanlla 
    print("  " + " ".join(str(i+1).rjust(2) for i in range(len(tablero)))) # 4x4 -> 1 2 3 4
    print(" +" + "--" * len(tablero)) # -> --
    for i, fila in enumerate(tablero):
        print(f"{i+1} |", end=" ") # -> |
        for j, valor in enumerate(fila):
            if reveladas[i][j]:
                print(str(valor).rjust(2), end=" ")
            else:
                print(" X", end=" ")
        print()

def obtener_coordenadas(tam):
    while True:
        try:
            fila = int(input("Elige fila (1 - " + str(tam) + "): ")) - 1
            columna = int(input("Elige columna (1 - " + str(tam) + "): ")) - 1
            if 0 <= fila < tam and 0 <= columna < tam:
                return (fila, columna)
            print("¡Coordenadas fuera de rango!")
        except ValueError:
            print("¡Ingresa solo números!")

def main():
    tam = 4 # Modificable
    tablero = crear_tablero(tam)
    reveladas = [[False for _ in range(tam)] for _ in range(tam)]
    intentos = 0
    pares_encontrados = 0

    while pares_encontrados < (tam**2)//2:
        mostrar_tablero(tablero, reveladas)

        # Primera seleccion
        print("\nPrimera carta:")
        f1, c1 = obtener_coordenadas(tam)
        while reveladas[f1][c1]:
            print("¡Esa carta ya está revelada!")
            f1, c1 = obtener_coordenadas(tam)

        reveladas[f1][c1] = True
        mostrar_tablero(tablero, reveladas)

        # Segunda selección
        print("\nSegunda carta:")
        f2, c2 = obtener_coordenadas(tam)
        while reveladas[f2][c2] or (f1 == f2 and c1 == c2):
            if reveladas[f2][c2]:
                print("¡Esa carta ya está revelada!")
            else:
                print("¡No pedes seleccionar la misma carta!")
            f2, c2 = obtener_coordenadas(tam)

        reveladas[f2][c2] = True
        mostrar_tablero(tablero, reveladas)
        intentos += 1

        # Verificar pareja
        if tablero[f1][c1] == tablero[f2][c2]:
            pares_encontrados += 1
            print(f"\n¡Encontraste una pareja! ({pares_encontrados}/{(tam**2)//2})")
        else:
            print("\nNo es pareja...")
            time.sleep(2)
            reveladas[f1][c1] = False
            reveladas[f2][c2] = False
        
        input("Presiona Enter para continuar...")

    print(f"\n¡Felicidades! Completaste el juego {intentos} intentos!")

if __name__ == "__main__":
    main()
