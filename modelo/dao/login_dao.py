class LoginDAO:
    def __init__(self, conexion):
        self.conn = conexion

    def validar_usuario(self, usuario, contrasena, rol_esperado):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT rol FROM usuarios WHERE usuario = ? AND contrasena = ?",
            (usuario, contrasena)
        )
        result = cursor.fetchone()
        if not result:
            return False, "Usuario o contraseña incorrectos.", None

        rol_registrado = result[0]
        if rol_registrado.lower() != rol_esperado.lower():
            return False, "El rol seleccionado no coincide con el registrado.", None

        return True, f"Bienvenido, {usuario}!", rol_registrado.lower()
