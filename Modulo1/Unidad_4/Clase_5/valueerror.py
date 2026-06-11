# ValueError

try:
    numero = int(input("Ingrese un número: "))
    print(numero)
except ValueError:
    print("Error: Dato incorrecto")