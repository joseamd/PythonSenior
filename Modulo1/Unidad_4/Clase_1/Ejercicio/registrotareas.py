"""
Enunciado del ejercicio

Desarrolla un programa llamado Sistema de Registro de Tareas.

El programa debe permitir al usuario:

Agregar una nueva tarea.
Ver todas las tareas guardadas.
Buscar una tarea por palabra clave.
Contar cuántas tareas hay registradas.
Salir del programa.

Las tareas deben guardarse en un archivo llamado:

tareas.txt

Cada tarea debe almacenarse en una línea diferente.

Requisitos técnicos

El programa debe usar:

open()

Bloque seguro:

with open(...)

Funciones:

agregar_tarea()
mostrar_tareas()
buscar_tarea()
contar_tareas()

Un ciclo while para mantener activo el menú.

Condicionales if, elif, else para controlar las opciones.

Una lista para almacenar temporalmente las tareas leídas desde el archivo.

Ejemplo de ejecución esperada
===== SISTEMA DE REGISTRO DE TAREAS =====
1. Agregar tarea
2. Ver tareas
3. Buscar tarea
4. Contar tareas
5. Salir

Seleccione una opción: 1
Ingrese la nueva tarea: Estudiar manejo de archivos en Python
Tarea guardada correctamente.

Seleccione una opción: 2

--- LISTADO DE TAREAS ---
1. Estudiar manejo de archivos en Python
2. Comprar materiales para clase
3. Revisar ejercicios pendientes

Retos adicionales para estudiantes
Agregar una opción para eliminar tareas.
Agregar una opción para marcar tareas como completadas.
Guardar cada tarea con fecha.
Evitar tareas repetidas.
Mostrar solo tareas pendientes.
"""
NOMBRE_ARCHIVO = "tareas.txt"

def mostrar_menu():
    menu = """
        ========================================
            SISTEMA DE REGISTRO DE TAREAS
        ========================================
        1. Agregar tarea
        2. Ver tareas
        3. Buscar tarea
        4. Contar tareas
        5. Eliminar tarea
        6. Marcar tarea como completada
        7. Mostrar tareas pendientes
        8. Salir del programa
        ========================================
        """
    print(menu)


def cargar_tareas():
    try:
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            tareas = archivo.readlines()

            tareas_limpias = []

            for tarea in tareas:
                tareas_limpias.append(tarea.strip())

            return tareas_limpias

    except FileNotFoundError:
        return []
    
def guardar_tarea(tarea):
    with open(NOMBRE_ARCHIVO, 'a', encoding='utf-8') as archivo:
        archivo.write("[ ] " + tarea + "\n")

def agregar_tarea():
    tarea = input("Ingrese la nueva tarea: ")

    if tarea.strip() == "":
        print("Debe ingresar una tarea válida")
    else:
        guardar_tarea(tarea)
        print("Tarea guardada correctamente")

def guardar_lista_tareas(lista):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
            for tarea in lista:
                archivo.write(tarea + '\n')

def mostrar_tareas():
    print("--- LISTADO DE TAREAS ---")

    tareas = cargar_tareas()

    if not tareas:
        print("No hay tareas registradas")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f'{i}. {tarea}')      

def buscar_tarea():
    print("--- BUSCAR TAREAS ---")
    tarea_buscar = input("Ingrese la tarea a buscar: ")
    if tarea_buscar.strip() == "":
        print("Ingrese una tarea válida")
        return
    
    tareas = cargar_tareas()
    encontrada = False

    for tarea in tareas:
        if tarea_buscar.lower() in tarea.lower():
            print(f'Tarea encontrada: {tarea}')
            encontrada = True

    if not encontrada:
        print("La tarea no existe")
    
    input("\nPresione Enter para volver al menú...")

def contar_tareas():
    print("--- TOTAL DE TAREAS ---")

    tareas = cargar_tareas()

    if not tareas:
        print("No hay tareas registradas!!!")
    else:
        cantidad = len(tareas)
        print(f'Total de tareas registradas: {cantidad}')
    
    # Volver al menú
    input("\nPresione Enter para volver al menú...")  

def eliminar_tarea():
    print("--- ELIMINAR TAREAS ---\n")

    while True:
        lista = cargar_tareas()

        if not lista:
            print("No hay tareas registradas")
            break

        mostrar_tareas()

        num_eliminar = input("\nIngrese el número de la tarea a eliminar ó 0 para volver al menú: ")

        if not num_eliminar.isdigit():
            print("Debe ingresar un número válido")
            continue           
        
        num_eliminar = int(num_eliminar)

        if num_eliminar == 0:
            break

        if num_eliminar < 1 or num_eliminar > len(lista):
            print("El número de tarea no existe")
            continue
        
        confirmacion = input("¿Desea eliminar la tarea? (s/n): ").lower() 

        if confirmacion not in ["s", "n"]:
            print("Debe ingresar solamente 's' o 'n'")
            continue

        if confirmacion == "n":
            print("Eliminación cancelada")
            continue

        tarea_eliminada = lista.pop(num_eliminar - 1)

        guardar_lista_tareas(lista)

        print(f"Tarea eliminada satisfactoriamente: {tarea_eliminada}")

        # Validar respuesta
        continuar = input("¿Desea eliminar otra tarea? (s/n): ").lower() 
        if continuar not in ["s", "n"]:
            print("Debe ingresar solamente 's' o 'n'")
            continue

        if continuar == "n":
            break

def marcar_completada():
    print("--- COMPLETAR TAREAS ---\n")

    while True:
        tareas = cargar_tareas()

        if not tareas:
            print("No hay tareas registradas")
            break

        mostrar_tareas()

        num_tarea = input("\nIngrese el número de la tarea completada ó 0 para volver al menú: ")

        # Validar número
        if not num_tarea.isdigit():
            print("Debe ingresar un número válido")
            continue        
        
        num_tarea = int(num_tarea)

        # Volver al menú
        if num_tarea == 0:
            break

        # Validar rango
        if num_tarea < 1 or num_tarea > len(tareas):
            print("El número de tarea no existe")
            continue

        # Obtener tarea seleccionada
        tarea_actual = tareas[num_tarea - 1]

        # Validar si ya está completada
        if tarea_actual.startswith("[x]"):
            print("La tarea ya está completada")
            continue
        
        # Limpiar estado anterior y marcar como completada
        tarea_limpia = tarea_actual.replace("[ ] ", "")

        tareas[num_tarea - 1] = f"[x] {tarea_limpia}"
        
        # Reescribir archivo
        guardar_lista_tareas(tareas)        

        print(f'Tarea completada: {tarea_limpia}')

        continuar = input("¿Desea marcar otra tarea como completada? (s/n): ").lower()

        # Validar respuesta
        while continuar not in ["s", "n"]:
            continuar = input("Ingrese solamente 's' o 'n': ").lower()

        if continuar == "n":
            break

def mostrar_tareas_pendientes():
    print("--- TAREAS PENDIENTES ---\n")

    tareas = cargar_tareas()

    # Validar si existen tareas
    if not tareas:
        print("No hay tareas registradas")
        return   

    encontradas = False          
        
    for i, tarea in enumerate(tareas, 1):
        if tarea.startswith("[ ]"):
            print(f'{i}. {tarea}') 
            encontradas = True

    # Validar si no hay pendientes
    if not encontradas:
        print("No hay tareas pendientes")

    # Volver al menú
    input("\nPresione Enter para volver al menú...")      

def main():

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion.isdigit():
            opcion = int(opcion)
        else:
            print("Debe ingresar un número válido del menú")
            continue

        match opcion:
            case 1:
                agregar_tarea()
                print("-" * 60)

            case 2:
                mostrar_tareas()
                input("\nPresione Enter para volver al menú...")
                print("-" * 60)

            case 3:
                buscar_tarea()
                print("-" * 60)

            case 4:
                contar_tareas()
                print("-" * 60)  

            case 5:
                eliminar_tarea()
                print("-" * 60)       

            case 6:
                marcar_completada()
                print("-" * 60)   

            case 7:
                mostrar_tareas_pendientes() 
                print("-" * 60)

            case 8:
                print("¡Hasta luego!")
                break

            case _:
                print("Opción inválida")

if __name__ == "__main__":
    main()