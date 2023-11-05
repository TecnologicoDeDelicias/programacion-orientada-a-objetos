from libro import Libro

def test(libro, descuento):
    libro.imprimir_datos()
    print(f"Libros creados: {Libro.libros_creados()}" )
    print(f"Precio sin descuento: {libro.obtener_precio()}")
    print(f"Precio con descuento: {libro.obtener_precio(descuento)}")

libro_quijote = Libro("Don Quijote de la Mancha", "Miguel Cervantes", 3000)
test(libro_quijote, 10)

libro_harry = Libro("Harry Potter y la Piedra filosofal", "JK Rowling", 450, 400, False)
test(libro_harry, 5)
