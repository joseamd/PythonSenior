"""
Desarrollar un programa en Python que permita gestionar clientes y sus mascotas utilizando diccionarios anidados, 
simulando un sistema básico de una veterinaria

Estructura de datos

Debes usar un diccionario con la siguiente estructura:
veterinaria = {
    "cliente1": {
        "telefono": "123456789",
        "mascotas": {
            "Firulais": {
                "especie": "perro",
                "edad": 5,
                "peso": 12.5
            },
            "Misu": {
                "especie": "gato",
                "edad": 3,
                "peso": 4.2
            }
        }
    }
}

1️⃣ Agregar un cliente
Solicitar:
Nombre del cliente
Teléfono
Crear el cliente con un diccionario vacío de mascotas
2️⃣ Agregar una mascota a un cliente
Solicitar:
Nombre del cliente
Nombre de la mascota
Especie
Edad
Peso
Guardar la mascota dentro del cliente
3️⃣ Mostrar todos los clientes y sus mascotas

Debe mostrar algo como:

Cliente: Carlos
 Teléfono: 123456
 Mascotas:
   - Firulais | Perro | 5 años | 12.5 kg
4️⃣ Buscar una mascota
Solicitar el nombre del cliente y la mascota
Mostrar toda la información de la mascota
5️⃣ Calcular el peso promedio de las mascotas de un cliente
Recorrer el diccionario anidado
Calcular el promedio del peso de todas las mascotas del cliente
6️⃣ Encontrar la mascota más pesada de toda la veterinaria
Debes recorrer todos los clientes y todas sus mascotas
7️⃣ Eliminar una mascota
Solicitar cliente y nombre de la mascota
Eliminarla del diccionario
8️⃣ Eliminar un cliente
Eliminar completamente su registro
🧩 Bonus (opcional 🔥)
Mostrar cuántas mascotas tiene cada cliente
Validar que no se repitan nombres de mascotas dentro del mismo cliente
Mostrar el cliente con más mascotas
"""

menu = """
        ========================================
        SISTEMA DE GESTIÓN VETERINARIA
        ========================================
        1. Agregar Cliente
        2. Agregar Mascota
        3. Mostrar Clientes y Mascotas
        4. Buscar Mascota
        5. Calcular el peso promedio de las mascotas de un cliente
        6. Encontrar la Mascota más pesada
        7. Cliente con más Mascotas
        8. Eliminar una Mascota
        9. Eliminar un Cliente
        10. Salir
        ========================================
        """
veterinaria = {}

while True:
    print(menu)
    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            print("== Registro de Clientes ==\n")            
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            telefono = input("Ingrese el número de teléfono: ")

            if nombre_cliente in veterinaria:
                print(f"{nombre_cliente} ya exite")
            else:
                veterinaria[nombre_cliente]={
                    "telefono" : telefono,
                    "mascotas" : {}
                }
                print(f"El cliente {nombre_cliente} agregado exitosamente.")

        case 2:
            print("== Registro de Mascotas (escriba -1 para volver)==\n") 
            nombre_cliente = input("Ingrese el nombre del cliente: ")

            if nombre_cliente in veterinaria:
                while True:
                    nombre_mascota = input("Ingrese el nombre de la mascota: ")
                    if nombre_mascota == "-1":
                        break
                    elif nombre_mascota in veterinaria[nombre_cliente]["mascotas"]:
                        print("La mascota ya existe")
                    else:
                        especie = input("Ingrese la especie: ")
                        edad = int(input("Ingrese la edad: "))
                        peso = float(input("Ingrese el peso: "))

                        veterinaria[nombre_cliente]["mascotas"][nombre_mascota]={
                            "especie": especie,
                            "edad": edad,
                            "peso": peso
                        }
            else:
                print("El cliente no existe, debes crearlo en la opción 1 del menú")

        case 3:
            print("== Lista de Clientes - Mascotas ==\n")
            if not veterinaria:
                print("No existen clientes")
            else:
                for nombre_cliente in veterinaria:
                    telefono = veterinaria[nombre_cliente]["telefono"]  
                    mascotas = veterinaria[nombre_cliente]["mascotas"]                  
                    print(f"Cliente: {nombre_cliente}")
                    print(f"Teléfono: {telefono}")
                    print("Mascotas:")
                    for nombre_mascota in mascotas:
                        especie = mascotas[nombre_mascota]["especie"]
                        edad = mascotas[nombre_mascota]["edad"]
                        peso = mascotas[nombre_mascota]["peso"]
                        print(f" - {nombre_mascota} | {especie} | {edad} años | {peso} Kg")
                    print(f"Total de mascotas: {len(mascotas)}")

        case 4:
            print("== Buscar una Mascota ==\n")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            if nombre_cliente in veterinaria:
                nombre_mascota = input("Ingrese el nombre de la mascota: ")

                if nombre_mascota in veterinaria[nombre_cliente]["mascotas"]:
                    mascota = veterinaria[nombre_cliente]["mascotas"][nombre_mascota]

                    especie = mascota["especie"]
                    edad = mascota["edad"]
                    peso = mascota["peso"]

                    print(f" - {nombre_mascota} | {especie} | {edad} años | {peso} Kg")
                else:
                    print("La mascota NO existe.")
            else:
                print("El cliente NO existe.")
            
        case 5:
            print("== Calcular Peso Promedio de las Mascotas ==\n")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            if nombre_cliente in veterinaria:
                mascotas = veterinaria[nombre_cliente]["mascotas"]
                pesos = []
                for nombre_mascota in mascotas:
                    pesos.append(mascotas[nombre_mascota]["peso"])
                if len(pesos) == 0:
                    print("No existen Mascotas.")
                else:
                    promedio = sum(pesos) / len(pesos)
                    print(f"El peso promedio de las mascotas de {nombre_cliente} es: {promedio:.2f} Kg")                
            else:
                print("El cliente NO existe.")

        case 6:
            print("== Mascota más Pesada ==\n")
            mascota_pesada = None
            mayor_peso = -1

            for nombre_cliente in veterinaria:
                mascotas = veterinaria[nombre_cliente]["mascotas"]
                for nombre_mascota in mascotas:
                    peso = mascotas[nombre_mascota]["peso"]
                    if peso > mayor_peso:
                        mayor_peso = peso
                        mascota_pesada = nombre_mascota                
            if mascota_pesada is None:
                print("No hay mascotas registradas.")
            else:
                print(f"La mascota más pesada es {mascota_pesada} con un peso de {mayor_peso} Kg")

        case 7:  
            print("== Cliente con más Mascotas ==\n")
            cliente_max = None
            max_mascotas = -1

            for nombre_cliente in veterinaria:
                mascotas = veterinaria[nombre_cliente]["mascotas"]
                if len(mascotas) > max_mascotas:
                    max_mascotas = len(mascotas)
                    cliente_max = nombre_cliente
            if cliente_max is None:
                print("No existen clientes.")
            else:
                print(f"El cliente que tiene el mayor número de mascotas es {cliente_max} con un total de {max_mascotas}")

        case 8:
            print("== Eliminar Mascota ==\n")
            nombre_cliente = input("Ingrese el nombre del Cliente: ")
            if nombre_cliente in veterinaria:
                nombre_mascota = input("Ingrese el nombre de la Mascota: ")
                if nombre_mascota in veterinaria[nombre_cliente]["mascotas"]:
                    veterinaria[nombre_cliente]["mascotas"].pop(nombre_mascota)
                    print(f"La Mascota {nombre_mascota} fue eliminada exitosamente.")
                else:
                    print("La mascota No existe.")

            else:
                print("El cliente NO existe.")

        case 9:
            print("== Eliminar Cliente ==")
            nombre_cliente = input("Ingrese el nombre del Cliente: ")

            if nombre_cliente in veterinaria:
                veterinaria.pop(nombre_cliente)
                print(f"El cliente {nombre_cliente} fue eliminado exitosamente." )
            else:
                print("El cliente NO existe.")

        case 10:
            print("¡Hasta luego!")
            break
        case _:
            print("Opción inválida")
