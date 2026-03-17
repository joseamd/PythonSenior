def registrar_nota(numero):
    nota = float(input(f"Ingrese la nota {numero} (0.0 a 5.0): "))
    while nota < 0 or nota > 5:            
        print("Notas no válidas")
        nota = float(input(f"Ingrese la nota {numero} nuevamente(0.0 a 5.0): "))
    return nota

def calcular_promedio(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio

def calcular_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    elif promedio >=3.0 and promedio < 4.0:
        return "En recuperación"
    else:
        return "Reprobado"     

def registrar_estudiante():
    print("--- Registro de estudiante ---") 
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    while edad <= 0:            
        print("La edad debe ser mayor que 0")
        edad = int(input("Ingrese la edad nuevamente: "))
        
    nota1 = registrar_nota(1)
    nota2 = registrar_nota(2)
    nota3 = registrar_nota(3)
    promedio = calcular_promedio(nota1, nota2, nota3)
    estado =calcular_estado(promedio)

    print(f"===== RESULTADO DEL ESTUDIANTE =====\n" \
    f"Nombre: {nombre}\n" \
    f"Edad: {edad}\n" \
    f"Nota 1: {nota1}\n" \
    f"Nota 2: {nota2}\n" \
    f"Nota 3: {nota3}\n" \
    f"Promedio: {promedio:.2f}\n" \
    f"Estado académico: {estado}\n")
    
    return {
        "nombre" : nombre,
        "edad" : edad,
        "nota1" : nota1,
        "nota2" : nota2,
        "nota3" : nota3,
        "promedio" : promedio,
        "estado" : estado
    }

def mostrar_estudiantes(estudiantes):
    contador = 1
    for est in estudiantes:
        print(f"{contador}. {est['nombre']} - Edad: {est['edad']} - Estado: {est['estado']}")
        contador += 1
    print()

def resumen_final(estudiantes):
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
    

menu = "===== SISTEMA DE ESTUDIANTES =====\n" \
"1. Registrar estudiante \n" \
"2. Mostrar todos los estudiantes\n" \
"3. Salir"

opcion = 0
estudiantes = []
estado = ""

while opcion != 3:
    print(menu)
    opcion = int(input("Seleccione una opción: \n"))
    
    match opcion:
        case 1:
            estudiante = registrar_estudiante()         
            estudiantes.append(estudiante)
        
        case 2:
            mostrar_estudiantes(estudiantes)

resumen_final(estudiantes)