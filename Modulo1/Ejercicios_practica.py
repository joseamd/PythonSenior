
"""
Nivel 1 - Par o impar
Pide un número y di si es par o impar."""

# numero = int(input("Ingrese un número: "))

# if numero % 2 == 0:
#     print(f"El número {numero} es par")
# else:
#     print(f"El número {numero} es impar")

"""
Nivel 2 - Calificación
Pide una nota de 0 a 10 y muestra:
- 0 a 5: Reprobado
- 6 a 7: Regular
- 8 a 9: Bueno
- 10: Excelente"""

# nota = int(input("Ingrese una nota: "))
# calificacion = ""

# if nota < 0 or nota > 10:
#     print("Nota inválida, debe ingresar un valor entre 0 y 10")
# elif nota <=5:
#     calificacion = "Reprobado"
# elif nota <= 7:
#     calificacion = "Regular"
# elif nota <= 9:
#     calificacion = "Bueno"
# else:
#     calificacion = "Excelente"

# if calificacion:
#     print(f"La calificación es: {calificacion}")


"""Nivel 3 - Cajero automático
Pide el saldo disponible y el monto a retirar.
- Si el monto es mayor al saldo: Error, saldo insuficiente
- Si el monto es 0 o negativo: Error, monto inválido
- Si todo está bien: muestra el saldo restante"""

# saldo_disponible = 1000000
# monto_retiro = int(input("Digita el monto a retirar: "))

# if monto_retiro <= 0:
#     print("Error, monto inválido")
# elif monto_retiro > saldo_disponible:
#     print("Error, saldo insuficiente")
# else:
#     saldo_restante = saldo_disponible-monto_retiro
#     print(f"Monto Retirado: ${monto_retiro:,}")
#     print(f"Saldo restante: ${saldo_restante:,}")

"""Nivel 4 - Calculadora
Pide dos números y una operación (+, -, *, /).
Muestra el resultado según la operación elegida.
Controla la división entre cero."""

# num1 = int(input("Ingresa el primer número: "))
# num2 = int(input("Ingresa el segundo número: "))
# operacion = input("Ingrese el tipo de operación: ")

# resultado = None
# operacion_nombre = ""

# if operacion == "+":
#     resultado = num1 + num2
#     operacion_nombre = "suma"
# elif operacion == "-":
#     resultado = num1 - num2
#     operacion_nombre = "resta"
# elif operacion == "*":
#     resultado = num1 * num2
#     operacion_nombre = "multiplicación"
# elif operacion == "/":
#     if num2 == 0:
#         print("No se puede realizar la división entre 0")
#     else:
#         resultado = num1 / num2
#         operacion_nombre = "división"
# else:
#     print("Operación inválida")

# if resultado is not None:
#     print(f"El resultado de la {operacion_nombre} es: {resultado}")



"""Nivel 5 - Clasificador de triángulos
Pide los 3 lados de un triángulo.
- Si los 3 lados son iguales: Equilátero
- Si 2 lados son iguales: Isósceles
- Si ningún lado es igual: Escaleno
- Si no forman un triángulo: Error (un lado no puede 
  ser mayor a la suma de los otros dos)"""

# lado1 = int(input("Ingresa el lado 1 del triángulo: "))
# lado2 = int(input("Ingresa el lado 2 del triángulo: "))
# lado3 = int(input("Ingresa el lado 3 del triángulo: "))

# lados = []
# for i in range(1, 4):
#     lados.append(int(input(f"Ingresa el lado {i} del triángulo: ")))

# lado1, lado2, lado3 = lados

# if lado1 >= (lado2+lado3) and lado2 >= (lado1+lado3) and lado3 >= (lado2+lado1):
#     print("Error (un lado no puede ser mayor a la suma de los otros dos)")
# elif lado1 == lado2 and lado2 == lado3:
#     print("Equilátero")
# elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#     print("Isósceles")
# else:
#     print("Escaleno")


"""Nivel 6 - Tarifa de taxi
Una empresa de taxis cobra así:
- Tarifa base: $2000
- Por cada km: $800
- Si es de noche (10pm - 6am): recargo del 30%
- Si son más de 4 pasajeros: recargo de $1500
Pide los km, la hora y el número de pasajeros 
y muestra el valor total del viaje."""


tarifa_base = 2000
km = int(input("Ingresa los kilómetros: "))
hora = int(input("Ingresa la hora actual (0-23): "))
num_pasajeros = int(input("Ingresa el número de pasajeros: "))

tarifa_total = tarifa_base + (km * 800)

if hora >= 22 and hora < 6:
    tarifa_total += tarifa_total * 0.3
if num_pasajeros > 4:
    tarifa_total += 1500

print(f"El valor total del viaje es: ${tarifa_total}")