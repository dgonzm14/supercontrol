from PyQt5 import QtCore, QtWidgets
from controlador.login import Ui_label_usuario
from controlador.registrar import Ui_Dialog


from controlador.cliente import Ui_ClienteWindow
from controlador.empleado import Ui_EmpleadoWindow
from controlador.jefe import Ui_JefeWindow


from vista.ventana_consultar_stock import VentanaConsultarStock
from vista.ventana_precios import VentanaConsultarPrecios
from vista.ventana_mod_stock2 import VentanaModificarStock
from vista.ventana_aniadir_producto import VentanaAniadirProducto
from vista.ventana_modificar_precio import VentanaModificarPrecio
from vista.ventana_informe_stock import VentanaInformeStock
from vista.ventana_valor_stock import VentanaValorStock


from modelo.sqlserver_db import SqlServerDatabase

class MainWindow(QtWidgets.QMainWindow, Ui_label_usuario):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        connection_string = (
            'DRIVER={SQL Server};'
            'SERVER=GOXUEL\\SQLEXPRESS;'
            'DATABASE=SuperControl;'
            'Trusted_Connection=yes;'
        )
        self.db = SqlServerDatabase(connection_string)
        self.db.connect()
        self.conn = self.db.get_connection()

        self.btn_login.clicked.connect(self.login)
        self.btn_registrar.clicked.connect(self.abrir_registro)
        self.btn_salir.clicked.connect(self.salir)

        self.ventana_rol = None

    def login(self):
        usuario = self.line_usuario.text()
        contrasena = self.line_contrasena.text()
        rol_combo = self.combo_rol.currentText()

        if not usuario or not contrasena:
            QtWidgets.QMessageBox.warning(self, "Campos vacíos", "Por favor, ingresa usuario y contraseña.")
            return

        cursor = self.conn.cursor()
        cursor.execute("SELECT id_usuario, rol FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contrasena))
        result = cursor.fetchone()
        if not result:
            QtWidgets.QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos.")
            return

        _, rol_registrado = result
        if rol_registrado.lower() != rol_combo.lower():
            QtWidgets.QMessageBox.critical(self, "Error", "El rol seleccionado no coincide con el registro.")
            return

        QtWidgets.QMessageBox.information(self, "Éxito", f"Bienvenido, {usuario}!")
        self.hide()
        self.abrir_ventana_rol(rol_registrado.lower())

    def abrir_ventana_rol(self, rol):
        if self.ventana_rol:
            self.ventana_rol.close()
            self.ventana_rol = None

        if rol == "cliente":
            self.ventana_rol = QtWidgets.QDialog(self)
            self.ui_rol = Ui_ClienteWindow()
            self.ui_rol.setupUi(self.ventana_rol)
            self.ui_rol.btn_consultar_stock.clicked.connect(self.consultar_stock)
            self.ui_rol.btn_consultar_precios.clicked.connect(self.consultar_precios)

        elif rol == "empleado":
            self.ventana_rol = QtWidgets.QDialog(self)
            self.ui_rol = Ui_EmpleadoWindow()
            self.ui_rol.setupUi(self.ventana_rol)
            self.ui_rol.btn_modificar_stock.clicked.connect(self.abrir_modificar_stock)
            self.ui_rol.btn_anadir_producto.clicked.connect(self.abrir_aniadir_producto)

        else:  
            self.ventana_rol = QtWidgets.QDialog(self)
            self.ui_rol = Ui_JefeWindow()
            self.ui_rol.setupUi(self.ventana_rol)
            self.ui_rol.btn_modificar_precio.clicked.connect(self.abrir_modificar_precio)
            self.ui_rol.btn_generar_informe_stock.clicked.connect(self.abrir_informe_stock)
            self.ui_rol.btn_calcular_valor_stock.clicked.connect(self.abrir_valor_stock)

        self.ui_rol.btn_volver.clicked.connect(self.volver_login_desde_rol)
        self.ui_rol.btn_salir.clicked.connect(self.salir)
        self.ventana_rol.show()

    def consultar_stock(self):
        ventana = VentanaConsultarStock(self)
        self.hide()
        ventana.exec_()
        self.show()

    def consultar_precios(self):
        ventana = VentanaConsultarPrecios(self)
        self.hide()
        ventana.exec_()
        self.show()

    def abrir_modificar_stock(self):
        ventana = VentanaModificarStock(self.ventana_rol)
        self.ventana_rol.hide()
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_aniadir_producto(self):
        self.ventana_rol.hide()
        ventana = VentanaAniadirProducto(parent=self, conexion=self.conn)
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_modificar_precio(self):
        self.ventana_rol.hide()
        ventana = VentanaModificarPrecio(parent=self, conexion=self.conn)
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_informe_stock(self):
        self.ventana_rol.hide()
        ventana = VentanaInformeStock(parent=self, conexion=self.conn)
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_valor_stock(self):
        self.ventana_rol.hide()
        ventana = VentanaValorStock(conexion=self.conn, parent=self)
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_registro(self):
        self.hide()
        self.dialog_registro = QtWidgets.QDialog(self)
        self.ui_registro = Ui_Dialog()
        self.ui_registro.setupUi(self.dialog_registro)
        self.ui_registro.btn_volver.clicked.connect(self.volver_login)
        self.ui_registro.btn_salir.clicked.connect(self.salir)
        self.ui_registro.btn_registrar.clicked.connect(self.registrar_usuario)
        self.dialog_registro.exec_()

    def registrar_usuario(self):
        campos = [
            self.ui_registro.line_nombre.text(),
            self.ui_registro.line_apellidos.text(),
            self.ui_registro.line_usuario.text(),
            self.ui_registro.line_contrasena.text(),
            self.ui_registro.line_email.text(),
            self.ui_registro.line_telefono.text(),
            self.ui_registro.combo_rol.currentText().lower(),
        ]
        if not all(campos):
            QtWidgets.QMessageBox.warning(self.dialog_registro, "Campos incompletos", "Completa todos los campos.")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre_usuario, apellido_usuario, usuario, contrasena, email_usuario, telefono_usuario, rol) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                campos
            )
            self.conn.commit()
            QtWidgets.QMessageBox.information(self.dialog_registro, "Registro exitoso", "Usuario registrado correctamente.")
            self.volver_login()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.dialog_registro, "Error", f"No se pudo registrar: {e}")

    def volver_login(self):
        self.dialog_registro.close()
        self.show()

    def volver_login_desde_rol(self):
        if self.ventana_rol:
            self.ventana_rol.hide()
            self.ventana_rol = None
        self.show()

    def salir(self):
        QtWidgets.QMessageBox.information(self, "Salir", "Saliendo de la aplicación.")
        QtCore.QCoreApplication.quit()

    def closeEvent(self, event):
        self.db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())
































































