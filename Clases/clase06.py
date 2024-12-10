# Herencia

# Clase Padre
class Animal:
    def __init__(self, nombre):  # Atributos
        self.nombre = nombre

    def sonido(self): # Método
        return "El animal hace un sonido"
    
# Clase Hija
class Elefante(Animal):
    def sonido(self):
        return "Sonido elefante!!!"
    

class Leon(Animal):
    def sonido(self):
        return "Rugido"
    

mi_elefante = Elefante("Juanito")
mi_leon = Leon("Simba")

print(mi_leon.nombre)
print(mi_leon.sonido())

print(mi_elefante.nombre)
print(mi_elefante.sonido())

# Polimorfismo

print("----------------------------------------------------------")

class Gato(Animal):
    def sonido(self):
        return "Miua!!"
    
animales = [Elefante("Pepito"), Leon("Simba"), Gato("Michi")]

for animal in animales:
    print(f"{animal.nombre} dice: {animal.sonido()}")


class Ave(Animal):
    def __init__(self, nombre, puede_volar):
        # Llamar al constructor de la clase Padre (SUPER)
        super().__init__(nombre) # Molde Constructor del Padre
        self.pueder_volar = puede_volar

    def sonido(self):
        sonido_padre = super().sonido()
        return f"{sonido_padre} El ave canta!!"
    
mi_ave = Ave("Rio", True)
print(mi_ave.nombre)
print(mi_ave.sonido())

print("----------------------------------------------------------")

"""
Crea una clase padre llamada Tienda con:

Un constructor que reciba nombre, ubicacion y productos (una lista de productos disponibles). [x]
Un método mostrar_informacion() que imprima el nombre y la ubicación de la tienda. [x]
Un método mostrar_productos() que liste los productos disponibles. []


Crea dos clases hijas: []
TiendaDeRopa:
Hereda de Tienda.
Agrega un atributo tallas_disponibles (una lista). [X]
Sobrescribe el método mostrar_informacion() para incluir las tallas disponibles. [x]

TiendaDeElectronica:
Hereda de Tienda.
Agrega un atributo garantia (duración de garantía en meses).
Sobrescribe el método mostrar_informacion() para incluir la información de garantía.
Usa super() en los constructores de las clases hijas para inicializar los atributos de la clase padre.

Crea una función que reciba una lista de tiendas y use polimorfismo para mostrar la información de todas.
"""

# Clase Padre Tienda
class Tienda:
    def __init__(self, nombre, ubicacion, productos):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = productos

    def mostrar_informacion(self):
        print(f"Tienda: {self.nombre}\nUbicación: {self.ubicacion}")
    
    def mostrar_productos(self):
        print("Productos disponibles: ")
        for producto in self.productos:
            print(f"- {producto}")

# Clases Hija: Tienda Ropa
class TiendaDeRopa(Tienda):
    def __init__(self, nombre, ubicacion, productos, tallas_disponibles):
        super().__init__(nombre, ubicacion, productos)
        self.tallas_disponibles = tallas_disponibles

    def mostrar_informacion(self): #Polimorfismo del método mostrar_informacion()
        super().mostrar_informacion()
        super().mostrar_productos()
        print(f"Tallas disponibles: {', '.join(self.tallas_disponibles)}")
    

# Clase Hija: Tienda Electronica
class TiendaDeElectronica(Tienda):
    def __init__(self, nombre, ubicacion, productos, garantia): # Parametros de la nueva clase Hija
        super().__init__(nombre, ubicacion, productos) # Atriburos que ya existen de la clase Padre
        self.garantia = garantia

    def mostrar_informacion(self):
        super().mostrar_informacion() # Llamos a la clase SUPER (.super()) para traer el método mostrar_informacion
        super().mostrar_productos()
        print(f"Duración de la garantía: {self.garantia} meses") # Sobreescribimos un método Padre

# Función que usa el polimorfismo
def mostrar_tienda(lista_tiendas: list):
    for tienda in lista_tiendas:
        tienda.mostrar_informacion()
        print()

# Caso de Ejemplo

if __name__ == "__main__":
    tienda_ropa = TiendaDeRopa(
        "Liverpool", # Atributo Nombre
        "Av. Hidalgo", # Atributo Dirección
        ["Camisa", "Pantalón", "Zapatos", "Cinturones", "Calcetines"], # Atributo Productos
        ["Ch", "30", "25", "32", "Ch"] # SI
    )

    tienda_electronica = TiendaDeElectronica(
        "Steren",
        "Av. Ejercito Méxicano",
        ["Cable USB Tipo C", "Camara Vigilancia", "Foco Ingeligente", "Arduino MEGA"],
        12 # SI
    )

tiendas = [tienda_ropa, tienda_electronica] # Una lista de listas
mostrar_tienda(tiendas)


print("----------------------------------------------------------")

# try:
#     # Bloque de código que genera excepción
#     resultado = 10 / 0
# except ZeroDivisionError:
#     # Manejo de errores
#     print("Error: No se puede divir entre cero, mi chavo.")

# try:
#     print([1,2,3,4][3])
# except Exception as e:
#     print(f"Se ha producido un error: {e} ({type(e).__name__})")
