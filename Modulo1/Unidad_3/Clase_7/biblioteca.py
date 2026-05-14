"""
Sistema de Gestión de Biblioteca
🎯 Objetivo del reto

Diseñar la estructura de datos más adecuada para representar una biblioteca utilizando listas, diccionarios, conjuntos y tuplas.

El reto no consiste únicamente en almacenar datos, sino en pensar como un arquitecto de software, seleccionando la estructura correcta para cada tipo de información.

📚 Contexto

Una biblioteca necesita almacenar información sobre:

Libros
Autores
Usuarios
Préstamos
Fechas
Categorías

Tu equipo debe diseñar un modelo de datos que permita representar toda esta información de forma organizada y sin redundancias.

📝 Requerimientos del sistema
1. Libros

Cada libro debe almacenar:

ISBN
Título
Año de publicación
Lista de autores
Categorías
Número total de copias
Número de copias disponibles

2. Autores

Cada autor debe tener:

Identificación única
Nombre
Nacionalidad
Año de nacimiento

3. Usuarios

Cada usuario debe almacenar:

ID
Nombre completo
Correo electrónico
Teléfono

4. Préstamos

Cada préstamo debe registrar:

ID del préstamo
Usuario
ISBN del libro
Fecha de préstamo
Fecha de devolución
Estado (activo, devuelto, atrasado)

5. Fechas

Las fechas deben almacenarse usando una estructura apropiada.

6. Categorías

No deben existir categorías repetidas. (conjuntos)

🎯 Parte 1 — Diseñar el esquema de datos

Construyan una estructura principal llamada biblioteca que contenga toda la información.

Sugerencia:
biblioteca = {
    "autores": {},
    "libros": {},
    "usuarios": {},
    "prestamos": {}
}
🎯 Parte 2 — Cargar datos de ejemplo

Agregar al menos:

3 autores
5 libros
4 usuarios
3 préstamos

🎯 Parte 3 — Consultas a resolver

El programa debe mostrar:

Todos los libros disponibles.
Todos los libros de un autor específico.
Todos los préstamos activos.
Usuarios con préstamos atrasados.
Categorías existentes.
Libro más prestado.
Cantidad total de libros.
Cantidad total de préstamos activos.

🎯 Parte 4 — Justificación técnica

El equipo debe explicar:

¿Por qué usaron diccionarios para ciertas entidades?
¿Por qué las categorías son conjuntos?
¿Por qué las fechas pueden representarse como tuplas?
¿Qué ventajas tiene evitar redundancia?

🎯 Parte 5 — Refactorización

Analicen el siguiente diseño deficiente:

biblioteca = [
    ["978001", "Python Básico", "Juan Pérez", "Programación"],
    ["978002", "Python Avanzado", "Juan Pérez", "Programación"],
    ["978003", "Bases de Datos", "Ana Gómez", "Tecnología"]
]
Preguntas
¿Qué redundancias existen?
¿Qué problemas tendría este diseño?
¿Cómo lo reestructurarían?

🏅 Bonus

Agregar:

Historial de préstamos por usuario.
Búsqueda por categoría.
Ranking de usuarios con más préstamos.
"""
biblioteca = {
    "autores" : {},
    "libros" : {},
    "usuarios" : {},
    "prestamos" : {}
}

biblioteca = {
    "autores": {
        1: {
            "nombre": "Gabriel García Márquez",
            "nacionalidad": "Colombia",
            "nacimiento": 1927
        },
        2: {
            "nombre": "Miguel de Cervantes",
            "nacionalidad": "España",
            "nacimiento": 1547
        },
        3: {
            "nombre": "George Orwell",
            "nacionalidad": "Reino Unido",
            "nacimiento": 1903
        },
        4: {
            "nombre": "Antoine de Saint-Exupéry",
            "nacionalidad": "Francia",
            "nacimiento": 1900
        },
        5: {
            "nombre": "J. K. Rowling",
            "nacionalidad": "Reino Unido",
            "nacimiento": 1965
        }
    },
    "libros": {
        "978-0307474728": {
            "titulo": "Cien años de soledad",
            "anio": 1967,
            "autores": [1],                                    
            "categorias": {"Realismo mágico", "Novela latinoamericana"},
            "total_copias": 10,
            "copias_disponibles": 5
        },
        "978-8420412146": {
            "titulo": "Don Quijote de la Mancha",
            "anio": 1605,
            "autores": [2],
            "categorias": {"Novela clásica", "Aventura", "Sátira"},
            "total_copias": 1,
            "copias_disponibles": 0
        },
        "978-0451524935": {
            "titulo": "1984",
            "anio": 1949,
            "autores": [3],
            "categorias": {"Ciencia ficción distópica", "Política"},
            "total_copias": 6,
            "copias_disponibles": 0
        },
        "978-0156012195": {
            "titulo": "El principito",
            "anio": 1943,
            "autores": [4],
            "categorias": {"Literatura infantil", "Fábula filosófica"},
            "total_copias": 4,
            "copias_disponibles": 4
        },
        "978-8478884452": {
            "titulo": "Harry Potter y la piedra filosofal",
            "anio": 1997,
            "autores": [5],
            "categorias": {"Fantasía", "Literatura juvenil"},
            "total_copias": 2,
            "copias_disponibles": 1
        }
    },
    "usuarios": {
        "001" : {
            "nombres" : "Alex Muñoz",
            "correo" : "alexmunoz@gmail.com",
            "telefono" : "555562"
        },
        "002" : {
            "nombres" : "Carlos Ortega",
            "correo" : "carlosortega@gmail.com",
            "telefono" : "555563"
        },
        "003" : {
            "nombres" : "Sandra Caro",
            "correo" : "sandracaro@gmail.com",
            "telefono" : "555564"
        },
        "004" : {
            "nombres" : "Nicolas Mayor",
            "correo" : "nicolasmayor@gmail.com",
            "telefono" : "555565"
        },
    },
    "prestamos": {
        1: {
            "usuario_id": "001",
            "isbn": "978-0307474728",
            "fecha_prestamo": (2026, 4, 1),
            "fecha_devolucion": (2026, 4, 15),
            "estado": "devuelto"
        },
        2: {
            "usuario_id": "002",
            "isbn": "978-8420412146",
            "fecha_prestamo": (2026, 5, 1),
            "fecha_devolucion": (2026, 5, 15),
            "estado": "activo"
        },
        3: {
            "usuario_id": "003",
            "isbn": "978-0451524935",
            "fecha_prestamo": (2026, 4, 20),
            "fecha_devolucion": (2026, 5, 5),
            "estado": "atrasado"
        },
    }
}

# Mostrar Todos los libros disponibles.
print("=" * 60)
print("== LIBROS DISPONIBLES ==")
print("=" * 60)

libros = biblioteca["libros"]
for isbn in libros:
    libro = libros[isbn]
    
    if libro["copias_disponibles"] > 0:
        print(f"Título: {libro["titulo"]} - Disponibles: {libro["copias_disponibles"]}")
    

print("=" * 60)
print("== LIBROS Miguel de Cervantes ==")
print("=" * 60)
id_autor = 2

for isbn in libros:
    libro = libros[isbn]

    if id_autor in libro["autores"]:
        print(f"Título: {libro["titulo"]}")

print("=" * 60)
print("== PRESTAMOS ACTIVOS ==")
print("=" * 60)

prestamos = biblioteca["prestamos"]
for pres in prestamos:
    prestamo = prestamos[pres]

    if prestamo["estado"] == "activo":
        usuario = biblioteca["usuarios"][prestamo["usuario_id"]]["nombres"]
        libro = biblioteca["libros"][prestamo["isbn"]]["titulo"]
        print(f"Id Préstamo: {pres} - Usuario: {usuario} - Libro: {libro}")

print("=" * 60)
print("== PRESTAMOS ATRASADOS ==")
print("=" * 60)

prestamos = biblioteca["prestamos"]
for pres in prestamos:
    prestamo = prestamos[pres]

    if prestamo["estado"] == "atrasado":
        usuario = biblioteca["usuarios"][prestamo["usuario_id"]]["nombres"]
        libro = biblioteca["libros"][prestamo["isbn"]]["titulo"]
        print(f"Id Préstamo: {pres} - Usuario: {usuario} - Libro: {libro}")