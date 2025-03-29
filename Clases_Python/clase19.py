# Tkinter

import tkinter as tk

# Crear la ventara principal
ventana = tk.Tk() # inicializa la venta principal -> Clase padre tkinter .Tk() HEREDANDO tkinter
ventana.title("Mi app chafa") # Titulo la ventana
ventana.geometry("600x500") # Tamaño inicial (ancho x alto)

# Mantener la venta abierta y a la espera de eventos
ventana.mainloop()


import tkinter as tk

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
