class ValorStockController:
    def __init__(self, logic_valor_stock):
        self.logic = logic_valor_stock

    def calcular_valor_total(self):
        try:
            return self.logic.calcular_valor_total()
        except Exception as e:
            raise e

