from PyQt5 import QtWidgets
from controlador.aniadir_producto import Ui_AniadirProductoDialog

class VentanaAniadirProducto(QtWidgets.QDialog):
    def __init__(self, parent=None, conexion=None):
        super().__init__(parent)
        self.ui = Ui_AniadirProductoDialog()
        self.ui.setupUi(self)

        self.conn = conexion

        self.ui.btn_agregar.clicked.connect(self.agregar_producto)
        self.ui.btn_cancelar.clicked.connect(self.close)

    def agregar_producto(self):
        nombre = self.ui.line_nombre.text().strip()
        descripcion = self.ui.line_descripcion.text().strip()

        if not nombre or not descripcion:
            QtWidgets.QMessageBox.warning(self, "Campos incompletos", "Por favor completa nombre y descripción.")
            return

        try:
            cursor = self.conn.cursor()

            
            cursor.execute(
                "INSERT INTO productos (nombre_producto, descripcion_producto) VALUES (?, ?)",
                (nombre, descripcion)
            )
            self.conn.commit()

           
            cursor.execute("SELECT @@IDENTITY")
            id_producto = cursor.fetchone()[0]

            
            cursor.execute(
                "INSERT INTO precios (id_producto, precio) VALUES (?, ?)",
                (id_producto, 1.00)
            )
            self.conn.commit()

            QtWidgets.QMessageBox.information(self, "Éxito", "Producto agregado correctamente con precio predeterminado 1.00.")
            self.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo agregar el producto:\n{e}")







