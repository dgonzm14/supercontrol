from modelo.dao.stock_dao_modstock import StockDAOModStock

class StockControllerModStock:
    def __init__(self, conexion):
        self.dao = StockDAOModStock(conexion)

    def obtener_productos(self):
        return self.dao.obtener_productos()

    def modificar_stock(self, id_producto, cantidad):
        self.dao.actualizar_stock(id_producto, cantidad)



