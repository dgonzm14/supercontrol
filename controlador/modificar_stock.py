# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificar_stock.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModificarStockWindow(object):
    def setupUi(self, ModificarStockWindow):
        ModificarStockWindow.setObjectName("ModificarStockWindow")
        ModificarStockWindow.resize(400, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(ModificarStockWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_titulo = QtWidgets.QLabel(ModificarStockWindow)
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo.setFont(font)
        self.label_titulo.setObjectName("label_titulo")
        self.verticalLayout.addWidget(self.label_titulo)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_producto = QtWidgets.QLabel(ModificarStockWindow)
        self.label_producto.setObjectName("label_producto")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_producto)
        self.combo_productos = QtWidgets.QComboBox(ModificarStockWindow)
        self.combo_productos.setObjectName("combo_productos")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_productos)
        self.label_cantidad = QtWidgets.QLabel(ModificarStockWindow)
        self.label_cantidad.setObjectName("label_cantidad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_cantidad)
        self.spin_cantidad = QtWidgets.QSpinBox(ModificarStockWindow)
        self.spin_cantidad.setMinimum(0)
        self.spin_cantidad.setMaximum(100000)
        self.spin_cantidad.setObjectName("spin_cantidad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spin_cantidad)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_modificar = QtWidgets.QPushButton(ModificarStockWindow)
        self.btn_modificar.setObjectName("btn_modificar")
        self.horizontalLayout.addWidget(self.btn_modificar)
        self.btn_volver = QtWidgets.QPushButton(ModificarStockWindow)
        self.btn_volver.setObjectName("btn_volver")
        self.horizontalLayout.addWidget(self.btn_volver)
        self.btn_salir = QtWidgets.QPushButton(ModificarStockWindow)
        self.btn_salir.setObjectName("btn_salir")
        self.horizontalLayout.addWidget(self.btn_salir)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ModificarStockWindow)
        QtCore.QMetaObject.connectSlotsByName(ModificarStockWindow)

    def retranslateUi(self, ModificarStockWindow):
        _translate = QtCore.QCoreApplication.translate
        ModificarStockWindow.setWindowTitle(_translate("ModificarStockWindow", "Modificar Stock"))
        self.label_titulo.setText(_translate("ModificarStockWindow", "Modificar Stock de Producto"))
        self.label_producto.setText(_translate("ModificarStockWindow", "Producto:"))
        self.label_cantidad.setText(_translate("ModificarStockWindow", "Nueva Cantidad:"))
        self.btn_modificar.setText(_translate("ModificarStockWindow", "Modificar"))
        self.btn_volver.setText(_translate("ModificarStockWindow", "Volver"))
        self.btn_salir.setText(_translate("ModificarStockWindow", "Salir"))
