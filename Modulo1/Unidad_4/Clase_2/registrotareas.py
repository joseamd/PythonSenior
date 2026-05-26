from datetime import datetime

NOMBRE_ARCHIVO = "tareas.txt"


def cargar_tareas():
    tareas = []

    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        for linea in lineas:
            partes = linea.strip().split("|")

            if len(partes) == 3:
                tarea = {
                    "descripcion": partes[0],
                    "estado": partes[1],
                    "fecha": partes[2]
                }
                tareas.append(tarea)

    except FileNotFoundError:
        pass

    return tareas


def guardar_todas_las_tareas(tareas):
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            linea = f"{tarea['descripcion']}|{tarea['estado']}|{tarea['fecha']}\n"
            archivo.write(linea)


def agregar_tarea():
    tareas = cargar_tareas()

    descripcion = input("Ingrese la nueva tarea: ").strip()

    if descripcion == "":
        print("No se puede guardar una tarea vacía.")
        return

    for tarea in tareas:
        if tarea["descripcion"].lower() == descripcion.lower():
            print("Esa tarea ya existe.")
            return

    nueva_tarea = {
        "descripcion": descripcion,
        "estado": "pendiente",
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tareas.append(nueva_tarea)
    guardar_todas_las_tareas(tareas)

    print("Tarea guardada correctamente.")


def mostrar_tareas():
    tareas = cargar_tareas()

    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    print("\n--- LISTADO DE TAREAS ---")

    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea['descripcion']}")
        print(f"   Estado: {tarea['estado']}")
        print(f"   Fecha: {tarea['fecha']}")


def mostrar_pendientes():
    tareas = cargar_tareas()

    pendientes = []

    for tarea in tareas:
        if tarea["estado"] == "pendiente":
            pendientes.append(tarea)

    if len(pendientes) == 0:
        print("No hay tareas pendientes.")
        return

    print("\n--- TAREAS PENDIENTES ---")

    for i, tarea in enumerate(pendientes, start=1):
        print(f"{i}. {tarea['descripcion']}")
        print(f"   Fecha: {tarea['fecha']}")


def marcar_completada():
    tareas = cargar_tareas()

    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    mostrar_tareas()

    try:
        numero = int(input("Ingrese el número de la tarea a completar: "))

        if numero < 1 or numero > len(tareas):
            print("Número de tarea inválido.")
            return

        tareas[numero - 1]["estado"] = "completada"
        guardar_todas_las_tareas(tareas)

        print("Tarea marcada como completada.")

    except ValueError:
        print("Debe ingresar un número válido.")


def eliminar_tarea():
    tareas = cargar_tareas()

    if len(tareas) == 0:
        print("No hay tareas para eliminar.")
        return

    mostrar_tareas()

    try:
        numero = int(input("Ingrese el número de la tarea a eliminar: "))

        if numero < 1 or numero > len(tareas):
            print("Número de tarea inválido.")
            return

        tarea_eliminada = tareas.pop(numero - 1)
        guardar_todas_las_tareas(tareas)

        print(f"Tarea eliminada: {tarea_eliminada['descripcion']}")

    except ValueError:
        print("Debe ingresar un número válido.")


def buscar_tarea():
    tareas = cargar_tareas()

    if len(tareas) == 0:
        print("No hay tareas para buscar.")
        return

    palabra = input("Ingrese palabra clave: ").lower()

    encontradas = []

    for tarea in tareas:
        if palabra in tarea["descripcion"].lower():
            encontradas.append(tarea)

    if len(encontradas) == 0:
        print("No se encontraron tareas.")
        return

    print("\n--- TAREAS ENCONTRADAS ---")

    for i, tarea in enumerate(encontradas, start=1):
        print(f"{i}. {tarea['descripcion']}")
        print(f"   Estado: {tarea['estado']}")
        print(f"   Fecha: {tarea['fecha']}")


def contar_tareas():
    tareas = cargar_tareas()

    total = len(tareas)
    pendientes = 0
    completadas = 0

    for tarea in tareas:
        if tarea["estado"] == "pendiente":
            pendientes += 1
        elif tarea["estado"] == "completada":
            completadas += 1

    print(f"Total de tareas: {total}")
    print(f"Pendientes: {pendientes}")
    print(f"Completadas: {completadas}")


def mostrar_menu():
    print("\n===== SISTEMA DE REGISTRO DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Buscar tarea")
    print("4. Contar tareas")
    print("5. Eliminar tarea")
    print("6. Marcar tarea como completada")
    print("7. Mostrar tareas pendientes")
    print("8. Salir")


def ejecutar_programa():
    opcion = ""

    while opcion != "8":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            buscar_tarea()
        elif opcion == "4":
            contar_tareas()
        elif opcion == "5":
            eliminar_tarea()
        elif opcion == "6":
            marcar_completada()
        elif opcion == "7":
            mostrar_pendientes()
        elif opcion == "8":
            print("Programa finalizado.")
        else:
            print("Opción inválida.")


ejecutar_programa()