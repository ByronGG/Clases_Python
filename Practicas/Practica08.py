"""
Ejercicio: Detección de Cadenas de Suministro y Cálculo de Costos

Una empresa tiene una lista de productos y una lista de dependencias entre ellos:
    Cada producto puede estar compuesto de otros productos (por ejemplo, un "PC" está compuesto de "Motherboard", "CPU", "RAM", etc).
    Las dependencias se almacenan en una estructura como un grafo dirigido (lista de pares: producto principal, producto componente).
    Cada producto base tiene un costo unitario.
    Los productos compuestos no tienen costo propio; su costo es la suma recursiva de sus componentes.

Tu objetivo:
    Dado un producto final, calcular recursivamente su costo total (sumando el costo de cada componente base, aunque se repitan en el árbol).
    Detectar ciclos de dependencia en la cadena de suministros (por ejemplo, si por error alguien hace que un producto dependa de sí mismo directa o indirectamente).
"""

import json

def cargar_datos():
    with open("productos.json", "r", encoding="utf-8") as f:
        productos = json.load(f)
    with open("dependencias.json", "r", encoding="utf-8") as f:
        dependencias = json.load(f)
    return productos, dependencias

def construir_diccionarios(productos, dependencias):
    # Diccionario de costos base: {nombre: costo}
    costos = {p["nombre"]: p["costo"] for p in productos}

    # Diccionario de dependencias: {producto: [componentes]}
    deps = {} # Dict vacio
    for padre, hijo in dependencias:
        deps.setdefault(padre, []).append(hijo)
    return costos, deps

# Tarea
def costo_total(productos, costos, deps):
    """
        Si el productos es "basico" (tiene costo propio), lo devolvemos.
        Si es "compuesto", sumamos recursivamente el costo de todos sus componentes (puede haber recursividad profunda)
    """
    pass

def tiene_ciclo(deps):
    visitado = set()
    en_pila = set()

    def dfs(nodo):
        visitado.add(nodo)
        en_pila.add(nodo)
        for vecino in deps.get(nodo, []):
            if vecino not in visitado:
                if dfs(vecino):
                    return True
            elif vecino in en_pila:
                # Detenctamos el ciclo
                return True
        en_pila.remove(nodo)
        return False
    
    #Probar desde cada nodo (por si hay varios árboles)
    for nodo in deps:
        if nodo not in visitado:
            if dfs(nodo):
                return True
    return False

def main():
    productos, dependencias = cargar_datos()
    costos, deps = construir_diccionarios(productos, dependencias)

    while True:
        print("\n--- Cadenas de Suministros ---")
        print("1. Calcular costo total de un producto")
        print("2. Detectar ciclos en dependencias")
        print("3. Salir")
        opcion = input("Elige una opción (1 - 3): ").strip()

        if opcion == "1":
            nombre = input("Producto final: ").strip()
            if nombre not in costos:
                print("Ese producto no existe")
            else:
                try:
                    total = costo_total(nombre, costos, deps)
                    print(f"Costo total de {nombre}: ${total}")
                except Exception as e:
                    print(f"Error calculo costos: {e}")
        elif opcion == "2":
            if tiene_ciclo(deps):
                print("¡Se detectó un cilco en las dependencías!")
            else:
                print("No hay ciclos, Las dependencias son válidas!")
        elif opcion == "3":
            print("Hasta Luego")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()