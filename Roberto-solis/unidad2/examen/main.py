from libro import Libro 
libroquijote= Libro("Don quijote de la mancha", "miguel cervantes", 3000)
libroquijote.imprimirDatos()
print(f"libros creados{Libro.contadorlibros()}")
precioSinDescuento=libroquijote.obtenerPrecio()
precioConDescuento=libroquijote.obtenerPrecio(10)

print(f"Precio sin descuento" + precioSinDescuento)
print(f"Precio con Descuento" + precioConDescuento)
libroHarryPotter = Libro("Harry Potter y la piedra Filosofal", "jk rewling", 450, 400, False)
libroHarryPotter.imprimirDatos()
print(f"libros creados{libro.contadorlibros()}")
print(f"precio sin descuento{libroHarryPotter.obtenerprecio()}")
print(f"precio con descuento{libroHarryPotter.obtenerprecio(5)}")



