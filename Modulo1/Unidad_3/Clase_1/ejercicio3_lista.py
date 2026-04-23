"""
Ejercicio 3 — Registro de calificaciones por estudiante
Crea un programa con menú que permita:

Agregar estudiante — pide el nombre y lo agrega a la lista
Ver estudiantes — muestra la lista numerada; si está vacía avisa
Buscar estudiante — el usuario escribe un nombre y el programa dice si está registrado o no, y en qué posición
Salir
"""
estudiantes = []
opcion = 0

menu ="=== REGISTRO DE CALIFICACIONES ===\n" \
"1. Agregar estudiante \n" \
"2. Ver estudiantes \n" \
"3. Buscar estudiante \n" \
"4. Salir"

while True:
    print(menu)
    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            print("== REGISTRO DE ESTUDIANTES (escriba -1 para volver) ==\n")
            while True:
                estudiante = input("Ingrese el nombre del estudiante: ")
                if estudiante == "-1":
                    break
                estudiantes.append(estudiante)
                print(f"{estudiante} registrado.")
            print("-" * 60)

        case 2:
            print("== LISTAS DE ESTUDIANTES == \n")
            if not estudiantes:
                print(f"No hay estudiantes, por favor selecciona la opción 1") 
            else:
                for i, estudiante in enumerate(estudiantes, start=1):
                    print(f"{i}. {estudiante}")
            print("-" * 60)

        case 3:
            print("== BUSCAR ESTUDIANTE (escriba -1 para volver) ==\n")
            while True:
                estudiante = input("Ingrese el nombre del estudiante a buscar: ")
                if estudiante == "-1":
                    break
                elif estudiante in estudiantes:
                    posicion = estudiantes.index(estudiante) + 1
                    print(f"{estudiante} se encuentra en la posición {posicion}")
                else:
                    print(f"{estudiante} no existe.")
            print("-" * 60)
            
        case 4:
            print("¡Hasta luego!")
            break

        case _:
            print("Opción inválida")

