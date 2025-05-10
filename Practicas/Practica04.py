"""
Crea una clase llamada TaskManager que permita gestionar una lista de tareas. Cada tarea debe tener un ID único, un título, una descripción, y un estado (pendiente, en progreso, completada).

Implementa los siguientes métodos:

    add_task(titulo, descripcion)  Agrega una nueva tarea con estado por defecto "pendiente".
    get_task(id) Devuelve la información de la tarea con el ID dado.
    update_status(id, nuevo_estado)  Actualiza el estado de la tarea (solo acepta los 3 valores válidos).
    delete_task(id)  Elimina una tarea por ID.
    list_tasks(estado=None)  Lista todas las tareas. Si se pasa un estado, solo lista las tareas con ese estado.
    Añade validaciones de entrada.
    Guarda las tareas en un archivo .json para persistencia entre ejecuciones.

"""
import os
import json

class TaskManager():
    # Que permita gestionar tareas. Cada
    # tarea debe tener un ID unico, un titulo
    # una descripción, y un estado (pendiente,
    # en progreso, completado)

    # Constructor
    def __init__(self, archivo ="tareas.json"):
        self.archivo = archivo
        self.task = {}
        self.next_id = 1
        self.status = {"Pendiente", "Proceso", "Completada"}
        self.cargar_tarea()

    # usa metodos

    def add_task(self):
        # Agregar nueva tarea con el estado pendiente

        titulo = input("Introduce el titulo: ").strip()
        while not titulo:
            titulo = input("El titulo no puede estar vacio, intente de nuevo.").strip()
  
        descripcion = input("Introduce la descripción: ").strip()
        while not descripcion:
            descripcion = input("Descripción no puede estar vacia.").strip()

        task = {"id": self.next_id,
                "titulo": titulo,
                "descripcion": descripcion,
                "estado": "Pendiente"}
        
        self.task[self.next_id] = task
        self.next_id += 1
        self.guardar_tarea()
        print(f"Se guardo tarea con el {titulo} y la Id {task['id']}")

    def get_task(self):
        try:
            id = int(input("Introduce el ID de la tarea"))
            task = self.task.get(id)
            if task:
                print(task)
            else:
                print("No se encontro la tarea")
        except ValueError:
            print("El ID debe ser numerico.")


    def update_status(self):
        pass

    def delete_task(self):
        try:
            id = int(input("ID de la tarea a eliminar: "))
            if id in self.task:
                del self.task[id]
                print("Tearea eliminada")
            else:
                print("No se encontró la tarea")
        except ValueError:
            print("ID inválido")

    
    def list_tasks(self):
        print("¿Deseas filtrar por estado? (s/n) ")
        filtrar = input().strip().lower()
        estado = None
        if filtrar == "S":
            estado = input("Estado (pendiente, Proceso, Completada): ").strip().lower()
            while estado not in self.status:
                estado = input("Estado inválido, Intenta de nuevo: ").strip().lower()

        tareas = [
            task for task in self.task.values()
            if estado is None or task["estado"] == estado
        ]

        if tareas:
            for t in tareas:
                print(f"\nID: {t['id']}\nTítulo: {t['titulo']}\nDescipción: {t['descripcion']}\nEstado: {t['estado']}")
            else:
                print("No hay tareas para mostrar.")

    # Cargar tarea
    def cargar_tarea(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.task = {int(k): v for k, v in data["task"].items()}
                self.next_id = data["next_id"]
        else:
            self.guardar_tarea()
    
    # Guardar tarea
    def guardar_tarea(self):
          with open(self.archivo, "w")as f: 
            json.dump({
                "task": self.task,
                "next_id": self.next_id,
            }, f, indent=4)


def menu():
    tm = TaskManager()
    opciones = {
        "1": tm.add_task,
        "2": tm.get_task,
        "3": tm.update_status,
        "4": tm.delete_task,
        "5": tm.list_tasks,
        "6": exit
    }

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar tarea")
        print("2. Ver tarea por ID")
        print("3. Actualizar estado de tarea")
        print("4. Eliminar tarea")
        print("5. Listar tareas")
        print("6. Salir")

        opcion = input("Elige una opción: ").strip()
        accion = opciones.get(opcion)

        if accion:
            accion()
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()