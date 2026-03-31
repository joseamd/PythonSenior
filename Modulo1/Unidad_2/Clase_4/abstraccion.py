from abc import ABC, abstractmethod 

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
# f = Cuadrado(7)
# print(f.area())

"""
Crear clase abstrata Empleado, Método abstracto calcular salario
sub clase desarrollador
"""

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, num_dias, valor_dia):
        self.num_dias = num_dias
        self.valor_dia = valor_dia

    def calcular_salario(self):
        return self.num_dias * self.valor_dia
        
d = Desarrollador(30, 30000)
print(f"El salario del desarrollador es: {d.calcular_salario()}")