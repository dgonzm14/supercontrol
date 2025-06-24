from modelo.dao.eliminar_producto_dao import EliminarProductoDAO

class EliminarProductoLogic:
    def __init__(self, conexion):
        self.dao = EliminarProductoDAO(conexion)
        self.productos = {} 

    def cargar_productos(self):
        productos = self.dao.obtener_productos()
        self.productos = {nombre: id_producto for id_producto, nombre in productos}
        return list(self.productos.keys())

    def eliminar_producto(self, nombre_seleccionado):
        if not nombre_seleccionado:
            return False, "Debes seleccionar un producto."

        id_producto = self.productos.get(nombre_seleccionado)
        if not id_producto:
            return False, "Producto no válido."

        count_detalle, count_precios, count_stock = self.dao.contar_dependencias(id_producto)

        print(f"Filas en detalle_ventas a borrar: {count_detalle}")
        print(f"Filas en precios a borrar: {count_precios}")
        print(f"Filas en stock a borrar: {count_stock}")

        self.dao.eliminar_producto_y_dependencias(id_producto)
        return True, f"Producto '{nombre_seleccionado}' eliminado correctamente."
