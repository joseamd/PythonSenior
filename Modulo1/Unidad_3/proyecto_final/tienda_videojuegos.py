"""
Ejercicio Integrador en Python
Sistema de Gestión de una Tienda de Videojuegos
Objetivo
Desarrollar un programa en Python que permita administrar el inventario y las ventas de una tienda de videojuegos utilizando:
Variables
Condicionales (if, elif, else)
Ciclos (while, for)
Funciones
Colecciones (diccionarios y listas)
Enunciado del Problema
Una tienda de videojuegos desea llevar el control de sus productos y ventas.
Cada videojuego tendrá la siguiente información:
Código
Nombre
Plataforma (PC, PlayStation, Xbox, Nintendo)
Precio
Cantidad en inventario
La información se almacenará en un diccionario con la siguiente estructura:
Python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    }
}
Menú Principal
El programa debe mostrar repetidamente el siguiente menú:
Plain text
===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por código
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir
Requisitos del Programa
1. Agregar videojuego
Crear una función que solicite los datos del videojuego y lo agregue al diccionario.
Validaciones:
No se debe permitir un código repetido.
El precio y la cantidad deben ser mayores que cero.
2. Mostrar inventario
Recorrer el diccionario e imprimir todos los videojuegos registrados.
3. Buscar videojuego por código
Solicitar un código y mostrar toda la información del videojuego si existe.
4. Actualizar precio
Permitir cambiar el precio de un videojuego existente.
5. Registrar venta
Solicitar:
Código del videojuego
Cantidad a vender
Validaciones:
El videojuego debe existir.
Debe haber suficiente inventario.
Acciones:
Restar del inventario.
Calcular el valor total de la venta.
Mostrar factura.
6. Mostrar estadísticas
Crear una función que muestre:
Total de videojuegos registrados.
Valor total del inventario.
Videojuego más costoso.
Videojuego con mayor cantidad disponible.
Promedio de precios.
7. Eliminar videojuego
Eliminar un videojuego por código.
8. Salir
Finalizar el programa.
Requisitos Técnicos
Funciones obligatorias
Debes implementar al menos las siguientes funciones:
Python
def agregar_videojuego(videojuegos):
def mostrar_inventario(videojuegos):
def buscar_videojuego(videojuegos):
def actualizar_precio(videojuegos):
def registrar_venta(videojuegos):
def mostrar_estadisticas(videojuegos):
def eliminar_videojuego(videojuegos):
def menu():
Datos Iniciales de Prueba
Python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}
Ejemplo de Venta
Plain text
Ingrese código del videojuego: VG001
Ingrese cantidad a vender: 2

Factura:
Juego: FIFA 26
Precio unitario: $250000
Cantidad: 2
Total: $500000
Retos Adicionales (Opcionales)
Si terminas antes, agrega:
Buscar videojuegos por plataforma.
Mostrar videojuegos con inventario bajo (cantidad < 3).
Aplicar descuentos del 10% en ventas mayores a $500.000.
Guardar historial de ventas en una lista.
Mostrar el videojuego más vendido.
Conceptos que Practicarás
Diccionarios anidados
Listas
Funciones con parámetros y retorno
Condicionales
Ciclos while y for
Validación de datos
Cálculos estadísticos básicos
Nivel de Dificultad
Intermedio
Tiempo Estimado
2 a 3 horas
Resultado Esperado
Al finalizar tendrás un sistema completo de consola para administrar una tienda de videojuegos, aplicando de 
forma práctica los principales fundamentos de Python.
"""

class GestionVideoJuegos:
    def __init__(self):
        # Datos iniciales de prueba
        self.videojuegos = {
            "VG001": {
                "nombre": "FIFA 26",
                "plataforma": "PlayStation 5",
                "precio": 250000,
                "cantidad": 10
            },
            "VG002": {
                "nombre": "Zelda: Breath of the Wild",
                "plataforma": "Nintendo Switch",
                "precio": 220000,
                "cantidad": 5
            },
            "VG003": {
                "nombre": "Forza Horizon 5",
                "plataforma": "Xbox Series X",
                "precio": 210000,
                "cantidad": 8
            }
        }
        # Lista para registrar el historial de ventas
        self.historial_ventas = []

    def mostrar_menu(self):
        menu = """
            ========================================
                    TIENDA DE VIDEOJUEGOS
            ========================================
            1. Agregar videojuego
            2. Mostrar inventario
            3. Buscar videojuego por código
            4. Actualizar precio
            5. Registrar venta
            6. Mostrar estadísticas
            7. Eliminar videojuego
            8. Buscar videojuegos por plataforma
            9. Videojuegos con inventario bajo
            10. Historial de ventas
            11. Videojuego más vendido
            12. Salir
            ========================================
            """
        print(menu)

    def agregar_videojuego(self):
        print("== Registro de Videojuegos ==\n")
        codigo_juego = input("Ingrese código del videojuego: ")
        nombre_juego = input("Ingrese nombre del videojuego: ")
        plataforma = input("Ingrese nombre de la plataforma: ")
        precio = float(input("Ingrese valor del videojuego: "))   
        while precio <= 0:
            print("El valor del precio debe ser mayor a cero")
            precio = float(input("Ingrese valor del videojuego nuevamente: ")) 

        cantidad = int(input("Ingrese la cantidad: "))
        while cantidad <= 0:        
            print("La cantidad debe ser mayor a cero")
            cantidad = int(input("Ingrese cantidad nuevamente: ")) 

        if codigo_juego in self.videojuegos:
            print(f'El código: {codigo_juego} ya existe')
        else:
            self.videojuegos[codigo_juego]={
                "nombre": nombre_juego,
                "plataforma": plataforma,
                "precio": precio,
                "cantidad": cantidad
            }
            print(f'El videojuego {nombre_juego} agregado exitosamente.')

    def mostrar_inventario(self):
        print("== Inventario de Videojuegos ==\n")
        if not self.videojuegos:
            print("No existen videojuegos")
        else:
            for codigo in self.videojuegos:
                juego = self.videojuegos[codigo]
                print(f'Videojuego: {juego["nombre"]} - Plataforma: {juego["plataforma"]} - Precio: ${juego["precio"]:,.0f} - Disponible: {juego["cantidad"]}')


    def buscar_videojuego(self):
        print("== Buscar videojuego ==")
        codigo = input("Ingrese código del videojuego: ")
        if codigo in self.videojuegos:
            juego = self.videojuegos[codigo]
            print(f'Videojuego: {juego["nombre"]} - Plataforma: {juego["plataforma"]} - Precio: ${juego["precio"]:,.0f} - Disponible: {juego["cantidad"]}')
        else:
            print("Código no Existe")

    def actualizar_precio(self):
        print("== Actualizar Videojuego ==")
        codigo = input("Ingrese código del videojuego: ")
        if codigo in self.videojuegos:
            precio_nuevo = float(input("Ingrese valor del videojuego: ")) 
            while precio_nuevo <= 0:
                print("El valor del precio debe ser mayor a cero")
                precio_nuevo = float(input("Ingrese valor del videojuego nuevamente: ")) 
            self.videojuegos[codigo]["precio"] = precio_nuevo
            print("Precio actualizado exitosamente")
        else:
            print("Código no Existe")

    def registrar_venta(self):
        print("== Registrar venta de Videojuegos ==")
        codigo = input("Ingrese código del videojuego: ")
        if codigo in self.videojuegos:
            juego = self.videojuegos[codigo]
            cantidad = int(input("Ingrese cantidad a vender: "))
            while cantidad <= 0:
                print("La cantidad debe ser mayor a cero")
                cantidad = int(input("Ingrese cantidad a vender nuevamente: "))

            if cantidad <= juego["cantidad"]:
                # Restar del inventario la cantidad vendida
                juego["cantidad"] -= cantidad
                
                valor_venta = juego["precio"] * cantidad

                # Aplicar descuento del 10% en ventas mayores a $500.000
                descuento = valor_venta > 500000
                if descuento:
                    valor_venta = valor_venta - (valor_venta * 0.10)                    

                print(f"-------Factura-------")
                print(f'VideoJuego: {juego["nombre"]}')
                print(f'Precio unitario: ${juego["precio"]:,.0f}')
                print(f'Cantidad: {cantidad}')
                if descuento:
                    print("Descuento aplicado: 10%")
                print(f'Total: ${valor_venta:,.0f}')

                # Guardar la venta en el historial
                self.historial_ventas.append({
                    "codigo": codigo,
                    "nombre": juego["nombre"],
                    "precio_unitario": juego["precio"],
                    "cantidad": cantidad,
                    "total": valor_venta
                })
            else :
                print("No hay suficiente inventario disponible")
        else:
            print("Código no Existe")

    def mostrar_estadisticas(self):
        print("== Estadísticas ==")

        if not self.videojuegos:
            print("No hay videojuegos registrados.")
            return                     

        # Calcular valor total del inventario (precio x cantidad de cada juego)                
        total_inventario = 0
        suma_precios = 0

        for codigo in self.videojuegos:
            juego = self.videojuegos[codigo]

            total_inventario += juego["precio"] * juego["cantidad"]
            suma_precios += juego["precio"]

        total_juegos = len(self.videojuegos)    
        promedio = suma_precios / total_juegos
        
        # Encontrar el juego más costoso y el de mayor cantidad
        max_costoso = max(self.videojuegos.values(), key=lambda j: j["precio"])        
        max_cantidad = max(self.videojuegos.values(), key=lambda j: j["cantidad"])
        
        print(f'Total de Videojuegos: {total_juegos}')
        print(f'Valor total del inventario: ${total_inventario:,.0f}')
        print(f'Videojuego más costoso: {max_costoso["nombre"]}')
        print(f'Videojuego con mayor cantidad disponible: {max_cantidad["nombre"]}')        
        print(f'Promedio de precios: {promedio:,.0f}')

    def eliminar_videojuego(self):
        print("== Eliminar Videojuego ==")
        codigo = input("Ingrese código del videojuego: ")
        if codigo in self.videojuegos:
            nombre = self.videojuegos[codigo]["nombre"]
            self.videojuegos.pop(codigo)
            print(f'El videojuego "{nombre}" fue eliminado exitosamente.')
        else:
            print("Código no Existe")

    def buscar_videojuego_plataforma(self):
        print("== Videojuegos por plataforma==")
        plataforma = input("Ingrese nombre de la plataforma: ")

        encontrados = 0
        for codigo in self.videojuegos:
            juego = self.videojuegos[codigo]
            if juego["plataforma"].lower() == plataforma.lower():
                print(f'Videojuego: {juego["nombre"]} - Plataforma: {juego["plataforma"]} - Precio: ${juego["precio"]:,.0f} - Disponible: {juego["cantidad"]}')
                encontrados += 1

        if encontrados == 0:
            print(f'No hay videojuegos para la plataforma "{plataforma}"')

    
    def inventario_bajo(self):
        print("== Inventario Bajo de Videojuegos ==\n")
        if not self.videojuegos:
            print("No existen videojuegos")
        else:
            encontrados = 0
            for codigo in self.videojuegos:
                juego = self.videojuegos[codigo]
                if juego["cantidad"] < 3:
                    print(f'Videojuego: {juego["nombre"]} - Plataforma: {juego["plataforma"]} - Precio: ${juego["precio"]:,.0f} - Disponible: {juego["cantidad"]}')
                    encontrados += 1

            if encontrados == 0:
                print("No hay videojuegos con inventario bajo.")
    
    def mostrar_historial_ventas(self):
        print("== Historial de Ventas ==")
        if not self.historial_ventas:
            print("No hay ventas registradas.")
            return
        
        print(f'{"N°":<5} {"Código":<8} {"Nombre":<30} {"Cantidad":<10} {"Precio Unit.":<15} {"Total"}')
        for i, venta in enumerate(self.historial_ventas, 1):
            print(f'{i:<5} {venta["codigo"]:<8} {venta["nombre"]:<30} {venta["cantidad"]:<10} ${venta["precio_unitario"]:<14,.0f} ${venta["total"]:,.0f}')

    def videojuego_mas_vendido(self):
        print("== Videojuego más vendido ==")

        if not self.historial_ventas:
            print("No hay ventas registradas")
            return

        ventas_por_codigo = {}
        
        # Acumular cantidad vendida por código
        for venta in self.historial_ventas:
            codigo = venta["codigo"]
            if codigo in ventas_por_codigo:
                ventas_por_codigo[codigo] += venta["cantidad"]
            else:
                ventas_por_codigo[codigo] = venta["cantidad"]

        # Encontrar el código con mayor cantidad vendida
        max_vendido_codigo = max(ventas_por_codigo, key=lambda c: ventas_por_codigo[c])
        max_vendido = ventas_por_codigo[max_vendido_codigo]   
        
        nombre = self.videojuegos[max_vendido_codigo]["nombre"]
        print(f'Videojuego más vendido: {nombre} con {max_vendido} unidades vendidas')

def main():
    gestion = GestionVideoJuegos()

    while True:
        gestion.mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion.isdigit():
            opcion = int(opcion)
        else:
            print("Debe ingresar un número válido del menú")
            continue

        match opcion:
            case 1:
                gestion.agregar_videojuego()
                print("-" * 60)

            case 2:
                gestion.mostrar_inventario()
                print("-" * 60)

            case 3:
                gestion.buscar_videojuego()
                print("-" * 60)

            case 4:
                gestion.actualizar_precio()
                print("-" * 60)

            case 5:
                gestion.registrar_venta()
                print("-" * 60)

            case 6:
                gestion.mostrar_estadisticas()
                print("-" * 60)

            case 7:
                gestion.eliminar_videojuego()
                print("-" * 60)

            case 8:
                gestion.buscar_videojuego_plataforma()
                print("-" * 60)

            case 9:
                gestion.inventario_bajo()
                print("-" * 60)

            case 10:
                gestion.mostrar_historial_ventas()
                print("-" * 60)

            case 11:
                gestion.videojuego_mas_vendido()
                print("-" * 60)

            case 12:
                print("¡Hasta luego!")
                break

            case _:
                print("Opción inválida")

if __name__ == "__main__":
    main()