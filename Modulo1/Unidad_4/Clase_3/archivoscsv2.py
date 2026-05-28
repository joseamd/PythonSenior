import csv

with open("estudiantes.csv", "w", encoding="utf-8", newline='') as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(["nombre", "nota"])
    escritor.writerow(["Juan", 8])
    escritor.writerow(["Alex", 9])