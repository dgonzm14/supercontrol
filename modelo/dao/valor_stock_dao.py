class ValorStockDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_valor_total_stock(self):
        cursor = self.conexion.cursor()
        query = """
            SELECT SUM(p.precio * s.cantidad) AS valor_total
            FROM productos p
            JOIN stock s ON p.id_producto = s.id_producto
        """
        cursor.execute(query)
        resultado = cursor.fetchone()
        valor_total = resultado.valor_total if resultado and resultado.valor_total is not None else 0.0
        return valor_total
