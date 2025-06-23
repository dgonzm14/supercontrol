from modelo.dao.valor_stock_dao import ValorStockDAO

class ValorStockLogic:
    def __init__(self, conexion):
        self.dao = ValorStockDAO(conexion)

    def calcular_valor_total(self):
        try:
            return self.dao.obtener_valor_total_stock()
        except Exception as e:
            raise e
