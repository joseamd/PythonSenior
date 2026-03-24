
# n = int(input("Ingresa un número: "))
# m = int(input("ingrese otro número: "))

# cociente = n // m
# resto = n % m

# print("La", n, "entre", m, "da un cociente", cociente, "y un resto", resto)

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta 
# por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular 
# el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g 
# y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el 
# último pedido y calcule el peso total del paquete que será enviado.




# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre 
# por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra 
# con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en 
# mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre = input("Ingrese su nombre completo: ")
mayuscula = nombre.upper()
miniscula = nombre.lower()
letra_capital = nombre.title()

print(mayuscula)
print(miniscula)
print(letra_capital)

