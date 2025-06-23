from PyQt5 import QtCore, QtWidgets
from vista.login import Ui_label_usuario  
from vista.registrar import Ui_Dialog
from vista.cliente import Ui_ClienteWindow
from vista.empleado import Ui_EmpleadoWindow
from vista.jefe import Ui_JefeWindow

from controlador.login_controller import LoginController, RegistroController
from controlador.eliminar_producto_controller import EliminarProductoController
from controlador.informe_stock_controller import InformeStockController
from controlador.modificar_precio_controller import ModificarPrecioController

from controlador.consultar_precios_controller import ConsultarPreciosController
from vista.ventana_consultar_precios import VentanaConsultarPrecios

from vista.ventana_consultar_stock import VentanaConsultarStock
from vista.ventana_mod_stock_modstock import VentanaModificarStockModStock 

from vista.ventana_aniadir_producto import VentanaAniadirProducto
from vista.ventana_modificar_precio import VentanaModificarPrecio
from vista.ventana_informe_stock import VentanaInformeStock
from vista.ventana_valor_stock import VentanaValorStock
from vista.ventana_eliminar_producto import VentanaEliminarProducto

from vista.ventana_gestionar_usuarios import VentanaGestionarUsuarios

from modelo.dao.modificar_precio_dao import ModificarPrecioDAO

from modelo.producto_logic import ProductoLogic
from modelo.informe_stock_logic import InformeStockLogic
from modelo.modificar_precio_logic import ModificarPrecioLogic
from modelo.sqlserver_db import SqlServerDatabase

from modelo.usuario_logic import UsuarioLogic
from controlador.usuario_controller import UsuarioController

# Aquí importamos la lógica y el controlador para valor stock (lógica incluye DAO)
from modelo.valor_stock_logic import ValorStockLogic
from controlador.valor_stock_controller import ValorStockController


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

        self.login_controller = LoginController(self.conn)
        self.registro_controller = None

        self.btn_login.clicked.connect(self.login)
        self.btn_registrar.clicked.connect(self.abrir_registro)
        self.btn_salir.clicked.connect(self.salir)

        self.ventana_rol = None

    def login(self):
        usuario = self.line_usuario.text()
        contrasena = self.line_contrasena.text()
        rol_combo = self.combo_rol.currentText()

        exito, mensaje, rol = self.login_controller.login(usuario, contrasena, rol_combo)
        if not exito:
            QtWidgets.QMessageBox.warning(self, "Error", mensaje)
            return

        QtWidgets.QMessageBox.information(self, "Éxito", mensaje)
        self.hide()
        self.abrir_ventana_rol(rol)

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
            self.ventana_rol = QtWidgets.QMainWindow(self)
            self.ui_rol = Ui_EmpleadoWindow()
            self.ui_rol.setupUi(self.ventana_rol)

            self.ui_rol.btn_modificar_stock.clicked.connect(self.abrir_modificar_stock_modstock)
            self.ui_rol.btn_aniadir_producto.clicked.connect(self.abrir_aniadir_producto)
            self.ui_rol.btn_eliminar_producto.clicked.connect(self.abrir_eliminar_producto)

        else:  # jefe
            self.ventana_rol = QtWidgets.QDialog(self)
            self.ui_rol = Ui_JefeWindow()
            self.ui_rol.setupUi(self.ventana_rol)
            self.ui_rol.btn_modificar_precio.clicked.connect(self.abrir_modificar_precio)
            self.ui_rol.btn_generar_informe_stock.clicked.connect(self.abrir_informe_stock)
            self.ui_rol.btn_calcular_valor_stock.clicked.connect(self.abrir_valor_stock)
            self.ui_rol.btn_gestionar_usuarios.clicked.connect(self.abrir_gestionar_usuarios)

        self.ui_rol.btn_volver.clicked.connect(self.volver_login_desde_rol)
        self.ui_rol.btn_salir.clicked.connect(self.salir)
        self.ventana_rol.show()

    def consultar_stock(self):
        ventana = VentanaConsultarStock(self.conn, self)
        self.hide()
        ventana.exec_()
        self.show()

    def consultar_precios(self):
        producto_logic = ProductoLogic(self.conn)
        controlador = ConsultarPreciosController(producto_logic)
        ventana = VentanaConsultarPrecios(controller=controlador, parent=self)
        self.hide()
        ventana.exec_()
        self.show()

    def abrir_modificar_stock_modstock(self):
        from controlador.stock_controller_modstock import StockControllerModStock

        controller = StockControllerModStock(self.conn)
        ventana = VentanaModificarStockModStock(controller, parent=self.ventana_rol)
        self.ventana_rol.hide()
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_aniadir_producto(self):
        self.ventana_rol.hide()
        ventana = VentanaAniadirProducto(parent=self, conexion=self.conn)
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_eliminar_producto(self):
        self.ventana_rol.hide()
        ventana = VentanaEliminarProducto(parent=self.ventana_rol, conexion=self.conn)
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_modificar_precio(self):
        self.ventana_rol.hide()
        dao = ModificarPrecioDAO(self.conn)
        logic = ModificarPrecioLogic(dao)
        controller = ModificarPrecioController(logic)
        ventana = VentanaModificarPrecio(parent=self, controller=controller)
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_informe_stock(self):
        self.ventana_rol.hide()
        vista = VentanaInformeStock(parent=self)
        logic = InformeStockLogic(self.conn)
        controller = InformeStockController(vista=vista, logic=logic)
        vista.exec_()
        self.ventana_rol.show()

    def abrir_valor_stock(self):
        # Ahora abrimos la ventana de valor stock usando la lógica que internamente usa DAO
        self.ventana_rol.hide()
        logic = ValorStockLogic(self.conn)
        controller = ValorStockController(logic)
        ventana = VentanaValorStock(controller=controller, parent=self)
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_gestionar_usuarios(self):
        self.ventana_rol.hide()
        logic = UsuarioLogic(self.conn)
        controller = UsuarioController(self.conn)
        ventana = VentanaGestionarUsuarios(parent=self, conexion=self.conn)
        ventana.controller = controller
        ventana.exec_()
        self.ventana_rol.show()

    def abrir_registro(self):
        self.hide()
        self.dialog_registro = QtWidgets.QDialog(self)
        self.ui_registro = Ui_Dialog()
        self.ui_registro.setupUi(self.dialog_registro)
        self.registro_controller = RegistroController(self.conn)

        self.ui_registro.btn_volver.clicked.connect(self.volver_login)
        self.ui_registro.btn_salir.clicked.connect(self.salir)
        self.ui_registro.btn_registrar.clicked.connect(self.registrar_usuario)
        self.dialog_registro.exec_()

    def registrar_usuario(self):
        campos = [
            self.ui_registro.line_nombre.text(),
            self.ui_registro.line_apellido.text(),
            self.ui_registro.line_usuario.text(),
            self.ui_registro.line_contrasena.text(),
            self.ui_registro.line_email.text(),
            self.ui_registro.line_telefono.text(),
            self.ui_registro.combo_rol.currentText()
        ]
        exito, mensaje = self.registro_controller.registrar_usuario(campos)
        if exito:
            QtWidgets.QMessageBox.information(self.dialog_registro, "Éxito", mensaje)
            self.dialog_registro.close()
            self.show()
        else:
            QtWidgets.QMessageBox.warning(self.dialog_registro, "Error", mensaje)

    def volver_login(self):
        self.dialog_registro.close()
        self.show()

    def volver_login_desde_rol(self):
        if self.ventana_rol:
            self.ventana_rol.close()
            self.ventana_rol = None
        self.show()

    def salir(self):
        self.db.disconnect()
        QtWidgets.qApp.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())










