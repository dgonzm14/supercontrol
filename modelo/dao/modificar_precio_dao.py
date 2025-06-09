class ModificarPrecioDAO:
    def __init__(self, conexion):
        self.conn = conexion

    def obtener_productos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_producto, nombre_producto, descripcion_producto, precio FROM productos")
        productos = cursor.fetchall()
        cursor.close()
        return productos

    def actualizar_precio(self, id_producto, nuevo_precio):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE productos SET precio = ? WHERE id_producto = ?", (nuevo_precio, id_producto))
        self.conn.commit()
        cursor.close()
