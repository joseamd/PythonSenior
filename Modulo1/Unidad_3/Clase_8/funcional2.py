numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
#print(numeros_pares)

edades = [15, 22, 30, 17, 25, 19]
mayores_de_edad = list(filter(lambda x: x >= 18, edades))
print(mayores_de_edad)