# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 583)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 451, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_usuario = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_usuario.setObjectName("label_usuario")
        self.verticalLayout.addWidget(self.label_usuario)
        self.line_usuario = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_usuario.setText("")
        self.line_usuario.setObjectName("line_usuario")
        self.verticalLayout.addWidget(self.line_usuario)
        self.label_contrasena = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_contrasena.setObjectName("label_contrasena")
        self.verticalLayout.addWidget(self.label_contrasena)
        self.line_contrasena = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_contrasena.setText("")
        self.line_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_contrasena.setObjectName("line_contrasena")
        self.verticalLayout.addWidget(self.line_contrasena)
        self.label_nombre = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_nombre.setObjectName("label_nombre")
        self.verticalLayout.addWidget(self.label_nombre)
        self.line_nombre = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_nombre.setText("")
        self.line_nombre.setObjectName("line_nombre")
        self.verticalLayout.addWidget(self.line_nombre)
        self.label_nombre_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_nombre_2.setObjectName("label_nombre_2")
        self.verticalLayout.addWidget(self.label_nombre_2)
        self.line_apellidos = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_apellidos.setText("")
        self.line_apellidos.setObjectName("line_apellidos")
        self.verticalLayout.addWidget(self.line_apellidos)
        self.label_nombre_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_nombre_3.setObjectName("label_nombre_3")
        self.verticalLayout.addWidget(self.label_nombre_3)
        self.line_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_email.setText("")
        self.line_email.setObjectName("line_email")
        self.verticalLayout.addWidget(self.line_email)
        self.label_nombre_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_nombre_4.setObjectName("label_nombre_4")
        self.verticalLayout.addWidget(self.label_nombre_4)
        self.line_telefono = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_telefono.setText("")
        self.line_telefono.setObjectName("line_telefono")
        self.verticalLayout.addWidget(self.line_telefono)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.combo_rol = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combo_rol.setObjectName("combo_rol")
        self.combo_rol.addItem("")
        self.combo_rol.addItem("")
        self.combo_rol.addItem("")
        self.verticalLayout.addWidget(self.combo_rol)
        self.btn_registrar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_registrar.setObjectName("btn_registrar")
        self.verticalLayout.addWidget(self.btn_registrar)
        self.btn_volver = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_volver.setObjectName("btn_volver")
        self.verticalLayout.addWidget(self.btn_volver)
        self.btn_salir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_salir.setObjectName("btn_salir")
        self.verticalLayout.addWidget(self.btn_salir)
        self.label_mensaje = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_mensaje.setObjectName("label_mensaje")
        self.verticalLayout.addWidget(self.label_mensaje)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(360, 50, 159, 118))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_usuario.setText(_translate("Dialog", "Usuario"))
        self.label_contrasena.setText(_translate("Dialog", "Contraseña"))
        self.label_nombre.setText(_translate("Dialog", "Nombre"))
        self.label_nombre_2.setText(_translate("Dialog", "Apellidos"))
        self.label_nombre_3.setText(_translate("Dialog", "email"))
        self.label_nombre_4.setText(_translate("Dialog", "Número de Teléfono"))
        self.label_2.setText(_translate("Dialog", "Rol"))
        self.combo_rol.setItemText(0, _translate("Dialog", "Cliente"))
        self.combo_rol.setItemText(1, _translate("Dialog", "Empleado"))
        self.combo_rol.setItemText(2, _translate("Dialog", "Jefe"))
        self.btn_registrar.setText(_translate("Dialog", "Registrarse"))
        self.btn_volver.setText(_translate("Dialog", "Volver Atras"))
        self.btn_salir.setText(_translate("Dialog", "Salir"))
        self.label_mensaje.setText(_translate("Dialog", "Mensaje estado"))
