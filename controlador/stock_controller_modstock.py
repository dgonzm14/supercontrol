from modelo.stock_logic_modstock import StockLogicModStock

class StockControllerModStock:
    def __init__(self, conexion):
        self.logic = StockLogicModStock(conexion)

    def obtener_productos(self):
        return self.logic.obtener_productos()

    def modificar_stock(self, id_producto, cantidad):
        self.logic.modificar_stock(id_producto, cantidad)




