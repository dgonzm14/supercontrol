from PyQt5 import QtWidgets

class VentanaConsultarPrecios(QtWidgets.QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller

        self.tabla_precios = QtWidgets.QTableWidget(self)
        self.tabla_precios.setColumnCount(3)
        self.tabla_precios.setHorizontalHeaderLabels(["Nombre", "Descripción", "Precio"])

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.tabla_precios)

        self.cargar_datos()

    def cargar_datos(self):
        try:
            productos = self.controller.obtener_productos()
            self.tabla_precios.setRowCount(len(productos))
            for fila, producto in enumerate(productos):
                self.tabla_precios.setItem(fila, 0, QtWidgets.QTableWidgetItem(producto.nombre))
                self.tabla_precios.setItem(fila, 1, QtWidgets.QTableWidgetItem(producto.descripcion))
                self.tabla_precios.setItem(fila, 2, QtWidgets.QTableWidgetItem(f"{producto.precio:.2f}"))

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"No se pudo cargar los precios:\n{str(e)}")















