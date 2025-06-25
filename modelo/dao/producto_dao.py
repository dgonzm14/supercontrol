from modelo.vo.producto_vo import ProductoVO
from modelo.sqlserver_db import SqlServerDatabase

class ProductoDAO:
    def __init__(self, conexion):  # Recibe la conexión como parámetro
        self.conn = conexion

    def agregar_producto(self, producto_vo):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO productos (nombre_producto, descripcion_producto, precio) VALUES (?, ?, ?)",
                (producto_vo.nombre, producto_vo.descripcion, producto_vo.precio)
            )
            self.conn.commit()

            cursor.execute("SELECT @@IDENTITY")
            producto_vo.id_producto = cursor.fetchone()[0]
            return producto_vo.id_producto

        except Exception as e:
            self.conn.rollback()
            raise e

    def obtener_todos(self):
        productos = []
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id_producto, nombre_producto, descripcion_producto, precio
            FROM productos
        """)
        resultados = cursor.fetchall()
        for fila in resultados:
            producto = ProductoVO(
                id_producto=fila[0],
                nombre=fila[1],
                descripcion=fila[2],
                precio=float(fila[3]) if fila[3] is not None else 0.0
            )
            productos.append(producto)
        return productos









