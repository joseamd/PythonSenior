"""
Ejercicio: Sistema de Empleados en una Empresa
🎯 Objetivo

Desarrollar un pequeño sistema en Python que modele diferentes tipos de empleados utilizando:

Herencia
Abstracción
Polimorfismo
📌 Parte 1: Clase abstracta Empleado

Crea una clase abstracta llamada Empleado que cumpla con lo siguiente:

Debe tener los atributos:
nombre
salario_base
Debe incluir un método abstracto:
calcular_salario() → que será implementado por las subclases
📌 Parte 2: Interfaz Trabajable

Crea una interfaz llamada Trabajable usando clases abstractas (ABC), que tenga:

Un método abstracto:
trabajar()
📌 Parte 3: Clases concretas

Crea las siguientes clases que heredan de Empleado e implementan Trabajable:

👨‍💼 Clase Gerente
Atributo adicional:
bono
Implementar:
calcular_salario() → salario base + bono
trabajar() → imprimir algo como: "El gerente está supervisando el equipo"
👨‍💻 Clase Desarrollador
Atributo adicional:
lenguaje (por ejemplo: Python, Java, etc.)
Implementar:
calcular_salario() → salario base (sin cambios o con lógica simple)
trabajar() → imprimir algo como: "El desarrollador está programando en X lenguaje"
📌 Parte 4: Uso del polimorfismo

En el programa principal:

Crea una lista de empleados que incluya:
Al menos un Gerente
Al menos un Desarrollador
Recorre la lista y para cada empleado:
Llama al método trabajar()
Imprime su salario usando calcular_salario()

👉 Ejemplo esperado (salida aproximada):

El gerente está supervisando el equipo
Salario: 5000

El desarrollador está programando en Python
Salario: 3000

⭐ Reto adicional (opcional)
Agrega una nueva clase Diseñador
Modifica el sistema para que todos los empleados puedan tener un aumento porcentual
Valida que no se puedan crear objetos de la clase Empleado directamente
💡 Pistas
Usa:
from abc import ABC, abstractmethod
Recuerda usar super() para reutilizar el constructor de la clase padre
"""

from abc import ABC, abstractmethod 

class Trabajable(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Empleado, Trabajable):
    
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self):
        return self.salario_base + self.bono
    
    def trabajar(self):
        print(f"El gerente {self.nombre} está supervisando el equipo")

class Desarrollador(Empleado, Trabajable):
    
    def __init__(self, nombre, salario_base, lenguaje):
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje

    def calcular_salario(self):
        return self.salario_base
    
    def trabajar(self):
        print(f"El desarrollador {self.nombre} está programando en el lenguaje {self.lenguaje}")

class Diseñador(Empleado, Trabajable):

    def __init__(self, nombre, salario_base, framework):
        super().__init__(nombre, salario_base)
        self.framework = framework

    def calcular_salario(self):
        return self.salario_base
    
    def trabajar(self):
        print(f"El diseñador {self.nombre} usa el framework {self.framework} para las UI")


empleados = [
    Gerente("Ana", 4000, 1000),
    Desarrollador("Luis", 3000, "Python"),
    Diseñador("Carlos",3500, "Angular")
]

for empleado in empleados:
    empleado.trabajar()
    print(f"Salario {empleado.calcular_salario()}")
    print("-" * 30)