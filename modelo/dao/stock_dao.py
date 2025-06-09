# modelo/stock_dao.py
class StockDAO:
    def __init__(self, conexion):
        self.conn = conexion

    def obtener_todo_stock(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT p.nombre_producto, s.cantidad, p.descripcion_producto
            FROM productos p
            JOIN stock s ON p.id_producto = s.id_producto
        """)
        resultados = cursor.fetchall()
        stock_list = []
        for row in resultados:
            stock_list.append(row)  # opcional: o crear StockVO(row[0], row[1], row[2])
        return stock_list
