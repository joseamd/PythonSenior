"""
FUNCIONES
"""

# def suma(a, b):
#     resultado = a + b
#     print(f"La suma de {a} y {b} es: {resultado}")

# (suma(4, 5))

# def suma2():
#     a = int(input("Ingrese el primer número: "))
#     b = int(input("Ingrese el segundo número: "))
#     resultado = a + b
#     return resultado

# print(suma2())

"""
CALCULADORA: 
Escribir un programa que pida al usuario dos números y muestre un menú de opciones, 
suma, resta, multiplicación y división
1. Suma
2. Resta
3. Multiplicación
4. División
5. División entera
6. Potencia
7. Módulo
8. Salir
"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error, no se puede dividir entre cero"
    return a / b

def division_entera(a, b):
    if b == 0:
        return "Error, no se puede dividir entre cero"
    return a // b

def potencia(a, b):
    resultado = a ** b
    return resultado

def modulo(a, b):
    resultado = a % b
    return resultado

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
opcion = 0

menu = "\n CALCULADORA \n" \
"1. Suma\n" \
"2. Resta\n" \
"3. Multiplicación\n" \
"4. División\n" \
"5. División entera\n" \
"6. Potencia\n" \
"7. Módulo\n" \
"8. Salir\n"
print(menu)

while opcion != 8:
    opcion = int(input("Seleccione la opción de operación: "))

    if opcion == 1:
        print(f"El resultado de la suma es: {suma(num1, num2)}")

    elif opcion == 2:
        print(f"El resultado de la resta es: {resta(num1, num2)}")
    
    elif opcion == 3:
        print(f"El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
    
    elif opcion == 4:
        print(f"El resultado de la división es: {division(num1, num2)}")
    
    elif opcion == 5:
        print(f"El resultado de la división entera es: {division_entera(num1, num2)}")
    
    elif opcion == 6:
        print(f"El resultado de la potencia es: {potencia(num1, num2)}")
    
    elif opcion == 7:
        print(f"El resultado del módulo es: {modulo(num1, num2)}")

    elif opcion == 8:
        break

    else:
        print("Opción no válida")
    
    print(menu)
    


