from PyQt5 import QtWidgets
from .eliminar_producto import Ui_EliminarProductoWindow
from controlador.eliminar_producto_controller import EliminarProductoController
from modelo.eliminar_producto_logic import EliminarProductoLogic
from modelo.dao.eliminar_producto_dao import EliminarProductoDAO  

class VentanaEliminarProducto(QtWidgets.QDialog):
    def __init__(self, parent=None, conexion=None):
        super().__init__(parent)
        self.ui = Ui_EliminarProductoWindow()
        self.ui.setupUi(self)

        self.dao = EliminarProductoDAO(conexion)
        self.logic = EliminarProductoLogic(self.dao)
        self.controller = EliminarProductoController(self.logic)

        self.cargar_productos()

        self.ui.btn_eliminar.clicked.connect(self.eliminar_producto)
        self.ui.btn_volver.clicked.connect(self.close)

    def cargar_productos(self):
        exito, resultado = self.controller.cargar_productos()
        if exito:
            self.ui.combo_productos.clear()
            self.ui.combo_productos.addItems(resultado)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", resultado)

    def eliminar_producto(self):
        nombre = self.ui.combo_productos.currentText()
        exito, mensaje = self.controller.eliminar_producto(nombre)
        if exito:
            QtWidgets.QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_productos()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", mensaje)














