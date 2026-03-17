print("Calculadora Aritmética")
a = float(input("Ingresa un número: "))
b = float(input("ingrese otro número: "))

suma = a + b
print("El resultado total de la suma es:", suma)

if b == 0:
    print("El resultado total de la division es: No se puede dividir entre cero")
else:
    division = a / b
    print("El resultado total de la division es:", division)
    
potencia = a ** b
print("El resultado total de la potencia es:", potencia)