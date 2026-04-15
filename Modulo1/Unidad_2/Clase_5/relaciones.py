# Relación de asociación
"""
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente

c1 = Cliente("Alex")
p1 = Pedido(c1)
"""

# Relación de agregación (debil)
"""
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Restaurante:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
e1 = Empleado("Alex")
r1 = Restaurante()

r1.agregar_empleado(e1)
"""

# Relación de composición (relación fuerte)
"""
class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self):
        self.platos = []

    def agregar_plato(self, nombre, precio):
        plato = Plato(nombre, precio)
        self.platos.append(plato)
    
# plato = Plato("Bandeja paisa", 35000) Esto no se debe hacer porque el plato queda huerfano

pedido = Pedido()
pedido.agregar_plato("Sancocho", 30000)
pedido.agregar_plato("Mojarra frita", 40000)
"""

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario(self):
        pass

class Mesero(Empleado):
    def calcular_salario(self):
        return 1000
    
class Chef(Empleado):
    def calcular_salario(self):
        return 2000