# controlador/consultar_stock_controller.py
from modelo.dao.stock_dao import StockDAO

class ConsultarStockController:
    def __init__(self, conexion):
        self.dao = StockDAO(conexion)

    def obtener_stock(self):
        return self.dao.obtener_todo_stock()
