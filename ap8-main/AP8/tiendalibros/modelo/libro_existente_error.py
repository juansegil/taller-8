from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):

    def __init__(self, libro:Libro):
        super().__init__(libro)

    def __str__(self):
        return f'El libro con titulo'"{self.titulo}"  'y isbn' "{self.isbn}"'esta agotado'

    pass
