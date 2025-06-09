from PyQt5 import QtWidgets
from vista.gestionar_usuarios import Ui_GestionarUsuariosWindow
from controlador.usuario_controller import UsuarioController

class VentanaGestionarUsuarios(QtWidgets.QDialog):
    def __init__(self, parent=None, conexion=None):
        super().__init__(parent)
        self.ui = Ui_GestionarUsuariosWindow()
        self.ui.setupUi(self)

        self.controller = UsuarioController(conexion)

        self.ui.btn_aniadir.clicked.connect(self.obtener_datos_formulario)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_usuario)

        self.cargar_usuarios()

    def cargar_usuarios(self):
        usuarios = self.controller.obtener_usuarios()
        self.ui.tabla_usuarios.setRowCount(0)
        for fila_idx, (usuario, rol) in enumerate(usuarios):
            self.ui.tabla_usuarios.insertRow(fila_idx)
            self.ui.tabla_usuarios.setItem(fila_idx, 0, QtWidgets.QTableWidgetItem(usuario))
            self.ui.tabla_usuarios.setItem(fila_idx, 1, QtWidgets.QTableWidgetItem(rol))

    def obtener_datos_formulario(self):
        campos = [
            self.ui.line_nombre.text().strip(),
            self.ui.line_apellido.text().strip(),
            self.ui.line_usuario.text().strip(),
            self.ui.line_contrasena.text().strip(),
            self.ui.line_email.text().strip(),
            self.ui.line_telefono.text().strip(),
            self.ui.combo_rol.currentText()
        ]
        exito, mensaje = self.controller.aniadir_usuario(campos)
        if exito:
            QtWidgets.QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_usuarios()
            self.limpiar_formulario()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", mensaje)

    def eliminar_usuario(self):
        fila = self.ui.tabla_usuarios.currentRow()
        if fila == -1:
            QtWidgets.QMessageBox.warning(self, "Seleccionar", "Selecciona un usuario para eliminar.")
            return

        usuario = self.ui.tabla_usuarios.item(fila, 0).text()
        confirmacion = QtWidgets.QMessageBox.question(
            self, "Confirmar eliminación",
            f"¿Estás seguro de eliminar al usuario '{usuario}'?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if confirmacion == QtWidgets.QMessageBox.Yes:
            exito, mensaje = self.controller.eliminar_usuario(usuario)
            if exito:
                QtWidgets.QMessageBox.information(self, "Eliminado", mensaje)
                self.cargar_usuarios()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", mensaje)

    def limpiar_formulario(self):
        self.ui.line_nombre.clear()
        self.ui.line_apellido.clear()
        self.ui.line_usuario.clear()
        self.ui.line_contrasena.clear()
        self.ui.line_email.clear()
        self.ui.line_telefono.clear()
        self.ui.combo_rol.setCurrentIndex(0)


