def suma(a:int, b:int) -> int:
    resultado = a + b # VARIABLE LOCAL
    return resultado

def multiplcar(resultado_suma, factor):
    resultado = resultado_suma * factor # VARIABLE LOCAL
    return resultado


resultado = suma(3, 5) # 8
resultado_final = multiplcar(resultado, 2) # 16
print(resultado_final)

print("-----------------------------------------------")

contador = 0

def incrementar():
    global contador # VARIABLE GLOBAL
    contador += 1

def mostrar_contador():
    print(f"Contador: {contador}")

incrementar()
incrementar()
incrementar()
mostrar_contador()

print("-----------------------------------------------")

def agregar_elemento(lista:list, elemento:int) -> list:
    lista.append(elemento)

def mostrar_lista(lista:list) -> list:
    print(f"Lista: {lista}")

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista, 4)
mostrar_lista(mi_lista)