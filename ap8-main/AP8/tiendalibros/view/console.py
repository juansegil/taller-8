import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros
from libro_existente_error import LibroExistenteError
from libro_agotado_error import LibroAgotadoError
from libro_existente_error import ExistenciasInsuficientesError


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro a retirar del carrito: ")

        try:
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print("El libro se ha retirado del carrito con éxito.")
        except LibroNoEnCarritoError:
            print("El libro no está en el carrito.")
        
    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro a agregar al carrito: ")
            cantidad = int(input("Ingrese la cantidad de unidades: "))

            libro = self.tienda_libros.obtener_libro(isbn)

            if libro is None:
                raise LibroNoEnCatalogoError("El libro no está en el catálogo.")

            self.tienda_libros.agregar_libro_a_carrito(isbn, cantidad)
            print(f"El libro se ha agregado al carrito con éxito.")

        except ValueError:
            print("La cantidad debe ser un número entero.")
        except LibroNoEnCatalogoError:
            print("El libro no está en el catálogo.")
        except LibroAgotadoError:
            print("El libro está agotado.")
        except ExistenciasInsuficientesError:
            print("Existencias insuficientes para cubrir la compra.")
    
    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            existencias = int(input("Ingrese las existencias del libro: "))

            libro = self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print(f"El libro '{titulo}' se ha agregado al catálogo con éxito.")

        except ValueError:
            print("Error: El precio o las existencias deben ser números válidos.")
        except LibroExistenteError as e:
            print(f"Error: {e}")