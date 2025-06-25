class ConsultarStockController:
    def __init__(self, logic):
        self.logic = logic

    def obtener_stock(self):
        return self.logic.obtener_stock()



