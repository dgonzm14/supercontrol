from modelo.dao.stock_dao import StockDAO

class StockLogic:
    def __init__(self, conexion):
        self.dao = StockDAO(conexion)

    def obtener_stock(self):
        return self.dao.obtener_todo_stock()
