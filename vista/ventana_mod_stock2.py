# ventana_mod_stock.py
print("ventana_mod_stock2.py cargado correctamente")


from PyQt5 import QtWidgets
from controlador.modificar_stock import Ui_ModificarStockWindow
import pyodbc

class VentanaModificarStock(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ModificarStockWindow()
        self.ui.setupUi(self)

        # Conecta botones
        self.ui.btn_modificar.clicked.connect(self.modificar_stock)
        self.ui.btn_volver.clicked.connect(self.volver)
        self.ui.btn_salir.clicked.connect(QtWidgets.qApp.quit)

        # Carga productos en el combo
        self.productos = []
        self.cargar_productos()

    def conectar(self):
        return pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=GOXUEL\\SQLEXPRESS;'
            'DATABASE=SuperControl;'
            'Trusted_Connection=yes;'
        )

    def cargar_productos(self):
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT id_producto, nombre_producto FROM productos ORDER BY nombre_producto")
            rows = cursor.fetchall()
            conn.close()

            self.ui.combo_productos.clear()
            self.productos = []
            for prod_id, prod_name in rows:
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
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM stock WHERE id_producto = ?", (prod_id,))
            exists = cursor.fetchone()[0] > 0

            if exists:
                cursor.execute("UPDATE stock SET cantidad = ? WHERE id_producto = ?", (nueva_cant, prod_id))
            else:
                cursor.execute("INSERT INTO stock (id_producto, cantidad) VALUES (?, ?)", (prod_id, nueva_cant))

            conn.commit()
            conn.close()

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





