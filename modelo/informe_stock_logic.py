from modelo.dao.informe_stock_dao import InformeStockDAO

class InformeStockLogic:
    def __init__(self, dao: InformeStockDAO):
        self.dao = dao

    def obtener_datos_stock(self):
        return self.dao.obtener_datos_stock()



