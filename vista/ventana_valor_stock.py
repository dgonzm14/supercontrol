from PyQt5 import QtWidgets, QtCore
import pyodbc  

class VentanaValorStock(QtWidgets.QDialog):
    def __init__(self, conexion, parent=None):  
        super().__init__(parent)               
        self.conexion = conexion
        self.setWindowTitle("Valor Total del Stock")
        self.resize(400, 150)

        
        layout = QtWidgets.QVBoxLayout()

        
        self.boton_calcular = QtWidgets.QPushButton("Calcular valor total del stock")
        layout.addWidget(self.boton_calcular)

        
        self.label_resultado = QtWidgets.QLabel("Valor total del stock: ")
        self.label_resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultado.setMinimumHeight(40)
        layout.addWidget(self.label_resultado)

        self.setLayout(layout)

        
        self.boton_calcular.clicked.connect(self.calcular_valor_stock)

    def calcular_valor_stock(self):
        try:
            cursor = self.conexion.cursor()
            query = """
            SELECT SUM(p.precio * s.cantidad) AS valor_total
            FROM productos p
            JOIN stock s ON p.id_producto = s.id_producto
            """
            cursor.execute(query)
            resultado = cursor.fetchone()

            valor_total = resultado.valor_total if resultado and resultado.valor_total is not None else 0.0
            self.label_resultado.setText(f"Valor total del stock: ${valor_total:.2f}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo calcular el valor del stock:\n{e}")

