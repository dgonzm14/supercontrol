class EliminarProductoController:
    def __init__(self, logic):
        self.logic = logic

    def cargar_productos(self):
        return self.logic.obtener_productos()

    def eliminar_producto(self, nombre):
        return self.logic.eliminar_producto(nombre)








