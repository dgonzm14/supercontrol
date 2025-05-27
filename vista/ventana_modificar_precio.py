from PyQt5 import QtWidgets
from controlador.modificar_precio import Ui_ModificarPrecioWindow
import pyodbc

class VentanaModificarPrecio(QtWidgets.QDialog):
    def __init__(self, parent=None, conexion=None):
        super().__init__(parent)
        self.ui = Ui_ModificarPrecioWindow()
        self.ui.setupUi(self)
        self.conn = conexion

        self.ui.btn_salir.clicked.connect(QtWidgets.qApp.quit)
        self.ui.btn_volver.clicked.connect(self.volver)
        self.ui.btn_actualizar.clicked.connect(self.actualizar_precio)

        self.productos = []  
        self.cargar_productos()

    def cargar_productos(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id_producto, nombre_producto, descripcion_producto, precio FROM productos")
            self.productos = cursor.fetchall()

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
                raise ValueError("Precio no válido")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Formato incorrecto", "El precio debe ser un número decimal mayor a 0.")
            return

        id_producto = self.productos[fila][0]  

        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE productos SET precio = ? WHERE id_producto = ?", (nuevo_precio, id_producto))
            self.conn.commit()
            QtWidgets.QMessageBox.information(self, "Éxito", "Precio actualizado correctamente.")
            self.ui.line_nuevo_precio.clear()
            self.cargar_productos()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo actualizar el precio:\n{e}")

    def volver(self):
        self.close()
        if self.parent():
            self.parent().show()
