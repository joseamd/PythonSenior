frutas = ["papaya", "naranja", "pera", "pera", [6, 7, 8]]
#print(frutas)
# print(frutas[0])
# print(frutas[3])
# print(frutas[4][0])
# print(frutas[:2])
frutas.append("mandarina")
# print(frutas.count("pera"))
#frutas.extend(["platano", "banano"]) # Añade los elementos de esta lista a la lista frutas
verduras = ["platano", "banano", "piña"]
#frutas.append(verduras) # Añade todo el grupo de la lista dentro de la lista como un solo objeto
#frutas.extend(verduras)
# print(frutas)
# print(frutas.index("pera")) # me muestra la posición del primer objeto encontrado en la lista con ese nombre
frutas.insert(4, "coco") # inserta un dato en la posición indicada
# print(frutas)
# print(frutas.pop()) # saca un elemento, en este caso el último
# print(frutas.pop(1)) # saca el elemento de la posición dada de la lista
# print(frutas)

frutas.remove("pera")
#print(frutas)

frutas.reverse()
#print(frutas)

#frutas.sort() # Se usa si los elementos son del mismo tipo
#print(frutas)


a = ["fresa", "manzana", "pera", "naranja", "sandía", "manzana", "kiwi", "manzana"]
# b = list(("fresa", "manzana", "pera", "naranja", "sandía"))

# print(a)
# print(type(a))
# print(b)
# print(type(b))

# # 1 forma
# total = 0
# for elemento in a:
#     total += len(elemento)
# print(total)

# # 2 forma
# total_carateres = sum(len(elemento) for elemento in a )
# print(total_carateres)

# i = 0
# while i < len(a):
#     if a[i] == "manzana":
#         print(f"Manzana encontrada en la posición {i}")
#     i += 1




