"""
Mini Proyecto: Sistema de Gestión de Restaurante (POO Avanzado)
🎯 Objetivo

Desarrollar un sistema en Python que permita gestionar un restaurante aplicando:

Composición y agregación
Clases abstractas
Relaciones bidireccionales
Bajo acoplamiento
Buenas prácticas de diseño
🧩 Descripción del problema

Se necesita modelar un sistema que permita:

Registrar clientes
Crear pedidos con múltiples platos
Asignar meseros a pedidos
Calcular cuentas y generar facturas
Aplicar diferentes tipos de pago
🏗️ Requisitos del sistema
1. 👤 Clientes
Un cliente puede tener múltiples pedidos (relación bidireccional)
2. 📦 Pedidos
Un pedido:
Pertenece a un cliente
Tiene varios platos (composición)
Tiene un estado (pendiente, servido, pagado)
Tiene un mesero asignado (agregación)
3. 🍝 Platos
Nombre
Precio
4. 👨‍🍳 Empleados (Clase abstracta)

Crear una clase abstracta:

Empleado

Métodos:

calcular_salario()

Subclases:

Mesero
Chef
5. 🧾 Factura
Asociada a un pedido
Calcula:
Total
Impuestos
Descuento opcional
6. 💳 Métodos de pago (tipo interfaz)

Crear una abstracción:

MetodoPago

Implementaciones:

Pago con tarjeta
Pago en efectivo

👉 Debe usarse polimorfismo

🔗 Relaciones clave (muy importante)
Relación	Tipo
Pedido → Plato	Composición
Restaurante → Empleados	Agregación
Pedido → Mesero	Agregación
Cliente ↔ Pedido	Bidireccional
💻 Estructura sugerida
abc/
modelos/
    cliente.py
    pedido.py
    plato.py
    empleado.py
    factura.py
    pago.py
main.py
🚀 Funcionalidades mínimas (MVP)

✔ Crear cliente
✔ Crear pedido
✔ Agregar platos
✔ Asignar mesero
✔ Calcular total
✔ Generar factura
✔ Pagar pedido

⭐ Funcionalidades extra (para subir nota)
Validar que un pedido no esté vacío
Manejar errores (exceptions)
Aplicar descuentos
Mostrar historial de pedidos por cliente
Separar lógica en módulos
🧪 Ejemplo de uso esperado
cliente = Cliente("Ana")

pedido = Pedido(cliente)
pedido.agregar_plato("Pizza", 20)
pedido.agregar_plato("Refresco", 5)

mesero = Mesero("Carlos")
pedido.asignar_mesero(mesero)

factura = Factura(pedido)
print(factura.calcular_total())

pago = PagoTarjeta()
pago.pagar(factura)
"""

from abc import ABC, abstractmethod

# Clase abstracta y herencia

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        

    @abstractmethod
    def calcular_salario(self):
        pass

class Mesero(Empleado):
    def calcular_salario(self):
        return 1200
    
class Chef(Empleado):
    def calcular_salario(reslf):
        return 2000
    
#Cliente y agregación con Pedido

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []
        
    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

#Plato
class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

#Pedido y composición con Plato

class Pedido:
    def __init__(self, cliente):
        self.estado = "pendiente"
        self.platos = []
        self.cliente = cliente
        self.mesero = None

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def asignar_mesero(self, mesero):
        self.mesero = mesero

    def calcular_total(self):
        return sum(plato.precio for plato in self.platos)
    
#Restaurante agregacion empleados y clientes

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []
        
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

class MetodoPago(ABC):
    def __init__(self, monto):
        self.monto = monto

    @abstractmethod
    def procesar_pago(self, monto):
        pass

class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago en efectivo procesado por {monto}."
    
class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago con tarjeta procesado por {monto}."
    
#Factura y asociación con MetodoPago
class Factura:
    def __init__(self, pedido, impuestos = 0.19, descuento = 0):
        self.pedido = pedido
        self.impuestos = impuestos
        self.descuento = descuento
        
    def calcular_total(self):
        subtotal = self.pedido.calcular_total()
        total = subtotal + (subtotal * self.impuestos) - self.descuento
        return total
    
    def pagar(self, metodo_pago: MetodoPago):
        total = self.calcular_total()
        return metodo_pago.procesar_pago(total)
    
restaurante = Restaurante("El Buen Sabor")
mesero = Mesero("Juan")
chef = Chef("Maria")

restaurante.agregar_empleado(mesero)
restaurante.agregar_empleado(chef)

cliente = Cliente("Carlos")
restaurante.agregar_cliente(cliente)

plato1 = Plato("Pasta", 10)
plato2 = Plato("Bandeja paisa", 15)

pedido = Pedido(cliente)
pedido.agregar_plato(plato1)
pedido.agregar_plato(plato2)
pedido.asignar_mesero(mesero)

cliente.agregar_pedido(pedido)

factura = Factura(pedido, descuento=5)
print("Total a pagar:", factura.calcular_total())

pago = PagoTarjeta(factura.calcular_total())
print(factura.pagar(pago))