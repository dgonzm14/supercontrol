class ModificarPrecioController:
    def __init__(self, logic):
        self.logic = logic

    def obtener_productos(self):
        return self.logic.obtener_productos()

    def actualizar_precio(self, id_producto, nuevo_precio):
        return self.logic.actualizar_precio(id_producto, nuevo_precio)

