from modelo.dao.producto_dao import ProductoDAO

class ProductoLogic:
    def __init__(self, conexion):
        self.dao = ProductoDAO(conexion)

    def obtener_todos(self):
        return self.dao.obtener_todos()
