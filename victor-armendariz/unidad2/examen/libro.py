class Libro:
    contador_libros = 0
    def __init__(self, titulo, autor, numeroDePaginas, precio = 100, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.numeroDePaginas = numeroDePaginas
        self.precio = precio
        self.disponible = disponible
        Libro.contador_libros = Libro.contador_libros + 1

    def imprimirDatos(self):
        print(f"Titulo {self.titulo}")

    def obtenerPrecio(self, descuento = 0):
        return self.precio

    @classmethod
    def contadorLibros(cls):
        return cls.contador_libros