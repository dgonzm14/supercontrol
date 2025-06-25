from PyQt5 import QtWidgets
from vista.aniadir_producto import Ui_AniadirProductoDialog
from controlador.aniadir_producto import AniadirProductoController
from modelo.producto_service import ProductoService
from modelo.dao.producto_dao import ProductoDAO

class VentanaAniadirProducto(QtWidgets.QDialog):
    def __init__(self, parent=None, conexion=None):
        super().__init__(parent)
        self.ui = Ui_AniadirProductoDialog()
        self.ui.setupUi(self)

        
        dao = ProductoDAO(conexion)
        service = ProductoService(dao)
        self.controller = AniadirProductoController(service)

        self.ui.btn_agregar.clicked.connect(self.agregar_producto)
        self.ui.btn_cancelar.clicked.connect(self.close)

    def agregar_producto(self):
        nombre = self.ui.line_nombre.text()
        descripcion = self.ui.line_descripcion.text()

        exito, mensaje = self.controller.agregar_producto(nombre, descripcion)

        if exito:
            QtWidgets.QMessageBox.information(self, "Éxito", mensaje)
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", mensaje)












