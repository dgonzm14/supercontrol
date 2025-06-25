class EliminarProductoLogic:
    def __init__(self, dao):
        self.dao = dao

    def obtener_productos(self):
        try:
            productos = self.dao.obtener_productos()
            nombres = [prod[1] for prod in productos]  
            return True, nombres
        except Exception as e:
            return False, str(e)

    def eliminar_producto(self, nombre_producto):
        try:
            productos = self.dao.obtener_productos()
            id_producto = None
            for prod in productos:
                if prod[1] == nombre_producto:
                    id_producto = prod[0]
                    break

            if id_producto is None:
                return False, "Producto no encontrado"

            
            self.dao.eliminar_producto_y_dependencias(id_producto)
            return True, "Producto eliminado correctamente"
        except Exception as e:
            return False, str(e)





