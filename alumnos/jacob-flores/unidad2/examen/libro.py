class Libro:
    contador = 0

    def __init__(self, titulo, autor, numeroPagina, precio=100, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.numeroPagina = numeroPagina
        self.precio = precio
        self.disponible = disponible
        Libro.contador += 1

    def imprimirDatos(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Numero de Paginas: {self.numeroPagina}")
        print(f"Precio: {self.precio}")
        print(f"Disponible: {self.disponible}")

    @staticmethod
    def contadorDeLibros(self):
        return Libro.contador

    def precioLibros(self, descuento=0):
        if descuento > 15:
            descuento = 15
        elif descuento < 0:
            descuento = 0

        return self.precio - (self.precio * descuento / 100)
