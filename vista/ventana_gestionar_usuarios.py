from PyQt5 import QtWidgets
from controlador.gestionar_usuarios import Ui_GestionarUsuariosWindow

class VentanaGestionarUsuarios(QtWidgets.QDialog):
    def __init__(self, parent=None, conexion=None):
        super().__init__(parent)
        self.ui = Ui_GestionarUsuariosWindow()
        self.ui.setupUi(self)

        self.conexion = conexion

        self.ui.btn_aniadir.clicked.connect(self.aniadir_usuario)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_usuario)

        self.cargar_usuarios()

    def aniadir_usuario(self):
        nombre = self.ui.line_nombre.text().strip()
        apellido = self.ui.line_apellido.text().strip()
        usuario = self.ui.line_usuario.text().strip()
        contrasena = self.ui.line_contrasena.text().strip()
        email = self.ui.line_email.text().strip()
        telefono = self.ui.line_telefono.text().strip()
        rol = self.ui.combo_rol.currentText()

        if not all([nombre, apellido, usuario, contrasena, email, telefono, rol]):
            QtWidgets.QMessageBox.warning(self, "Campos incompletos", "Todos los campos son obligatorios.")
            return

        try:
            cursor = self.conexion.cursor()
            cursor.execute("""
                INSERT INTO usuarios (nombre_usuario, apellido_usuario, usuario, contrasena, email_usuario, telefono_usuario, rol)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (nombre, apellido, usuario, contrasena, email, telefono, rol))
            self.conexion.commit()
            QtWidgets.QMessageBox.information(self, "Éxito", "Usuario añadido correctamente.")
            self.cargar_usuarios()
            self.limpiar_formulario()
        except Exception as e:
            self.conexion.rollback()
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo añadir el usuario:\n{e}")

    def eliminar_usuario(self):
        fila = self.ui.tabla_usuarios.currentRow()
        if fila == -1:
            QtWidgets.QMessageBox.warning(self, "Seleccionar", "Selecciona un usuario de la tabla para eliminar.")
            return

        usuario = self.ui.tabla_usuarios.item(fila, 0).text()

        confirmacion = QtWidgets.QMessageBox.question(
            self, "Confirmar eliminación",
            f"¿Estás seguro de eliminar al usuario '{usuario}'?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if confirmacion == QtWidgets.QMessageBox.Yes:
            try:
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM usuarios WHERE usuario = ?", (usuario,))
                self.conexion.commit()
                QtWidgets.QMessageBox.information(self, "Eliminado", f"Usuario '{usuario}' eliminado correctamente.")
                self.cargar_usuarios()
            except Exception as e:
                self.conexion.rollback()
                QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo eliminar el usuario:\n{e}")

    def cargar_usuarios(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT usuario, rol FROM usuarios")
            usuarios = cursor.fetchall()

            self.ui.tabla_usuarios.setRowCount(0)
            for fila_idx, (usuario, rol) in enumerate(usuarios):
                self.ui.tabla_usuarios.insertRow(fila_idx)
                self.ui.tabla_usuarios.setItem(fila_idx, 0, QtWidgets.QTableWidgetItem(usuario))
                self.ui.tabla_usuarios.setItem(fila_idx, 1, QtWidgets.QTableWidgetItem(rol))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo cargar la lista de usuarios:\n{e}")

    def limpiar_formulario(self):
        self.ui.line_nombre.clear()
        self.ui.line_apellido.clear()
        self.ui.line_usuario.clear()
        self.ui.line_contrasena.clear()
        self.ui.line_email.clear()
        self.ui.line_telefono.clear()
        self.ui.combo_rol.setCurrentIndex(0)
