import csv

datos = [
    ["portatil", 2500000],
    ["Table", 1500000],
    ["Smartphone", 1000000]
]

with open("inventario.csv", "w", encoding="utf-8", newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Producto", "Precio"])
    for fila in datos:
        escritor.writerow(fila)