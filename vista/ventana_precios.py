

from PyQt5 import QtWidgets
from controlador.consultar_precios import Ui_ConsultarPreciosWindow
import pyodbc

class VentanaConsultarPrecios(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ConsultarPreciosWindow()
        self.ui.setupUi(self)

        self.ui.btn_volver.clicked.connect(self.volver)
        self.ui.btn_salir.clicked.connect(QtWidgets.qApp.quit)

        self.cargar_datos()

    def cargar_datos(self):
        try:
            conn = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=GOXUEL\\SQLEXPRESS;'
                'DATABASE=SuperControl;'
                'Trusted_Connection=yes;'
            )
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT nombre_producto AS Producto, precio AS Precio
                FROM productos
            """)
            resultados = cursor.fetchall()

            self.ui.tabla_precios.setColumnCount(2)
            self.ui.tabla_precios.setHorizontalHeaderLabels(["Producto", "Precio"])
            self.ui.tabla_precios.setRowCount(len(resultados))

            for fila, datos in enumerate(resultados):
                for columna, valor in enumerate(datos):
                    item = QtWidgets.QTableWidgetItem(str(valor))
                    self.ui.tabla_precios.setItem(fila, columna, item)

            self.ui.tabla_precios.resizeColumnsToContents()
            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo cargar los precios:\n{e}"
            )

    def volver(self):
        self.close()
        if self.parent():
            self.parent().show()









