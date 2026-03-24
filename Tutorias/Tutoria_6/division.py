#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num2 == 0:
    print("Error, no se puede dividir por 0")
else:
    division = num1 / num2
    print(f"El resultado de la división es: {division}")