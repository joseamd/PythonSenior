"""
Crear una aplicación que permita:

Registrar usuarios.
Validar información.
Guardar en archivo.
Capturar errores.
Mostrar mensajes amigables.

Deben utilizar validaciones

El formato del archivo es:
Nombre, Edad                                                             
Carlos,25
Ana,30
Pedro,22
CSV

Modificar el programa para:

Buscar usuarios.
Evitar usuarios duplicados.
Validar un archivo al momento de leerlo y en caso de errores mortralos
Crear archivo de errores. Meter los datos buenos en un archivo y los malos en otro
Registrar fecha y hora de creación. Modificar la opcion 1 para registrar la fecha en que se crea
"""

from datetime import datetime

# Archivos de datos
ARCHIVO = "usuarios.txt"
ARCHIVO_BUENOS = "usuarios_validos.txt"
ARCHIVO_MALOS = "usuarios_invalidos.txt"

def mostrar_menu():
        menu = """
            ========================================
                    SISTEMA DE USUARIOS
            ========================================
            1. Registrar usuario
            2. Mostrar usuarios
            3. Buscar usuario
            4. Validar archivo
            5. Procesar archivo con errores
            6. Eliminar usuario
            7. Edad promedio 
            8. Ordenar Usuarios         
            9. Salir
            ========================================
            """
        print(menu)

def leer_archivo():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados.")
                return []
            return lineas
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
        return []
    except PermissionError:
        print("No tienes permisos para leer el archivo.")
        return []
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
        return []

def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ").strip().lower()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return   
    
    try:
        edad = int(input("Ingrese la edad: "))
    except ValueError:
        print("Edad debe ser números. Usuario no registrado.")
        return

    if edad < 0 or edad > 120:
        print("La edad debe estar entre 0 y 120 años.")
        return
    
    # Verificar que no exista un usuario con el mismo nombre
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) >= 2 and partes[0].lower() == nombre:
                    print("Ya existe un usuario con ese nombre.")
                    return
    except FileNotFoundError:
        pass
    
    # Guardar el usuario con fecha y hora de registro
    try:
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")    
            print("Usuario registrado correctamente.")    
    except PermissionError:
        print("No tienes permisos para escribir en el archivo.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

def mostrar_usuarios():
    print("== Lista de Usuarios ==\n")

    # leer archivo
    lineas = leer_archivo()
    if not lineas:
        return
    
    total_usuarios = 0
    for linea in lineas:
        partes = linea.strip().split(",")
        # Verificar que la línea tenga el formato correcto
        if len(partes) == 3:
            nombre, edad, fecha = partes
            print(f"Nombre: {nombre}, Edad: {edad}, Fecha: {fecha}")    
            total_usuarios += 1
        else:
            print(f"\nLínea con formato incorrecto: {linea.strip()}")    

    print(f"\nTotal de usuarios correctamente registrados: {total_usuarios}")     

def buscar_usuario():
    busqueda = input("Ingrese el nombre del usuario a buscar: ").strip().lower()

    if not busqueda:
        print("Debe ingresar un nombre para buscar.")
        return

    encontrados = []

    # leer archivo
    lineas = leer_archivo()
    if not lineas:
        return
    
    # Buscar coincidencias ignorando mayúsculas y minúsculas
    for linea in lineas:
        partes = linea.strip().split(",")
        if len(partes) == 3:
            nombre_archivo, edad, fecha = partes
            if nombre_archivo.lower() == busqueda:
                encontrados.append({"nombre": nombre_archivo, "edad": edad, "fecha": fecha})  
    
    if encontrados:
        print("\n-- Usuarios Encontrados --")
        for i, usuario in enumerate(encontrados, start=1):
            print(f"{i}. Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Fecha: {usuario['fecha']}")
    else:
        print("No se encontraron usuarios con ese nombre.")

def validar_archivo():
    print("== Validación de Archivos ==\n")

    errores = 0
    usuarios = []   # lineas válidas
    invalidos = []  # líneas con errores y su motivo

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados.")
                return [], []       
            
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
        return [], []
    except PermissionError:
        print("No tienes permisos para leer el archivo.")
        return [], []
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
        return [], []

    for i, linea in enumerate(lineas, start=1):
        partes = linea.strip().split(",")
        usuario_valido = True   # se asume válido hasta encontrar un error

        # Validar que tenga exactamente 3 campos
        if len(partes) != 3:
            print(f"Línea {i}: formato incorrecto: {linea.strip()}")
            errores += 1
            invalidos.append(f"{linea.strip()} → formato incorrecto")
            continue

        # Desempaquetar los campos
        nombre, edad, fecha = partes

        # Validar nombre no vacío
        if not nombre.strip():
            print(f"Línea {i}: nombre vacío.")
            errores += 1
            invalidos.append(f"{linea.strip()} → nombre vacío")
            usuario_valido = False

        # Validar que edad sea numérica y esté en rango 
        try:
            edad_int = int(edad)
            if edad_int < 0 or edad_int > 120:
                print(f"Línea {i}: edad fuera de rango →  {edad}")
                errores += 1
                invalidos.append(f"{linea.strip()} → edad fuera de rango")
                usuario_valido = False
        except ValueError:
            print(f"Línea {i}: edad no es un número → {edad}")
            errores += 1
            invalidos.append(f"{linea.strip()} → edad no es un número")
            usuario_valido = False

        # Si pasó todas las validaciones, se agrega a la lista de válidos llamada usuarios
        if usuario_valido:
            usuarios.append(linea.strip())

    # Resumen final
    if errores == 0:
        print("Todos los datos son válidos.")
    else:
        print(f"\nSe encontraron {errores} errores.")
    
    print(f"Usuarios válidos: {len(usuarios)}")
    print(f"Usuarios inválidos: {len(invalidos)} \n")

    return usuarios, invalidos

def procesar_archivos():
    print("== Procesador de Archivos ==\n")

    # Reutilizar la lógica de validación
    usuarios, invalidos = validar_archivo()    

    if not usuarios and not invalidos:
        print("No hay datos para procesar.")
        return
    
    try:
        # Guardar registros válidos
        if usuarios:
            with open(ARCHIVO_BUENOS, "w", encoding="utf-8") as archivo:
                for linea in usuarios:
                    archivo.write(linea + "\n")
            print(f"Archivo de válidos guardado correctamente con: {len(usuarios)} usuarios.")

        # Guardar registros inválidos con el motivo del error
        if invalidos:
            with open(ARCHIVO_MALOS, "w", encoding="utf-8") as archivo:
                for linea in invalidos:
                    archivo.write(linea + "\n")
            print(f"Archivo de inválidos guardado correctamente con: {len(invalidos)} registros.")
    except PermissionError:
        print("No tienes permisos para escribir los archivos.")
    except OSError as error:
        print(f"Error al guardar los archivos: {error}")   

def eliminar_usuario():
    busqueda = input("Ingrese el nombre del usuario a eliminar: ").strip().lower()

    if not busqueda:
        print("Debe ingresar un nombre para eliminar.")
        return
    
    # Filtrar todas las líneas excepto la del usuario a eliminar
    nuevas_lineas = []
    eliminado = False 

    # leer archivo
    lineas = leer_archivo()
    if not lineas:
        return
    
    for linea in lineas:
        partes = linea.strip().split(",")
        if len(partes) == 3 and partes[0].lower() == busqueda:
            eliminado = True  # encontramos al usuario
        else:
            nuevas_lineas.append(linea)  # conservamos las demás    

    if eliminado:
        try:
            with open(ARCHIVO, "w", encoding="utf-8") as archivo:
                archivo.writelines(nuevas_lineas)
            print(f"Usuario '{busqueda}' eliminado correctamente.")
        except PermissionError:
            print("No tienes permisos para modificar el archivo.")
        except OSError as error:
            print(f"Error al guardar los cambios: {error}")
    else:
        print("No se encontró un usuario con ese nombre.")

def calcular_edad_promedio():
    print("== Edad promedio de Usuarios ==\n")

    # leer archivo
    lineas = leer_archivo()
    if not lineas:
        return
    
    suma_edades = 0
    total_usuarios = 0
    for linea in lineas:
        partes = linea.strip().split(",")
        # Solo procesar líneas con formato correcto
        if len(partes) == 3:
            nombre, edad, fecha = partes
            try:
                suma_edades += int(edad)    # convertir a entero para sumar
                total_usuarios += 1
            except ValueError:
                print(f"Línea con edad inválida ignorada: {linea.strip()}")             
        else:
            print(f"\nLínea con formato incorrecto: {linea.strip()}")    

    # Evitar división por cero si no hay usuarios válidos
    if total_usuarios == 0:
        print("No hay usuarios válidos para calcular el promedio.")
        return
    
    promedio = suma_edades / total_usuarios
    print(f"\nEl promedio de edad de los usuarios registrados es: {promedio:.1f} años")  

def ordenar_usuarios():
    # leer archivo
    lineas = leer_archivo()
    if not lineas:
        return
    
    # mostrar submenú y ordenar
    print("\n== Ordenar Usuarios ==")
    print("1. Nombre")
    print("2. Edad")
    opcion = input("¿Ordenar por: ")

    match opcion:
        case "1":
            lineas_ordenadas = sorted(lineas, key=lambda l: l.split(",")[0])
            print("-" * 60)

        case "2":
            try:
                lineas_ordenadas = sorted(lineas, key=lambda l: int(l.split(",")[1]))
            except ValueError:
                print("No se puede ordenar por edad: hay líneas con edad inválida.")
                return
            print("-" * 60)
            
        case _:
            print("Opción inválida")
            return

    # imprimir resultado
    print("\n-- Usuarios Ordenados --")
    for linea in lineas_ordenadas:
        partes = linea.strip().split(",")
        if len(partes) == 3:
            nombre, edad, fecha = partes
            print(f"Nombre: {nombre}, Edad: {edad}, Fecha: {fecha}")
        else:
            print(f"Línea con formato incorrecto: {linea.strip()}")       

def main():    

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        # Validar que la opción sea un número
        try:
            opcion = int(opcion)
        except ValueError:
            print("Debe ingresar un número válido del menú")
            continue

        match opcion:
            case 1:
                registrar_usuario()
                print("-" * 60)

            case 2:
                mostrar_usuarios()
                print("-" * 60)

            case 3:
                buscar_usuario()
                print("-" * 60)      

            case 4:
                validar_archivo()
                print("-" * 60)    

            case 5:
                procesar_archivos()
                print("-" * 60)    

            case 6:
                eliminar_usuario()
                print("-" * 60)    

            case 7:
                calcular_edad_promedio()
                print("-" * 60) 

            case 8:
                ordenar_usuarios()
                print("-" * 60) 

            case 9:
                print("¡Hasta luego!")
                break

            case _:
                print("Opción inválida")

if __name__ == "__main__":
    main()