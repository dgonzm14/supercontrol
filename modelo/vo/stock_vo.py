# modelo/stock_vo.py
class StockVO:
    def __init__(self, nombre_producto, cantidad, descripcion):
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.descripcion = descripcion
