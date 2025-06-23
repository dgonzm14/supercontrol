from modelo.producto_service import ProductoService

class AniadirProductoController:
    def __init__(self, conexion):
        self.service = ProductoService(conexion)

    def agregar_producto(self, nombre, descripcion):
        return self.service.agregar_producto(nombre, descripcion)


