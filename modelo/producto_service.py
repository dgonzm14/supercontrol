from modelo.dao.producto_dao import ProductoDAO
from modelo.vo.producto_vo import ProductoVO

class ProductoService:
    def __init__(self, dao):
        self.dao = dao  

    def agregar_producto(self, nombre, descripcion):
        if not nombre or not descripcion:
            return False, "Por favor completa nombre y descripción."

        producto = ProductoVO(nombre.strip(), descripcion.strip(), precio=1.00)

        try:
            self.dao.agregar_producto(producto)
            return True, "Producto agregado correctamente con precio predeterminado 1.00."
        except Exception as e:
            return False, f"No se pudo agregar el producto:\n{e}"



