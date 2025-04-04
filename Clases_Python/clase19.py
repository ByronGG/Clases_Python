# Tkinter
"""
    * pack(): Organiza widgets en bloques (vertical/horizontal)
    * grid(): Disposición en filas y columnas
    * place(): Posicionamiento absoluto o relativo (obsoleto)
    * Frame(): Contenedor para organizar otros widgets
    * Entry(): Permite entrada de texto
"""

import tkinter as tk

# Crear la ventara principal
ventana = tk.Tk() # inicializa la venta principal -> Clase padre tkinter .Tk() HEREDANDO tkinter
ventana.title("Mi app chafa") # Titulo la ventana
ventana.geometry("600x500") # Tamaño inicial (ancho x alto)

# Mantener la venta abierta y a la espera de eventos
ventana.mainloop()


print("--------------------------------------------------------------------------------------")

ventana = tk.Tk()
ventana.title("Widgets Básicos")
ventana.geometry("250x250")

# Widget Label
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!", font=("Arial", 14))
etiqueta.pack(pady=10)

# Widget Button
def saludar():
    etiqueta.config(text="¡Boton presionado!")

boton = tk.Button(ventana, text="Presionar", command=saludar)
boton.pack(pady=10)

ventana.mainloop()

print("--------------------------------------------------------------------------------------")

class MiApp: # -> Clase Padre
    def __init__(self, ventana): # -> def __init__ Declarar atributos / self 
        self.ventana = ventana # -> Atriburo ventana = Variable ventana (Self)
        ventana.title("Mi App")

        # Crear widgets
        self.etiqueta = tk.Label(ventana, text="Hola, Tkinter!")
        self.etiqueta.pack()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = MiApp(ventana)
    ventana.geometry("250x250")
    ventana.mainloop() # Renderizar ventana

"""
    Buenas prácticas iniciales
        * Organizar con clases: Facilita el manejo de widgets y eventos
        * Evitar mezcar pack() y grid() en el mismo contendor
        * Use ttk para estilos modernos: El módulo tkinter.ttk ofrece widgets más actualizados.
"""

print("--------------------------------------------------------------------------------------")

def enviar():
    nombre = entrada_nombre.get()
    bio = cuadro_texto.get("1.0", tk.END) # -> "1.0" Indica desde el primer carácter de texto / END Termina en el último caracter
    print(f"Nombre: {nombre}\nBio: {bio}")

ventana = tk.Tk()
ventana.title("Formulario")

# Frame Principal
frame = tk.Frame(ventana)
frame.pack(padx=10, pady=10)

# Entrada de nombre
tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="w")
entrada_nombre = tk.Entry(frame, width=30)
entrada_nombre.grid(row=0, column=1, pady=5)

# Cuadro de texto (Bio)
tk.Label(frame, text="Bio:").grid(row=1, column=0, sticky="nw")
cuadro_texto = tk.Text(frame, width=25, height=5)
cuadro_texto.grid(row=1, column=1, pady=5)

# Boton enviar
tk.Button(frame, text="Enviar", command=enviar).grid(row=2, column=1, pady=10)

ventana.mainloop()

print("--------------------------------------------------------------------------------------")


def accion(opcion):
    print(f"Opcion seleccionada: {opcion}")

ventana = tk.Tk()
ventana.title("Menús")

# Barra de menú
barra_menu = tk.Menu(ventana)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=lambda: accion("Abrir"))
menu_archivo.add_command(label="Guardar", command=lambda:accion("Guardar"))
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=lambda: accion("Arcerca de"))
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(menu=barra_menu)
ventana.mainloop()


print("--------------------------------------------------------------------------------------")

ventana = tk.Tk()
ventana.title("Lista con Scroll")

# Frame contendor
frame = tk.Frame(ventana)
frame.pack(padx=10)
frame.pack(pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox
lista = tk.Listbox(frame, width=40, yscrollcommand=scrollbar.set)
for i in range(100):
    lista.insert(tk.END, f"Elemento {i + 1}")
lista.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=lista.yview)
ventana.mainloop()

print("--------------------------------------------------------------------------------------")

def convertir():
    fahrenheit = entrada_fahrenheit.get()
    celsius = (float(fahrenheit) - 32) * 5/9
    etiqueta_resultado.config(text=f"{celsius:.2f} °C")

ventana = tk.Tk()
ventana.title("Conversor De Temperatura")

# Widgets
tk.Label(ventana, text="fahrenheit:").grid(row=0, column=0, padx=10, pady=10)
entrada_fahrenheit = tk.Entry(ventana)
entrada_fahrenheit.grid(row=0, column=1, padx=10, pady=10)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.grid(row=1, column=0, columnspan=2, pady=10)

tk.Button(ventana, text="Convertir", command=convertir).grid(row=2, column=0, pady=10)
ventana.mainloop()