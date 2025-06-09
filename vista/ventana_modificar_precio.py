from PyQt5 import QtWidgets
from vista.modificar_precio import Ui_ModificarPrecioWindow

class VentanaModificarPrecio(QtWidgets.QDialog):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_ModificarPrecioWindow()
        self.ui.setupUi(self)
        self.controller = controller

        self.ui.btn_salir.clicked.connect(QtWidgets.qApp.quit)
        self.ui.btn_volver.clicked.connect(self.volver)
        self.ui.btn_actualizar.clicked.connect(self.actualizar_precio)

        self.productos = []
        self.cargar_productos()

    def cargar_productos(self):
        try:
            self.productos = self.controller.obtener_productos()
            self.ui.tabla_precios.setRowCount(len(self.productos))
            self.ui.tabla_precios.setColumnCount(3)
            self.ui.tabla_precios.setHorizontalHeaderLabels(["Nombre", "Descripción", "Precio actual"])

            for fila, (idp, nombre, descripcion, precio) in enumerate(self.productos):
                self.ui.tabla_precios.setItem(fila, 0, QtWidgets.QTableWidgetItem(nombre))
                self.ui.tabla_precios.setItem(fila, 1, QtWidgets.QTableWidgetItem(descripcion))
                self.ui.tabla_precios.setItem(fila, 2, QtWidgets.QTableWidgetItem(f"{precio:.2f}"))

            self.ui.tabla_precios.resizeColumnsToContents()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudieron cargar los productos:\n{e}")

    def actualizar_precio(self):
        fila = self.ui.tabla_precios.currentRow()
        if fila < 0:
            QtWidgets.QMessageBox.warning(self, "Selección requerida", "Selecciona un producto de la tabla.")
            return

        nuevo_precio_texto = self.ui.line_nuevo_precio.text().strip()
        if not nuevo_precio_texto:
            QtWidgets.QMessageBox.warning(self, "Campo vacío", "Ingresa un nuevo precio.")
            return

        try:
            nuevo_precio = float(nuevo_precio_texto)
            if nuevo_precio <= 0:
                raise ValueError("El precio debe ser positivo.")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Valor inválido", "Ingresa un número válido para el precio.")
            return

        id_producto = self.productos[fila][0]

        exito, mensaje = self.controller.actualizar_precio(id_producto, nuevo_precio)
        if exito:
            QtWidgets.QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_productos()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", mensaje)

    def volver(self):
        self.close()


