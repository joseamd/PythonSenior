import csv

with open("malo.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        nombre = fila.get("nombre")
        precio_str = fila.get("precio")
        cantidad_str = fila.get("cantidad")

        if nombre is None or precio_str is None or cantidad_str is None:
            print("Falta una columna en la fila:", fila)
            continue

        try:
            precio = float(precio_str)
            cantidad = int(cantidad_str)
        except (ValueError, TypeError):
            print("Error de formato en la fila:", fila)
            continue

        if precio < 0 or cantidad < 0:
            print("valores negativos inválidos")
            continue

        print(nombre, precio, cantidad)