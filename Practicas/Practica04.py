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


class TaskManager:
    # Que permita gestionar tareas. Cada
    # tarea debe tener un ID unico, un titulo
    # una descripción, y un estado (pendiente,
    # en progreso, completado)

    # Constructor
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.task = {}
        self.next_id = 1
        self.status = {"Pendiente", "Proceso", "Completada"}
        self.cargar_tarea()

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
        with open(self.archivo, "w") as f:
            json.dump(
                {
                    "task": self.task,
                    "next_id": self.next_id,
                },
                f,
                indent=4,
            )

    def add_task(self):
        # Agregar nueva tarea con el estado pendiente

        titulo = input("Introduce el titulo: ").strip()
        while not titulo:
            titulo = input("El titulo no puede estar vacio, intente de nuevo.").strip()

        descripcion = input("Introduce la descripción: ").strip()
        while not descripcion:
            descripcion = input("Descripción no puede estar vacia.").strip()

        task = {
            "id": self.next_id,
            "titulo": titulo,
            "descripcion": descripcion,
            "estado": "Pendiente",
        }

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
        try:
            id = int(input("ID de la tarea a actulizar: "))
            if id not in self.task:
                print("No existe una tarea con ese ID")
                return
            print("Estado válidos: ", self.status)
            nuevo_estado = input("Nuevo estado: ")
            while nuevo_estado not in self.status:
                nuevo_estado = (
                    input("Estado inválido. Intenta de nuevo: ").strip().capitalize()
                )
            self.task[id]["estado"] = nuevo_estado # Asignacion (variable nueva => dato viejo)
            self.guardar_tarea()
            print("Estado actualizado")
        except ValueError:
            print("ID inválido")

    def delete_task(self):
        try:
            id = int(input("ID de la tarea a eliminar: "))
            if id in self.task:
                del self.task[id]
                self.guardar_tarea()
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
            task
            for task in self.task.values()
            if estado is None or task["estado"] == estado
        ]

        if tareas:
            for t in tareas:
                print(
                    f"\nID: {t['id']}\nTítulo: {t['titulo']}\nDescipción: {t['descripcion']}\nEstado: {t['estado']}"
                )
            else:
                print("No hay tareas para mostrar.")


def menu():
    tm = TaskManager()
    opciones = {
        "1": tm.add_task,
        "2": tm.get_task,
        "3": tm.update_status,
        "4": tm.delete_task,
        "5": tm.list_tasks,
        "6": exit,
    }

    while True:
        # CRUD
        print("\n--- MENÚ ---")
        print("1. Agregar tarea") # Create
        print("2. Ver tarea por ID") # Read
        print("3. Actualizar estado de tarea") #Update
        print("4. Eliminar tarea") # Delete
        print("5. Listar tareas") # Read
        print("6. Salir")

        opcion = input("Elige una opción: ").strip()
        accion = opciones.get(opcion)

        if accion:
            accion()
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()