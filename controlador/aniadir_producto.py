from modelo.vo.producto_vo import ProductoVO
from modelo.dao.producto_dao import ProductoDAO

class AniadirProductoController:
    def __init__(self, conexion):
        self.conn = conexion
        self.dao = ProductoDAO(conexion)

    def agregar_producto(self, nombre, descripcion):
        if not nombre or not descripcion:
            return False, "Por favor completa nombre y descripción."

        producto = ProductoVO(nombre.strip(), descripcion.strip())

        try:
            self.dao.agregar_producto(producto)
            return True, "Producto agregado correctamente con precio predeterminado 1.00."
        except Exception as e:
            return False, f"No se pudo agregar el producto:\n{e}"

