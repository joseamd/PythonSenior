"""
Ejercicio: Sistema de Gestión de Estudiantes
Crea un programa que gestione las calificaciones de estudiantes usando diccionarios. 
El programa debe permitir:

Requisitos:
Estructura de datos: Usa un diccionario donde las claves sean los nombres de los estudiantes 
y los valores sean listas de calificaciones.

Funcionalidades a implementar:
Agregar un nuevo estudiante (con una lista vacía de calificaciones)
Agregar calificaciones a un estudiante existente
Calcular el promedio de un estudiante
Mostrar todos los estudiantes con sus promedios
Encontrar el estudiante con el promedio más alto
Eliminar un estudiante
"""
class GestionEstudiante:
    def __init__(self):
        self.estudiantes = {}

    def mostrar_menu(self):
        menu = """
            ========================================
            SISTEMA DE GESTIÓN DE ESTUDIANTES
            ========================================
            1. Agregar estudiante
            2. Agregar calificaciones
            3. Calcular promedio de un estudiante
            4. Mostrar todos los estudiantes con sus promedios
            5. Encontrar el estudiante con el promedio más alto
            6. Eliminar un estudiante
            7. Salir
            ========================================
            """
        print(menu)

    def agregar_estudiante(self, codigo, nombre, apellido):
        if codigo in self.estudiantes:
            print("El código ya existe")
        else:
            self.estudiantes[codigo] = {
                "nombre" : nombre,
                "apellido" : apellido,
                "notas" : []
            }
            print(f"Estudiante {nombre} {apellido} agregado exitosamente.")

    def registro_notas(self, codigo):
        if codigo in self.estudiantes:
            while True:
                nota = input("Ingrese nota: ")
                if nota == "-1":
                    break
                else:
                    self.estudiantes[codigo]["notas"].append(float(nota))
        else:
            print("El estudiante no existe")                

    def calcular_promedio(self, codigo):
        notas = self.estudiantes[codigo]["notas"]
        if len(notas) == 0:
            return 0
        return sum(notas) / len(notas)

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        else:
            for codigo in self.estudiantes:
                nombre = self.estudiantes[codigo]["nombre"]
                apellido = self.estudiantes[codigo]["apellido"]
                promedio = self.calcular_promedio(codigo)
                print(f"Estudiante: {nombre} {apellido} - Promedio: {promedio:.2f}")

    def mostrar_mejor_estudiante(self):
        mejor_codigo = None
        mejor_promedio = -1

        for codigo in self.estudiantes:
            promedio = self.calcular_promedio(codigo)
            if promedio > mejor_promedio:                    
                mejor_codigo = codigo
                mejor_promedio = promedio

        if mejor_codigo is None:
            print("No hay estudiantes registrados.")
        else:
            nombre = self.estudiantes[mejor_codigo]["nombre"]
            apellido = self.estudiantes[mejor_codigo]["apellido"]
            print(f"El estudiante {nombre} {apellido} tiene el mejor promedio de: {mejor_promedio:.2f}")  
            
    def eliminar_estudiante(self, codigo):
        if codigo in self.estudiantes:
            nombre = self.estudiantes[codigo]["nombre"]
            apellido = self.estudiantes[codigo]["apellido"] 
            self.estudiantes.pop(codigo)
            print(f"Estudiante {nombre} {apellido} eliminado exitosamente.")
        else:
            print("El estudiante no existe")

def main():
    gestion = GestionEstudiante()

    while True:
        gestion.mostrar_menu()
        opcion = int(input("Ingrese una opción: "))

        match opcion:
            case 1:
                codigo = input("Ingrese código: ")
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese apellido: ")
            
                gestion.agregar_estudiante(codigo, nombre, apellido)
                print("-" * 60)
            
            case 2:
                print("== Registro de Notas (escriba -1 para volver) ==\n")
                codigo = input("Ingrese código de estudiante: ")
                
                gestion.registro_notas(codigo)
                print("-" * 60)                

            case 3:
                print("== Calcular Promedio ==\n")
                codigo = input("Ingrese código de estudiante: ")

                if codigo in gestion.estudiantes:
                    promedio = gestion.calcular_promedio(codigo)
                    nombre = gestion.estudiantes[codigo]["nombre"]
                    apellido = gestion.estudiantes[codigo]["apellido"]
                    print(f"El promedio del estudiante {nombre} {apellido} es: {promedio:.2f}")
                else:
                    print("El estudiante no existe")
                print("-" * 60)

            case 4:
                print("== Lista de Estudiantes ==\n")                
                gestion.mostrar_estudiantes()
                print("-" * 60)

            case 5:
                print("== Estudiante con puntaje más Alto ==\n")
                gestion.mostrar_mejor_estudiante()                          
                print("-" * 60)

            case 6:
                print("== Eliminar Estudiante ==\n")
                codigo = input("Ingrese código de estudiante: ")
                gestion.eliminar_estudiante(codigo)
                print("-" * 60)

            case 7:
                print("¡Hasta luego!")
                break

            case _:
                print("Opción inválida")
            
if __name__ == "__main__":
    main()