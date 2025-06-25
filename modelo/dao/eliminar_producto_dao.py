class EliminarProductoDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_productos(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT id_producto, nombre_producto FROM productos")
            return cursor.fetchall()
        except Exception as e:
            raise e

    def eliminar_producto_y_dependencias(self, id_producto):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM detalle_ventas WHERE id_producto = ?", (id_producto,))
            cursor.execute("DELETE FROM precios WHERE id_producto = ?", (id_producto,))
            cursor.execute("DELETE FROM stock WHERE id_producto = ?", (id_producto,))
            cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id_producto,))
            self.conexion.commit()
        except Exception as e:
            self.conexion.rollback()
            raise e


