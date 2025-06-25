class StockControllerModStock:
    def __init__(self, logic):
        self.logic = logic

    def obtener_productos(self):
        return self.logic.obtener_productos()

    def modificar_stock(self, id_producto, cantidad):
        self.logic.modificar_stock(id_producto, cantidad)





