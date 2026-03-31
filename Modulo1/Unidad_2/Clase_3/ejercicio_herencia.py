"""
Crear una clase (Padre) Vehículo y tres clases hijas
carro, moto, barco
"""
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, numero_llantas):
        super().__init__(marca, modelo)
        self.numero_llantas = numero_llantas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de llantas: {self.numero_llantas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, numero_llantas):
        super().__init__(marca, modelo)
        self.numero_llantas = numero_llantas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de llantas: {self.numero_llantas}")

class Barco(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)
        self.tipo_motor = tipo_motor 

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de motor: {self.tipo_motor}")

# Prueba
carro1 = Carro("Toyota", "Corolla", 4)
moto1 = Moto("Honda", "CB500", 2)
barco1 = Barco("Yamaha", "242X", "Fueraborda")

carro1.mostrar_info()
moto1.mostrar_info()
barco1.mostrar_info()