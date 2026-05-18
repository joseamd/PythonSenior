# Sistema de Gestión de Tienda de Videojuegos

Este proyecto consiste en el desarrollo de un sistema básico en Python para administrar una tienda de videojuegos desde consola. La aplicación permite llevar el control del inventario, realizar ventas y consultar información relacionada con los productos registrados.

El programa trabaja con videojuegos almacenados en un diccionario, donde cada uno tiene información como código, nombre, plataforma, precio y cantidad disponible. A partir de estos datos se implementaron diferentes funcionalidades para facilitar la administración de la tienda.

El sistema permite agregar nuevos videojuegos validando que el código no exista previamente y que tanto el precio como la cantidad ingresada sean valores mayores a cero. También es posible visualizar el inventario completo y buscar videojuegos específicos utilizando su código.

Otra funcionalidad importante es la actualización de precios, permitiendo modificar el valor de un videojuego registrado en cualquier momento.

En el módulo de ventas se verifica que el videojuego exista y que haya suficientes unidades disponibles antes de realizar la operación. Cuando una venta se completa, el inventario se actualiza automáticamente y se genera una factura mostrando la información de la compra.

Adicionalmente, se implementó un descuento del 10% para ventas superiores a $500.000 y un historial de ventas donde se almacenan todas las transacciones realizadas. Gracias a esto, el sistema también puede identificar cuál ha sido el videojuego más vendido.

El proyecto incluye funciones estadísticas para mostrar:

- Cantidad total de videojuegos registrados.
- Valor total del inventario.
- Videojuego más costoso.
- Videojuego con mayor cantidad disponible.
- Promedio de precios.

Como funcionalidades adicionales también se incorporaron:

- Búsqueda de videojuegos por plataforma.
- Consulta de videojuegos con inventario bajo.
- Registro y visualización del historial de ventas.

Durante el desarrollo se utilizaron conceptos fundamentales de Python como:

- Condicionales.
- Ciclos for y while.
- Funciones y métodos.
- Diccionarios y listas.
- Validación de datos.
- Programación orientada a objetos.

## Funcionalidades

- Agregar videojuegos
- Mostrar inventario
- Buscar videojuegos por código
- Actualizar precios
- Registrar ventas
- Aplicar descuentos
- Mostrar estadísticas
- Eliminar videojuegos
- Buscar videojuegos por plataforma
- Mostrar videojuegos con inventario bajo
- Mostrar historial de ventas
- Identificar el videojuego más vendido

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos

## Ejecución

Para ejecutar el programa:

```bash
python tienda_videojuegos.py
```

## Nota

Este proyecto fue desarrollado con fines académicos para practicar estructuras de datos, validaciones y lógica de programación en Python.

## Repositorio

https://github.com/joseamd/PythonSenior/tree/main/Modulo1/Unidad_3/proyecto_final

## Autor

José Alexander Muñoz Delgado