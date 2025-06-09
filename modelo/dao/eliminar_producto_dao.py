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

    def contar_dependencias(self, id_producto):
        try:
            cursor = self.conexion.cursor()

            cursor.execute("SELECT COUNT(*) FROM detalle_ventas WHERE id_producto = ?", (id_producto,))
            count_detalle = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM precios WHERE id_producto = ?", (id_producto,))
            count_precios = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM stock WHERE id_producto = ?", (id_producto,))
            count_stock = cursor.fetchone()[0]

            return count_detalle, count_precios, count_stock
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
