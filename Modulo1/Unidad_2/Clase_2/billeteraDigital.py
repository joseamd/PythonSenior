"""
Vas a crear una clase llamada CuentaBancaria que simule una billetera digital como Nequi o Daviplata.

🔹 Requisitos
1. Atributos

Debes usar los tres niveles de acceso:

titular → Público
_historial → Protegido
__saldo → Privado
2. Constructor

Debe recibir:

titular
saldo inicial
3. Métodos obligatorios
🔹 Getters y Setters
Obtener saldo (NO acceso directo)
Modificar saldo SOLO con validación
🔹 Funcionalidades
depositar(monto)
retirar(monto)
ver_saldo()
ver_historial()
4. Validaciones
No permitir saldo negativo
No permitir retiros mayores al saldo
No permitir depósitos negativos
5. Prueba del sistema

En el programa principal:

Crear una cuenta
Depositar dinero
Retirar dinero
Mostrar saldo
Mostrar historial
"""

class CuentaBancaria:
    def __init__(self, cedula, titular, saldo_inicial):
        self.cedula = cedula
        self.titular = titular
        self._historial = []
        self.__saldo = 0
        self.depositar(saldo_inicial)

    # Getters
    def get_saldo(self):
        return self.__saldo
    
    # Setters
    def set_saldo(self, monto):
        if monto < 0:
            print("No se puede establecer un saldo negativo.")
            return
        self.__saldo = monto    

    def depositar(self, monto):
        if monto <= 0:
            print("El monto a depositar debe ser positivo.")
            return
        self.__saldo += monto
        self._historial.append(f"Depósito: +{monto}")
    
    def retirar(self, monto):
        if monto <=0 :
            print("El monto a retirar debe ser positivo.")
            return
        if monto > self.__saldo:
            print("No se puede retirar más de lo que tienes en la cuenta.")
            return
        self.__saldo -= monto
        self._historial.append(f"Retiro: -{monto}")
    
    def ver_saldo(self):
        print(f"Saldo actual: {self.get_saldo()}")

    def ver_historial(self):
        print("Historial de transacciones:")
        for transaccion in self._historial:
            print(transaccion)
        print()

def buscar_por_cedula(cuentas, cedula):
        for cuenta in cuentas:
            if cuenta.cedula == cedula:
                return cuenta
        return None

def main():

    menu = "===== Billetera Digital =====\n" \
    "1. Crear cuenta \n" \
    "2. Depositar dinero \n" \
    "3. Retirar dinero \n" \
    "4. Mostrar saldo \n" \
    "5. Mostrar historial \n" \
    "6. Salir"   

    opcion = 0
    cuentas = []

    while opcion != 6:
        print(menu)
        opcion = int(input("Seleccione una opción: \n"))

        match opcion:
            case 1:
                cedula = input("Ingrese la cédula del titular: ")
                titular = input("Ingrese el nombre del titular: ")
                saldo_inicial = float(input("Ingrese el saldo inicial: "))
                cuenta = CuentaBancaria(cedula, titular, saldo_inicial)
                cuentas.append(cuenta)
                print("Cuenta creada exitosamente. \n")
            
            case 2:
                cedula = input("Ingrese la cédula: ")
                cuenta = buscar_por_cedula(cuentas, cedula)
                if cuenta:
                    monto = float(input("Ingrese el monto a depositar: "))
                    cuenta.depositar(monto)
                else:
                    print("Cuenta no encontrada. \n")

            case 3:
                cedula = input("Ingrese la cédula: ")
                cuenta = buscar_por_cedula(cuentas, cedula)
                if cuenta:
                    monto = float(input("Ingrese el monto a retirar: "))
                    cuenta.retirar(monto)
                else:
                    print("Cuenta no encontrada. \n")

            case 4:
                cedula = input("Ingrese la cédula: ")
                cuenta = buscar_por_cedula(cuentas, cedula)
                if cuenta:
                    cuenta.ver_saldo()
                else:
                    print("Cuenta no encontrada. \n")

            case 5:
                cedula = input("Ingrese la cédula: ")
                cuenta = buscar_por_cedula(cuentas, cedula)
                if cuenta:
                    cuenta.ver_historial()
                else:
                    print("Cuenta no encontrada.\n")

            case 6:
                print("Saliendo del sistema. ¡Hasta luego! \n")

            case _:
                print("Opción no válida. Intente de nuevo. \n")
            
if __name__ == "__main__":    main()