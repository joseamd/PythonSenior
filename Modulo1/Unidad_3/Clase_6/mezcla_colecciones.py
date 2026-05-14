"""
Sistema de Gestión de Biblioteca
Enunciado completo

Desarrollar en Python un programa que permita gestionar una biblioteca usando estructuras compuestas de datos.

El programa debe utilizar:

Diccionarios
Listas
Diccionarios anidados
Listas de diccionarios
Restricciones

El programa debe cumplir estas condiciones:

No usar funciones.
No usar archivos.
No usar bases de datos.
Todo debe trabajarse en memoria.
El programa debe tener un menú interactivo.
El código debe estar documentado con comentarios.
Contexto

Una biblioteca necesita organizar la información de sus libros, usuarios y préstamos.

El sistema debe permitir registrar libros, registrar usuarios, prestar libros, devolver libros y consultar información general.

Estructura sugerida

El sistema debe manejar un diccionario principal llamado biblioteca con la siguiente estructura:

biblioteca = {
    "libros": {},
    "usuarios": {},
    "prestamos": []
}
Funcionalidades obligatorias
1. Agregar libro

El sistema debe solicitar:

Código del libro
Título
Autor
Año de publicación
Categoría

Cada libro debe guardarse con estado disponible.

2. Mostrar libros

Debe mostrar todos los libros registrados, indicando:

Código
Título
Autor
Año
Categoría
Disponibilidad
3. Eliminar libro

Debe permitir eliminar un libro por su código.

No se debe eliminar un libro si está prestado.

4. Registrar usuario

El sistema debe solicitar:

Código del usuario
Nombre
Teléfono
5. Mostrar usuarios

Debe mostrar todos los usuarios registrados.

6. Prestar libro

El sistema debe solicitar:

Código del usuario
Código del libro
Fecha de préstamo
Fecha estimada de entrega

Condiciones:

El usuario debe existir.
El libro debe existir.
El libro debe estar disponible.
Al prestarlo, el libro debe cambiar a no disponible.
El préstamo debe guardarse en una lista de préstamos.

7. Devolver libro

El sistema debe solicitar el código del libro.

Condiciones:

El libro debe existir.
El libro debe estar prestado.
Al devolverlo, debe cambiar nuevamente a disponible.
El préstamo activo debe marcarse como devuelto.

8. Mostrar préstamos activos

Debe mostrar solo los préstamos que aún no han sido devueltos.

9. Mostrar historial de préstamos

Debe mostrar todos los préstamos realizados, tanto activos como devueltos.

10. Salir

Finaliza el programa.
"""
