# controlador/login_controller.py

class LoginController:
    def __init__(self, conexion):
        self.conn = conexion

    def login(self, usuario, contrasena, rol_seleccionado):
        if not usuario or not contrasena:
            return False, "Por favor, ingresa usuario y contraseña.", None

        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id_usuario, rol FROM usuarios WHERE usuario = ? AND contrasena = ?",
            (usuario, contrasena)
        )
        result = cursor.fetchone()
        if not result:
            return False, "Usuario o contraseña incorrectos.", None

        _, rol_registrado = result
        if rol_registrado.lower() != rol_seleccionado.lower():
            return False, "El rol seleccionado no coincide con el registrado.", None

        return True, f"Bienvenido, {usuario}!", rol_registrado.lower()


class RegistroController:
    def __init__(self, conexion):
        self.conn = conexion

    def registrar_usuario(self, campos):
        if not all(campos):
            return False, "Completa todos los campos."

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

