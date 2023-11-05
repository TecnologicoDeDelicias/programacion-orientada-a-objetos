from libro import Libro

libroQuijote = Libro("Don Quijote de la Mancha", "Miguel Cervantes", 3000)

libroQuijote.imprimirDatos()

print(f"Libros creados {Libro.contadorLibros()}" )
precioSinDescuento = libroQuijote.obtenerPrecio()
precioConDescuento = libroQuijote.obtenerPrecio(10)

print(f"Precio sin descuento {precioSinDescuento}")
print(f"Precio con descuento {precioConDescuento}")

libroHarryPotter = Libro("Harry Potter y la Piedra filosofal", "JK Rowling", 450, 400, False)

libroHarryPotter.imprimirDatos()

print(f"Libros creados {Libro.contadorLibros()}" )

print(f"Precio sin descuento {libroHarryPotter.obtenerPrecio()}")
print(f"Precio con descuento {libroHarryPotter.obtenerPrecio(5)}")