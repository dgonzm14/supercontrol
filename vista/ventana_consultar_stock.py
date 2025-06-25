from PyQt5 import QtWidgets
from vista.consultar_stock import Ui_ConsultarStockWindow  

class VentanaConsultarStock(QtWidgets.QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.ui = Ui_ConsultarStockWindow()
        self.ui.setupUi(self)

        self.controlador = controller

        self.ui.btn_volver.clicked.connect(self.volver_a_cliente)
        self.ui.btn_salir.clicked.connect(QtWidgets.qApp.quit)

        self.cargar_datos()

    def cargar_datos(self):
        try:
            resultados = self.controlador.obtener_stock()
            self.ui.tabla_stock.setColumnCount(3)
            self.ui.tabla_stock.setHorizontalHeaderLabels(["Producto", "Stock", "Descripción"])
            self.ui.tabla_stock.setRowCount(len(resultados))

            for fila, datos in enumerate(resultados):
                for columna, valor in enumerate(datos):
                    item = QtWidgets.QTableWidgetItem(str(valor))
                    self.ui.tabla_stock.setItem(fila, columna, item)

            self.ui.tabla_stock.resizeColumnsToContents()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo cargar el stock:\n{e}")

    def volver_a_cliente(self):
        self.close()
        if self.parent():
            self.parent().show()









