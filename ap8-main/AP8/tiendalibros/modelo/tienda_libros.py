class TiendaLibros:
    def __init__(self):
        self.catálogo = {} 
        self.carrito = CarroCompras()  


    def adicionar_libro_a_catálogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catálogo:
            raise LibroExistenteError(titulo, isbn)
        
        libro = Libro(isbn, titulo, precio, existencias)
        self.catálogo[isbn] = libro
        return libro
     
    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.isbn not in self.catálogo:
            raise LibroNoEnCatalogoError("El libro no está en el catálogo.")
        
        libro_en_catalogo = self.catálogo[libro.isbn]
        
        if libro_en_catalogo.existencias <= 0:
            raise LibroAgotadoError("El libro está agotado.")
        
        if cantidad > libro_en_catalogo.existencias:
            raise ExistenciasInsuficientesError("Existencias insuficientes para cubrir la compra.")
        
        self.carrito.agregar_item(libro, cantidad)
        libro_en_catalogo.existencias -= cantidad
    
    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)

