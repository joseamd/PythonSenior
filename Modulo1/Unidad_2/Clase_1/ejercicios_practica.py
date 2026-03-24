"""
1. Crea una clase Vehiculo que tenga:
Atributos privados:

marca
modelo
velocidad (inicia en 0)

Métodos:

acelerar(cantidad) → suma a la velocidad, pero no puede superar 200
frenar(cantidad) → resta a la velocidad, pero no puede bajar de 0
get_velocidad() → retorna la velocidad actual
mostrar_info() → imprime marca, modelo y velocidad actual
"""

class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = 0

    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_velocidad(self):
        return self.__velocidad
    
    def set_marca(self, marca):
        self.__marca = marca
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def acelerar(self, cantidad):
        if self.__velocidad + cantidad <= 200:
            self.__velocidad = self.__velocidad + cantidad
            print(f"Acelerando... velocidad actual: {self.__velocidad}")
        else:
            print("No puedes superar 200")
    
    def frenar(self, cantidad):
        if self.__velocidad - cantidad >= 0:
            self.__velocidad = self.__velocidad - cantidad
            print(f"Frenando... velocidad actual: {self.__velocidad}")
        else:
            print("No puedes bajar de 0")
    
    def mostrar_info(self):
        print(f"La marca es {self.get_marca()}, el model es {self.get_modelo()} y la velocidad es {self.get_velocidad()}")

    
auto = Vehiculo("Toyota", "Corolla")
auto.mostrar_info()     # Toyota Corolla - Velocidad: 0
auto.acelerar(8)
#auto.acelerar(250)      # No puedes superar 200
auto.frenar(9)
#auto.frenar(200)         # No puedes bajar a 0
