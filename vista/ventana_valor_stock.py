from PyQt5 import QtWidgets, QtCore

class VentanaValorStock(QtWidgets.QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
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
            valor_total = self.controller.calcular_valor_total()
            self.label_resultado.setText(f"Valor total del stock: ${valor_total:.2f}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo calcular el valor del stock:\n{e}")


