import csv
from PyQt5 import QtWidgets
from informe_stock import Ui_InformeStockWindow  # tu archivo generado

class VentanaInformeStock(QtWidgets.QDialog):
    def __init__(self, parent=None, conexion=None):
        super().__init__(parent)
        self.ui = Ui_InformeStockWindow()
        self.ui.setupUi(self)
        self.conn = conexion

        # Configurar tabla
        self.ui.tabla_stock.setColumnCount(4)
        self.ui.tabla_stock.setHorizontalHeaderLabels(["Nombre", "Precio", "Descripción", "Stock"])

        # Conectar botones
        self.ui.btn_exportar.clicked.connect(self.exportar_csv)
        self.ui.btn_cerrar.clicked.connect(self.close)

        # Cargar datos
        self.cargar_datos()

    def cargar_datos(self):
        try:
            cursor = self.conn.cursor()
            # Consulta que junta productos con stock
            cursor.execute("""
                SELECT p.nombre_producto, p.precio, p.descripcion_producto, 
                       ISNULL(s.cantidad, 0) as stock
                FROM productos p
                LEFT JOIN stock s ON p.id_producto = s.id_producto
            """)
            datos = cursor.fetchall()

            self.ui.tabla_stock.setRowCount(len(datos))
            for fila, (nombre, precio, descripcion, stock) in enumerate(datos):
                self.ui.tabla_stock.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(nombre)))
                self.ui.tabla_stock.setItem(fila, 1, QtWidgets.QTableWidgetItem(f"{precio:.2f}" if precio is not None else "0.00"))
                self.ui.tabla_stock.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(descripcion) if descripcion else ""))
                self.ui.tabla_stock.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(stock)))

            self.ui.tabla_stock.resizeColumnsToContents()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo cargar el informe:\n{e}")

    def exportar_csv(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Guardar informe como CSV", "", "CSV Files (*.csv)")
        if not path:
            return
        try:
            with open(path, mode='w', newline='', encoding='utf-8') as archivo:
                writer = csv.writer(archivo)
                # Escribir encabezado
                writer.writerow(["Nombre", "Precio", "Descripción", "Stock"])
                # Escribir filas
                for fila in range(self.ui.tabla_stock.rowCount()):
                    rowdata = []
                    for col in range(self.ui.tabla_stock.columnCount()):
                        item = self.ui.tabla_stock.item(fila, col)
                        rowdata.append(item.text() if item else "")
                    writer.writerow(rowdata)
            QtWidgets.QMessageBox.information(self, "Éxito", "Informe exportado correctamente.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo exportar el informe:\n{e}")
