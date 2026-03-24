class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

persona1 = Persona("Juan")
print(persona1.get_nombre())
persona1 = Persona("Carlos")
persona1.set_nombre("Carlos")
print(persona1.get_nombre())

#getters y setters son métodos que se utilizan para acceder y modificar