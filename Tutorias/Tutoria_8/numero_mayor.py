num_mayor = 0
while True:
    num = int(input("Ingrese números: "))
    if num == -1:
        break
    elif num > num_mayor:
        num_mayor = num
    else:
        num_mayor = num_mayor

print(f"El número mayor es: {num_mayor}")