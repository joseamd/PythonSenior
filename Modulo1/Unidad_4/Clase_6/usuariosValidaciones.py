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
            6. Salir
            ========================================
            """
        print(menu)

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
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados.")
                return
            
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) == 3:
                    nombre, edad, fecha = partes
                    print(f"Nombre: {nombre}, Edad: {edad}, Fecha: {fecha}")    
                else:
                    print(f"Línea con formato incorrecto: {linea.strip()}")     
            
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
    except PermissionError:
        print("No tienes permisos para leer el archivo.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

def buscar_usuario():
    busqueda = input("Ingrese el nombre del usuario a buscar: ").strip().lower()

    if not busqueda:
        print("Debe ingresar un nombre para buscar.")
        return

    encontrados = []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            if not lineas:
                print("No hay usuarios registrados.")
                return            
            
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) == 3:
                    nombre_archivo, edad, fecha = partes
                    if nombre_archivo.lower() == busqueda:
                        encontrados.append({"nombre": nombre_archivo, "edad": edad, "fecha": fecha})   
            
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
    except PermissionError:
        print("No tienes permisos para leer el archivo.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")    
    
    if encontrados:
        print("\n-- Usuarios Encontrados --")
        for i, usuario in enumerate(encontrados, start=1):
            print(f"{i}. Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Fecha: {usuario['fecha']}")
    else:
        print("No se encontraron usuarios con ese nombre.")

def validar_archivo():
    print("== Validación de Archivos ==\n")

    errores = 0
    usuarios = []
    invalidos = []

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
        usuario_valido = True

        if len(partes) != 3:
            print(f"Línea {i}: formato incorrecto: {linea.strip()}")
            errores += 1
            invalidos.append(linea.strip())
            continue  

        nombre, edad, fecha = partes

        if not nombre.strip():
            print(f"Línea {i}: nombre vacío.")
            errores += 1
            usuario_valido = False

        try:
            edad_int = int(edad)
            if edad_int < 0 or edad_int > 120:
                print(f"Línea {i}: edad fuera de rango: {edad}")
                errores += 1
                usuario_valido = False
        except ValueError:
            print(f"Línea {i}: edad no es un número: {edad}")
            errores += 1
            usuario_valido = False

        if usuario_valido:
            usuarios.append(linea.strip())
        else:
            invalidos.append(linea.strip())

    # Resumen final
    if errores == 0:
        print("Todos los datos son válidos.")
    else:
        print(f"\nSe encontraron {errores} errores.")
    
    print(f"Usuarios válidos: {len(usuarios)}")
    print(f"Usuarios inválidos: {len(invalidos)}")

    return usuarios, invalidos

def procesar_archivos():
    print("== Procesador de Archivos ==\n")

    usuarios, invalidos = validar_archivo()    

    if not usuarios and not invalidos:
        print("No hay datos para procesar.")
        return
    
    try:
        if usuarios:
            with open(ARCHIVO_BUENOS, "w", encoding="utf-8") as archivo:
                for linea in usuarios:
                    archivo.write(linea + "\n")
            print(f"Archivo de válidos guardado: {len(usuarios)} usuarios.")

        if invalidos:
            with open(ARCHIVO_MALOS, "w", encoding="utf-8") as archivo:
                for linea in invalidos:
                    archivo.write(linea + "\n")
            print(f"Archivo de inválidos guardado: {len(invalidos)} registros.")
    except PermissionError:
        print("No tienes permisos para escribir los archivos.")
    except OSError as error:
        print(f"Error al guardar los archivos: {error}")    
    

def main():    

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

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
                print("¡Hasta luego!")
                break

            case _:
                print("Opción inválida")

if __name__ == "__main__":
    main()