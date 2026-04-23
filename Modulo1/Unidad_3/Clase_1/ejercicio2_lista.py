"""
Ejercicio 2 — Gestión de lista de compras
Crea un programa con menú que permita:

Agregar producto — el usuario escribe el nombre y se agrega a la lista
Eliminar producto — el usuario escribe el nombre y si existe se elimina, si no, avisa que no está
Ver lista — muestra todos los productos numerados; si está vacía avisa
Salir
"""

productos = []
opcion = 0

menu = "=== LISTA DE COMPRAS === \n" \
" 1. Agregar producto \n" \
" 2. Eliminar producto \n" \
" 3. Ver lista \n" \
"-1. Salir \n" \
"========================" \

while True:
    print(menu)
    opcion = int(input("Ingrese una opción:"))

    if opcion == -1:
        print("¡Hasta luego!")
        break

    elif opcion == 1:
        print("-- Ingreso de productos (escriba -1 para volver) --")
        while True:           
            producto = input("Ingrese el producto:")
            if producto == "-1":
                break
            productos.append(producto)
            print(f"'{producto}' agregado correctamente.")
        print("------------------------")
    
    elif opcion == 2:
        eliminar = input("Ingrese el nombre del producto a eliminar:")
        if eliminar in productos:
            productos.remove(eliminar)
            print(f"{eliminar} eliminado ")
        else:
            print(f"El producto: {eliminar}, no existe o es inválido")
        print("------------------------")

    elif opcion == 3:
        if not productos:
            print(f"No hay productos, por favor selecciona la opción 1")        
        else:
            print("--- Lista de compras ---")
            for i, producto in enumerate(productos, start=1):
                print(f"{i}. {producto}")
            print("------------------------")
    else:
        print("Opción Inválida. Por favor elija 1, 2, 3 o -1")