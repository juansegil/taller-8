class CarroCompras:
    pass
    def __init__(self):
        self.items = []

    def agregar_item(self, libro, cantidad):
        item = itemcompra(libro, cantidad)
        self.item.append(item)
        return item
    
    def calcular_total(self):
        total = 0
        for item in self.items:
            subtotal = item.calcular_subtotal()
            total += subtotal
            return total
        
    def quitar_item(self, isbn):
        self.item = [item for item in self.items if self.isbn != isbn]
