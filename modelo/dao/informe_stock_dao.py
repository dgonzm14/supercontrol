class InformeStockDAO:
    def __init__(self, conexion):
        self.conn = conexion

    def obtener_datos_stock(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT p.nombre_producto, p.precio, p.descripcion_producto,
                   ISNULL(s.cantidad, 0) as stock
            FROM productos p
            LEFT JOIN stock s ON p.id_producto = s.id_producto
        """)
        return cursor.fetchall()


