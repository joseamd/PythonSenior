class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Hace sonido genérico"
    

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"
    
class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad


p = Perro("Trosky")
print(f"{p.nombre} dice {p.hacer_sonido()}")

a = Animal("Rooney")
print(f"{a.nombre} dice {a.hacer_sonido()}")


