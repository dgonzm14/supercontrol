from modelo.eliminar_producto_logic import EliminarProductoLogic

class EliminarProductoController:
    def __init__(self, conexion):
        self.logic = EliminarProductoLogic(conexion)

    def cargar_productos(self):
        try:
            nombres = self.logic.cargar_productos()
            return True, nombres
        except Exception as e:
            return False, f"No se pudo cargar productos:\n{e}"

    def eliminar_producto(self, nombre_seleccionado):
        try:
            return self.logic.eliminar_producto(nombre_seleccionado)
        except Exception as e:
            return False, f"No se pudo eliminar el producto:\n{e}"



