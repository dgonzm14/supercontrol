class ValorStockController:
    def __init__(self, dao_valor_stock):
        self.dao = dao_valor_stock

    def calcular_valor_total(self):
        try:
            return self.dao.obtener_valor_total_stock()
        except Exception as e:
            raise e
