"""
CICLO FOR
"""
# for x in range(1,11):
#     print(x)

# for x in range(5):
#     print(x)

# for x in range(1, 12, 2):  #Empieza desde el 1 hasta 11 de dos en dos
#     print(x)

# texto = "Python"
# for letra in texto:
#     print(letra)

# tabla = int(input("Ingrese el número de la tabla de multiplicar: "))

# print(f"TABLA DE MULTIPLICAR DEL NUMERO {tabla}")
# for x in range(1,11):
#     print(f"{tabla} x {x} = {tabla * x}")



print("LAS TABLAS DE MULTIPLICAR \n")
for x in range(1,11):
    print(f"TABLA DEL {x}")
    for y in range(1,11):
        print(f"{x} x {y} = {x * y}")
    print("\n")
