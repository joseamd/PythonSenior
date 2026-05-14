def suma(a, b):
    return a + b

suma2 = lambda n1, n2: n1 + n2

print("Aquí arranca el programa")
#print(suma(4, 5))
#print(suma2(4, 6))

a = 5
b = 10
#print(suma(a, b))
#print(suma2(a, b))

suma3 = lambda n1, n2, n3: n1 + n2 + n3
#print(suma3(5, 10, 15))

doble = lambda x: x * 2
#print(doble(5))

es_mayor = lambda edad: "Mayor de edad" if edad >= 18 else "menor de edad"
#print(es_mayor(18))

numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
#print(dobles)

nombres = ["Alex", "Carlos", "Luis"]
nombres_mayusculas = list(map(lambda x: x.upper(), nombres))
#print(nombres_mayusculas)

precios = [10, 20, 30, 40, 50]
precios_con_iva = list(map(lambda x: x * 1.19, precios))
print(precios_con_iva)