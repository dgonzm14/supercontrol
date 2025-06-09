# modelo/dao/usuario_dao.py
class UsuarioDAO:
    def __init__(self, conexion):
        self.conn = conexion

    def obtener_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT usuario, rol FROM usuarios")
        return cursor.fetchall()

    def insertar_usuario(self, nombre, apellido, usuario, contrasena, email, telefono, rol):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nombre_usuario, apellido_usuario, usuario, contrasena, email_usuario, telefono_usuario, rol)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nombre, apellido, usuario, contrasena, email, telefono, rol))
        self.conn.commit()

    def eliminar_usuario_por_nombre(self, usuario):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE usuario = ?", (usuario,))
        self.conn.commit()
