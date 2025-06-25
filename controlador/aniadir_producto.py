class AniadirProductoController:
    def __init__(self, service):  
        self.service = service

    def agregar_producto(self, nombre, descripcion):
        return self.service.agregar_producto(nombre, descripcion)






