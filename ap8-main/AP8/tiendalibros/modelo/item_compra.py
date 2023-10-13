class ItemCompra:
    def __init__(self, libro, cantidad_tipo_libro:int):
        self.libro = libro
        self.cantidad_tipo_libro = cantidad
    def calcular_subtotal(self):
        subtotal = self.cantidad*self.precio
        return subtotal
    pass
