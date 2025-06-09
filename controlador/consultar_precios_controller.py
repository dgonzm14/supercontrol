class ConsultarPreciosController:
    def __init__(self, producto_dao):
        self.producto_dao = producto_dao

    def obtener_productos(self):
        return self.producto_dao.obtener_todos()


    




