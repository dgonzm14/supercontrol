class ConsultarPreciosController:
    def __init__(self, producto_logic):
        self.producto_logic = producto_logic

    def obtener_productos(self):
        return self.producto_logic.obtener_todos()



    




