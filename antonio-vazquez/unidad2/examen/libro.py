class Libro:
    def __init__(self, titulo, autor, numeroDePaginas, precio = 100, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.numeroDePaginas = numeroDePaginas
        self.precio = precio
        self.disponible = disponible

    def imprimirDatos(self):
        print(f"Titulo {self.titulo}")

    def obtenerPrecio(self, descuento = 0):
        return self.precio

    @staticmethod
    def contadorLibros():
        return 0