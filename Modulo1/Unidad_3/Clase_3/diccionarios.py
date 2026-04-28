carro = {
    "marca" : "Toyota",
    "modelo" : "Prado",
    "anio" : 2022
}

print(carro)
x = carro["modelo"]
#print(x)
y = carro["anio"]
#print(y)
#print(len(carro))
carro["color"] = "negro"
#print(carro)

carro.update({
    "puertas": 5,
    "automatico": True
})
#print(carro)

llaves = carro.keys()
#print(llaves)

valores = carro.values()
#print(valores)

items = carro.items()
# print(items)
# print(carro)

# Remover un Item: pop()
carro.pop("puertas")
#print(carro)

# Remover el ultimo elemento insertado: popitem()
carro.popitem()
#print(carro)

# for x in carro:
#     print(x)

# for x in carro:
#     print(carro[x])

# Imprime las llaves
# for x in carro.keys():
#     print(x)

# Imprime los valores asociados a las llaves
# for x in carro.values():
#     print(x)

# Copia de diccionarios
copia_carro = carro.copy()
#print(copia_carro)

estudiantes = {
    "estudiante1" : {
        "nombre" : "Alex",
        "apellido" : "Muñoz",
        "fecha_nac" : "1984-06-11"
    },
    "estudiante2" : {
        "nombre" : "Carlos",
        "apellido" : "Ortega",
        "fecha_nac" : "1990-07-11"
    }
}
# Accedo a un valor de una llave en específico
fecha_nacimiento = estudiantes["estudiante1"]["fecha_nac"]
print(fecha_nacimiento)
print(estudiantes["estudiante1"]["nombre"])
print(estudiantes.get("estudiante1", {}).get("nombre"))

est1 = estudiantes.get("estudiante1", {})
print(est1.get("nombre"), est1.get("apellido"))