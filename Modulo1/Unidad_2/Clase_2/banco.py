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