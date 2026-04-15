# Sistema de Gestión de Hospital Veterinario

Este proyecto se desarrolló con el objetivo de representar el funcionamiento básico de un hospital veterinario utilizando programación orientada a objetos en Python.

La idea principal fue modelar situaciones reales que ocurren en una clínica veterinaria, como el registro de clientes, el manejo de mascotas, la atención por parte de un veterinario, la generación de consultas y tratamientos, y finalmente el proceso de facturación y pago.

Todo comienza con la llegada de un cliente a la clínica. La recepcionista se encarga de registrarlo en el sistema, guardando sus datos básicos. Luego, el cliente puede agregar una o más mascotas, las cuales serán atendidas según sea necesario.

Cuando una mascota presenta algún problema, entra en acción el veterinario, quien la atiende y genera una consulta. En esta consulta se registra el motivo, el diagnóstico y se crean los tratamientos necesarios. Cada tratamiento tiene un costo, lo que permite calcular el valor total de la consulta.

Posteriormente, se genera una factura basada en la consulta. Esta factura calcula el subtotal, aplica un impuesto y determina el total a pagar.

Una de las partes más interesantes del sistema es la forma en que se manejan los pagos. Se implementaron diferentes métodos de pago como efectivo, tarjeta y transferencia. Gracias al uso de polimorfismo, es posible cambiar la forma de pago sin modificar la lógica de la factura, lo que hace el sistema más flexible.

Durante el desarrollo se aplicaron varios conceptos clave de la programación orientada a objetos, como la herencia, la agregación, la composición y el polimorfismo, lo que permitió estructurar el sistema de manera organizada y fácil de entender.

## Funcionalidades

- Registro de clientes
- Gestión de mascotas
- Atención por parte de veterinarios
- Creación de consultas
- Generación de tratamientos
- Cálculo de costos
- Generación de facturas
- Pago con diferentes métodos

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos

## Ejecución

Para ejecutar el programa:

```bash
python hospital_veterinario.py
```

## Nota

Este proyecto fue desarrollado con fines académicos para reforzar conceptos de programación orientada a objetos.

## Repositorio

https://github.com/joseamd/PythonSenior/tree/main/Modulo1/Unidad_2/Clase_7

## Autor

José Alexander Muñoz Delgado