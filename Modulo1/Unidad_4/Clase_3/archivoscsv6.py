import csv

with open("usuarios.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = ["nombre", "edad"]

    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()

    escritor.writerow({
        "nombre": "Carlos",
        "edad" : 30
    })
    escritor.writerow({
        "nombre": "Alex",
        "edad" : 41
    })
