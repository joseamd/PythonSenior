# class Perro:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def ladrar(self):
#         return "¡Guau!"
    
#     def rascarse(self):
#         print("¡Me estoy rascando!")
    
# perro1 = Perro("Fido", 1)
# perro2 = Perro("Rooney", 2)
# print(perro1.ladrar())
# perro1.rascarse()



class Perro:
    def __init__(self, nombre, raza, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad

    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_raza(self, raza):
        self.__raza = raza
    
    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser mayor que 0")

    # Método para mostrar información
    def mostrar_info(self):
        print("Nombre:", self.get_nombre())
        print("Raza:", self.get_raza())
        print("Edad:", self.get_edad())
        print("------------------------")


# Clase principal
def main():
    perro1 = Perro("Max", "Labrador", 5)
    perro2 = Perro("Bella", "Golden Retriever", 3)
    perro3 = Perro("Rocky", "Bulldog", 4)

    perro1.mostrar_info()
    perro2.mostrar_info()
    perro3.mostrar_info()
   

    # Ejemplo de uso de setter
    perro1.set_edad(6)
    print("Nueva edad del perro 1:", perro1.get_edad())
    perro1.mostrar_info()    

main()
    
    