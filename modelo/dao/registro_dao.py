class RegistroDAO:
    def __init__(self, conexion):
        self.conn = conexion

    def insertar_usuario(self, campos):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO usuarios (nombre_usuario, apellido_usuario, usuario, contrasena, email_usuario, telefono_usuario, rol)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                campos
            )
            self.conn.commit()
            return True, "Usuario registrado correctamente."
        except Exception as e:
            return False, f"No se pudo registrar: {e}"
