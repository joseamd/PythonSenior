"""
EJERCICIO 1
Pedir al usuario que ingrese notas entre 0 y 10,
hasta que ingrese -1 para finalizar.
Luego, mostrar el promedio de notas ingresadas.
"""
notas = []

menu = """
===========================
    PROMEDIO DE NOTAS
===========================
 1. Ingresar notas
 2. Calcular Promedio
-1. Salir
===========================
"""

while True:
    print(menu)
    opcion = int(input("Ingrese una opción del menú: "))

    if opcion == -1:
        print("¡Hasta luego!")
        break

    elif opcion == 1:
        print("\n-- Ingreso de notas (escriba -1 para terminar) --")
        while True:
            n = float(input("Ingrese la nota:"))

            if n == -1:
                break
            elif 0 <= n <= 10:
                notas.append(n)
                print(f"Nota {n} agregada. Total de notas ingresadas: {len(notas)}")
            else:
                print("Nota inválida. Debe estar entre 0 y 10")

    elif opcion == 2:        
        if not notas:
            print("No hay notas ingresadas. Use la opción 1 primero")
        else:
            promedio = sum(notas) / len(notas)
            print(f"El promedio total es: {promedio:.2f}")
    
    else:
        print("Opción Inválida. Por favor elija 1, 2 o -1")