# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aniadir_producto.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AniadirProductoDialog(object):
    def setupUi(self, AniadirProductoDialog):
        AniadirProductoDialog.setObjectName("AniadirProductoDialog")
        AniadirProductoDialog.resize(300, 140)
        self.verticalLayout = QtWidgets.QVBoxLayout(AniadirProductoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_nombre = QtWidgets.QLabel(AniadirProductoDialog)
        self.label_nombre.setObjectName("label_nombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nombre)
        self.line_nombre = QtWidgets.QLineEdit(AniadirProductoDialog)
        self.line_nombre.setObjectName("line_nombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_nombre)
        self.label_descripcion = QtWidgets.QLabel(AniadirProductoDialog)
        self.label_descripcion.setObjectName("label_descripcion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_descripcion)
        self.line_descripcion = QtWidgets.QLineEdit(AniadirProductoDialog)
        self.line_descripcion.setObjectName("line_descripcion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_descripcion)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")
        self.btn_agregar = QtWidgets.QPushButton(AniadirProductoDialog)
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout_buttons.addWidget(self.btn_agregar)
        self.btn_cancelar = QtWidgets.QPushButton(AniadirProductoDialog)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_buttons.addWidget(self.btn_cancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_buttons)

        self.retranslateUi(AniadirProductoDialog)
        QtCore.QMetaObject.connectSlotsByName(AniadirProductoDialog)

    def retranslateUi(self, AniadirProductoDialog):
        _translate = QtCore.QCoreApplication.translate
        AniadirProductoDialog.setWindowTitle(_translate("AniadirProductoDialog", "Añadir Nuevo Producto"))
        self.label_nombre.setText(_translate("AniadirProductoDialog", "Nombre:"))
        self.label_descripcion.setText(_translate("AniadirProductoDialog", "Descripción:"))
        self.btn_agregar.setText(_translate("AniadirProductoDialog", "Agregar"))
        self.btn_cancelar.setText(_translate("AniadirProductoDialog", "Cancelar"))
