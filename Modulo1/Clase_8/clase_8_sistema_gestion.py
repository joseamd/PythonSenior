
menu = "===== SISTEMA DE ESTUDIANTES =====\n" \
"1. Registrar estudiante \n" \
"2. Mostrar todos los estudiantes\n" \
"3. Salir"

opcion = 0
estudiantes = []
promedio = 0
estado = ""

while opcion != 3:
    print(menu)
    opcion = int(input("Seleccione una opción: \n"))
    
    match opcion:
        case 1:
            print("--- Registro de estudiante ---") 
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))

            while edad <= 0:            
                print("La edad debe ser mayor que 0")
                edad = int(input("Ingrese la edad nuevamente: "))

            nota1 = float(input("Ingrese la nota 1(0.0 a 5.0): "))
            while nota1 < 0 or nota1 > 5:            
                print("Notas no válidas")
                nota1 = float(input("Ingrese la nota 1 nuevamente(0.0 a 5.0): "))

            nota2 = float(input("Ingrese la nota 2(0.0 a 5.0): "))
            while nota2 < 0 or nota2 > 5:            
                print("Notas no válidas")
                nota2 = float(input("Ingrese la nota 2 nuevamente(0.0 a 5.0): "))

            nota3 = float(input("Ingrese la nota 3(0.0 a 5.0): "))
            while nota3 < 0 or nota3 > 5:            
                print("Notas no válidas")
                nota3 = float(input("Ingrese la nota 3 nuevamente(0.0 a 5.0): "))

            promedio = (nota1 + nota2 + nota3) / 3
            if promedio >= 4.0:
                estado = "Aprobado"
            elif promedio >=3.0 and promedio < 4.0:
                estado = "En recuperación"
            else:
                estado = "Reprobado"

            print(f"===== RESULTADO DEL ESTUDIANTE =====\n" \
            f"Nombre: {nombre}\n" \
            f"Edad: {edad}\n" \
            f"Nota 1: {nota1}\n" \
            f"Nota 2: {nota2}\n" \
            f"Nota 3: {nota3}\n" \
            f"Promedio: {promedio:.2f}\n" \
            f"Estado académico: {estado}\n")
            
            estudiante = {
                "nombre" : nombre,
                "edad" : edad,
                "nota1" : nota1,
                "nota2" : nota2,
                "nota3" : nota3,
                "promedio" : promedio,
                "estado" : estado
            }

            estudiantes.append(estudiante)
        
        case 2:
            contador = 1
            for est in estudiantes:
                print(f"{contador}. {est['nombre']} - Edad: {est['edad']} - Estado: {est['estado']}")
                contador += 1
            print()

total_estudiantes = len(estudiantes)
suma_promedio = 0
promedio_general = 0

for prom in estudiantes:
    suma_promedio += prom['promedio']

promedio_general = suma_promedio / total_estudiantes


print(f"===== RESUMEN FINAL =====\n"
      f"Total de estudiantes registrados: {total_estudiantes}\n"
      f"Promedio general por grupo: {promedio_general:.2}\n"
      f"Programa finalizado")