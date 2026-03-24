num = int(input("Ingrese un número: "))
invertido = 0

while num > 0:
    digito = num % 10
    invertido = (invertido * 10) + digito
    num = num //10

print(invertido)