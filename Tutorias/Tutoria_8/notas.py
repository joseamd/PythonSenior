
suma_total = 0
cantidad_notas= 1
while True:
    nota = float(input("Ingrese nota: "))
    if nota == -1:
        break
    else:
        suma_total += nota
        cantidad_notas += 1

promedio = suma_total / cantidad_notas
print(f"El promedio de las notas es: {promedio}")