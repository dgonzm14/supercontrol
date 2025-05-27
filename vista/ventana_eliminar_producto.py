from PyQt5 import QtWidgets
from controlador.eliminar_producto import Ui_EliminarProductoWindow

class VentanaEliminarProducto(QtWidgets.QDialog):
    def __init__(self, parent=None, conexion=None):
        super().__init__(parent)
        self.ui = Ui_EliminarProductoWindow()
        self.ui.setupUi(self)

        self.conexion = conexion
        self.parent = parent

        self.ui.btn_volver.clicked.connect(self.volver)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_producto)

        self.productos = {}  # nombre: id
        self.cargar_productos()

    def cargar_productos(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT id_producto, nombre_producto FROM productos")
            productos = cursor.fetchall()

            self.ui.combo_productos.clear()
            self.productos.clear()

            for id_producto, nombre in productos:
                self.productos[nombre] = id_producto
                self.ui.combo_productos.addItem(nombre)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo cargar productos:\n{e}")

    def eliminar_producto(self):
        nombre_seleccionado = self.ui.combo_productos.currentText()
        if not nombre_seleccionado:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Debes seleccionar un producto.")
            return

        id_producto = self.productos.get(nombre_seleccionado)

        try:
            cursor = self.conexion.cursor()

            # Verificar filas dependientes antes de eliminar
            cursor.execute("SELECT COUNT(*) FROM detalle_ventas WHERE id_producto = ?", (id_producto,))
            count_detalle = cursor.fetchone()[0]
            print(f"Filas en detalle_ventas a borrar: {count_detalle}")

            cursor.execute("SELECT COUNT(*) FROM precios WHERE id_producto = ?", (id_producto,))
            count_precios = cursor.fetchone()[0]
            print(f"Filas en precios a borrar: {count_precios}")

            cursor.execute("SELECT COUNT(*) FROM stock WHERE id_producto = ?", (id_producto,))
            count_stock = cursor.fetchone()[0]
            print(f"Filas en stock a borrar: {count_stock}")

            # Borrar dependencias
            cursor.execute("DELETE FROM detalle_ventas WHERE id_producto = ?", (id_producto,))
            self.conexion.commit()

            cursor.execute("DELETE FROM precios WHERE id_producto = ?", (id_producto,))
            self.conexion.commit()

            cursor.execute("DELETE FROM stock WHERE id_producto = ?", (id_producto,))
            self.conexion.commit()

            # Finalmente borrar el producto
            cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id_producto,))
            self.conexion.commit()

            QtWidgets.QMessageBox.information(self, "Éxito", f"Producto '{nombre_seleccionado}' eliminado correctamente.")
            self.cargar_productos()
        except Exception as e:
            self.conexion.rollback()
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo eliminar el producto:\n{e}")

    def volver(self):
        self.close()
        if self.parent:
            self.parent.show()




