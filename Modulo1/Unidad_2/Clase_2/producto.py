"""
Mini proyecto: Sistema de gestión de productos
Objetivo

Crear un programa orientado a objetos que permita:

Crear productos
Mostrar productos
Buscar productos
Actualizar precio y stock
Vender productos
Eliminar productos
Conceptos que se trabajan
Clases y objetos
Constructor
Encapsulamiento
Getters y setters
Métodos
Listas de objetos
"""

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Getters
    def get_codigo(self):
        return self.__codigo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio
    
    def get_stock(self):
        return self.__stock
    
    # Setters
    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        self.__precio = precio

    def set_stock(self, stock):
        self.__stock = stock

    def mostrar_info(self):
        print("Código:", self.get_codigo())
        print("Nombre:", self.get_nombre())
        print("Precio:", self.get_precio())
        print("Stock:", self.get_stock())
        print("------------------------")


class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self):
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre el producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))

        producto = Producto(codigo, nombre, precio, stock)
        self.__productos.append(producto)
        print("Producto agregado exitosamente.")

    def mostrar_productos(self):
        print("Lista de productos:")
        print("-" * 30)
        for producto in self.__productos:
            producto.mostrar_info()

    def buscar_producto(self, codigo):
        for producto in self.__productos:
            if producto.get_codigo() == codigo:
                return producto
        return None
    
    def actualizar_precio(self, codigo, nuevo_precio):
        producto = self.buscar_producto(codigo)
        if producto:
            producto.set_precio(nuevo_precio)
            print("Precio actualizado exitosamente.")
        else:
            print("Producto no encontrado.")
        
    def actualizar_stock(self, codigo, nuevo_stock):
        producto = self.buscar_producto(codigo)
        if producto:
            producto.set_stock(nuevo_stock)
            print("Stock actualizado exitosamente.")
        else:
            print("Producto no encontrado.")
    
    def vender_producto(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto:
            if producto.get_stock() >= cantidad: 
                producto.set_stock(producto.get_stock() - cantidad)
                print(f"Venta exitosa. Stock restante: {producto.get_stock()}")
            else:
                print("Stock insuficiente")
        else:
            print("Producto no encontrado")

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto:
            self.__productos.remove(producto)
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")


def main():
    inventario = Inventario()
    menu = "===== Sistema de Gestión de Productos =====\n" \
    "1. Agregar producto \n" \
    "2. Mostrar productos \n" \
    "3. Buscar producto \n" \
    "4. Actualizar precio \n" \
    "5. Actualizar stock \n" \
    "6. Vender producto \n" \
    "7. Eliminar producto \n" \
    "8. Salir"    
    opcion = 0
    while opcion != 8:
        print(menu)
        opcion = int(input("Seleccione una opción: \n"))

        match opcion:
            case 1:
                inventario.agregar_producto()
            case 2:
                inventario.mostrar_productos()
            case 3:
                codigo = input("Ingrese el código del producto a buscar: ")
                producto = inventario.buscar_producto(codigo)
                if producto:
                    producto.mostrar_info()
                else:
                    print("Producto no encontrado.")
            case 4:
                codigo = input("Ingrese el código del producto a actualizar: ")   
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                inventario.actualizar_precio(codigo, nuevo_precio)
            case 5:
                codigo = input("Ingrese el código del producto a actualizar: ")   
                nuevo_stock = int(input("Ingrese el nuevo stock: "))
                inventario.actualizar_stock(codigo, nuevo_stock)
            case 6:
                codigo = input("Ingrese el código del producto a vender: ")   
                cantidad = int(input("Ingrese la cantidad a vender: "))
                inventario.vender_producto(codigo, cantidad)
            case 7:
                codigo = input("Ingrese el código del producto a eliminar: ")
                inventario.eliminar_producto(codigo)
            case 8:
                print("Saliendo del sistema. ¡Hasta luego!")
            case _:
                print("Opción no válida. Intente de nuevo.")        


if __name__ == "__main__":    main()

