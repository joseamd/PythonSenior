"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en 
función de su respuesta le muestre un menú con los ingredientes 
disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y 
el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los 
ingredientes que lleva.
"""
tipoPizza = int(input("Selecciona el tipo de pizza: \n"
                    "1) Vegetariana \n"
                    "2) No vegetariana \n"))

if tipoPizza == 1:
    ingVegetarianos = int(input("Selecciona un ingrediente: \n"
                        "1)Pimiento \n"
                        "2)Tofu \n"))
    
    if ingVegetarianos == 1:
        ingrediente = "Pimiento"

    elif ingVegetarianos == 2:
        ingrediente = "Tofu"

    else:
        print("Opción no válida")

    print("La pizza seleccionada es Vegetariana")
    print(f"Los ingredientes son: \n"
            f"1){ingrediente} \n"
            f"2)mozzarella \n"
            f"3)tomate \n")

elif tipoPizza == 2:
    ingNoVegetarianos = int(input("Selecciona un ingrediente: \n"
                                  "1)Peperoni \n"
                                  "2)Jamón \n"
                                  "3)Salmón \n"))
    
    if ingNoVegetarianos == 1:
        ingrediente = "Peperoni"
        
    elif ingNoVegetarianos == 2:
        ingrediente = "Jamón"
    
    elif ingNoVegetarianos == 3:
        ingrediente = "Salmón"        
    
    else:
        print("Opción no válida")

    print("La pizza seleccionada es No Vegetariana")
    print(f"Los ingredientes son: \n"
            f"1){ingrediente} \n"
            f"2)mozzarella \n"
            f"3)tomate \n")

else:
    print("Opción no válida")