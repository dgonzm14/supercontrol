from PyQt5 import QtWidgets
from vista.modificar_stock import Ui_ModificarStockWindow

class VentanaModificarStockModStock(QtWidgets.QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.ui = Ui_ModificarStockWindow()
        self.ui.setupUi(self)

        self.controller = controller

        self.ui.btn_modificar.clicked.connect(self.modificar_stock)
        self.ui.btn_volver.clicked.connect(self.volver)
        self.ui.btn_salir.clicked.connect(QtWidgets.qApp.quit)

        self.productos = []
        self.cargar_productos()

    def cargar_productos(self):
        try:
            productos = self.controller.obtener_productos()
            self.ui.combo_productos.clear()
            self.productos = []
            for prod_id, prod_name in productos:
                self.productos.append((prod_id, prod_name))
                self.ui.combo_productos.addItem(prod_name)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudieron cargar productos:\n{e}")

    def modificar_stock(self):
        idx = self.ui.combo_productos.currentIndex()
        if idx < 0:
            return
        prod_id, prod_name = self.productos[idx]
        nueva_cant = self.ui.spin_cantidad.value()

        try:
            self.controller.modificar_stock(prod_id, nueva_cant)
            QtWidgets.QMessageBox.information(
                self, "Éxito",
                f"Stock de '{prod_name}' actualizado a {nueva_cant}."
            )
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo modificar el stock:\n{e}")

    def volver(self):
        self.close()
        if self.parent():
            self.parent().show()








