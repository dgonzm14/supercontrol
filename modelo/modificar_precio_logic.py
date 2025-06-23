class ModificarPrecioLogic:
    def __init__(self, dao):
        self.dao = dao

    def obtener_productos(self):
        return self.dao.obtener_productos()

    def actualizar_precio(self, id_producto, nuevo_precio):
        if nuevo_precio <= 0:
            return False, "El precio debe ser mayor que cero."
        try:
            self.dao.actualizar_precio(id_producto, nuevo_precio)
            return True, "Precio actualizado correctamente."
        except Exception as e:
            return False, f"Error al actualizar el precio: {e}"
