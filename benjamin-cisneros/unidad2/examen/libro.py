class Libro:
    contador_libros = 0

    def __init__(self, titulo, autor, numero_de_paginas, precio = 100, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas
        self.precio = precio
        self.disponible = disponible
        Libro.contador_libros = Libro.contador_libros + 1

    def imprimir_datos(self):
        print(
            f"Titulo: '{self.titulo}', Autor: '{self.autor}', # Páginas: {self.numero_de_paginas}, Precio: ${self.precio}, Disponible: {self.disponible}"
        )

    def obtener_precio(self, descuento=0):
        descuento_porcentaje = 1 - (descuento / 100)
        return self.precio * descuento_porcentaje

    @classmethod
    def libros_creados(cls):
        return cls.contador_libros
