from modelo.stock_logic import StockLogic

class ConsultarStockController:
    def __init__(self, conexion):
        self.logic = StockLogic(conexion)

    def obtener_stock(self):
        return self.logic.obtener_stock()

