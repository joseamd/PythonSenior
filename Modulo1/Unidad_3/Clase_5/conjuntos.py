"""
Conjuntos y estructuras mixtas

- Imprime en desorden
- No permite datos duplicados, los elimina
"""

frutas = {"Manzana", "Banana", "Naranja", "Pera", "Uva", "Pera"}
print(frutas)
print(len(frutas))
frutas.add("Kiwi")
print(frutas)
frutas.remove("Uva")
print(frutas)
frutas.pop()
print(frutas)
# frutas.clear()
# print(frutas)
frutas2 = frutas.copy()
print(frutas2)

frutas1 = {"Manzana", "Banana", "Naranja", "Pera", "Uva", "Banana"}
frutas2 = {"Kiwi", "Fresa", "Melón", "Pera", "Uva"}
print(frutas1.difference(frutas2))
print(frutas1.intersection(frutas2))
print(frutas1.union(frutas2))
frutas1.discard("Uva")
print(frutas1)