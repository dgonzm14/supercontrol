class StockDAOModStock:
    def __init__(self, conexion):
        self.conn = conexion

    def obtener_productos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_producto, nombre_producto FROM productos ORDER BY nombre_producto")
        return cursor.fetchall()

    def existe_stock(self, id_producto):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM stock WHERE id_producto = ?", (id_producto,))
        return cursor.fetchone()[0] > 0

    def actualizar_stock(self, id_producto, cantidad):
        cursor = self.conn.cursor()
        if self.existe_stock(id_producto):
            cursor.execute("UPDATE stock SET cantidad = ? WHERE id_producto = ?", (cantidad, id_producto))
        else:
            cursor.execute("INSERT INTO stock (id_producto, cantidad) VALUES (?, ?)", (id_producto, cantidad))
        self.conn.commit()
