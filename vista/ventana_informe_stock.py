import csv
from PyQt5 import QtWidgets
from vista.informe_stock import Ui_InformeStockWindow

class VentanaInformeStock(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InformeStockWindow()
        self.ui.setupUi(self)

    def set_column_headers(self, headers):
        self.ui.tabla_stock.setColumnCount(len(headers))
        self.ui.tabla_stock.setHorizontalHeaderLabels(headers)

    def mostrar_datos(self, datos):
        self.ui.tabla_stock.setRowCount(len(datos))
        for fila, fila_datos in enumerate(datos):
            for col, valor in enumerate(fila_datos):
                item = QtWidgets.QTableWidgetItem(str(valor if valor is not None else ""))
                self.ui.tabla_stock.setItem(fila, col, item)
        self.ui.tabla_stock.resizeColumnsToContents()

    def on_exportar(self, callback):
        self.ui.btn_exportar.clicked.connect(callback)

    def on_cerrar(self, callback):
        self.ui.btn_cerrar.clicked.connect(callback)

    def obtener_ruta_guardado(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Guardar informe como CSV", "", "CSV Files (*.csv)")
        return path

    def obtener_datos_tabla(self):
        datos = []
        for fila in range(self.ui.tabla_stock.rowCount()):
            fila_datos = []
            for col in range(self.ui.tabla_stock.columnCount()):
                item = self.ui.tabla_stock.item(fila, col)
                fila_datos.append(item.text() if item else "")
            datos.append(fila_datos)
        return datos

    def exportar_a_csv(self, path, datos):
        with open(path, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Nombre", "Precio", "Descripción", "Stock"])
            writer.writerows(datos)

    def mostrar_error(self, mensaje):
        QtWidgets.QMessageBox.critical(self, "Error", mensaje)

    def mostrar_info(self, titulo, mensaje):
        QtWidgets.QMessageBox.information(self, titulo, mensaje)

