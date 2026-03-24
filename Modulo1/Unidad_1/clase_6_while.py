menu = "Restaurante el buen sabor \n" \
"1. Hamburguesa     - $20.000 \n" \
"2. Pizza           - $15.000 \n" \
"3. Ensalada        - $ 4.500 \n" \
"4. Salchipapa      - $ 8.000 \n" \
"5. Perro Caliente  - $12.000 \n" \
"6. Salir"

print(menu)
opcion = 0
cantidad_hamburguesa = 0
cantidad_pizza = 0
cantidad_ensalada = 0
cantidad_salchipapa = 0
cantidad_perro = 0
total_hamburguesa = 0
total_pizza = 0
total_ensalada = 0
total_salchipapa = 0
total_perro = 0
total_cuenta = 0

while opcion != 6:

    opcion = int(input("Ingrese una opción del menú: "))

    if opcion == 1:
        print("Has elegido Hamburguesa")        
        cantidad_hamburguesa += 1
        total_hamburguesa +=20000
        total_cuenta += 20000 

    elif opcion == 2:
        print("Has elegido Pizza")
        cantidad_pizza += 1
        total_pizza += 15000
        total_cuenta += 15000 

    elif opcion == 3:
        print("Has elegido Ensalada")
        cantidad_ensalada += 1
        total_ensalada += 4500
        total_cuenta += 4500 

    elif opcion == 4:
        print("Has elegido Salchipapa")
        cantidad_salchipapa += 1
        total_salchipapa += 8000
        total_cuenta += 8000 

    elif opcion == 5:
        print("Has elegido Perro Caliente")
        cantidad_perro += 1
        total_perro += 12000
        total_cuenta += 12000 

    elif opcion == 6:
        print(f"Gracias por visitar el Restaurante el Buen Sabor.\n"
              f"Total Hamburguesas:         cant {cantidad_hamburguesa:>3}      ${total_hamburguesa:>2,}\n"
              f"Total Pizzas:               cant {cantidad_pizza:>3}      ${total_pizza:>2,}\n"
              f"Total Ensaladas:            cant {cantidad_ensalada:>3}      ${total_ensalada:>2,}\n"
              f"Total Salchipapas:          cant {cantidad_salchipapa:>3}      ${total_salchipapa:>2,}\n"
              f"Total Perros Caliente:      cant {cantidad_perro:>3}      ${total_perro:>2,}\n"
              f"El total de la cuenta es:                 ${total_cuenta:>2,}\n"
              f"¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")        

    print(menu)

    
