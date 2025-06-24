class LoginLogic:
    def __init__(self, dao):
        self.dao = dao

    def verificar_credenciales(self, usuario, contrasena, rol_seleccionado):
        if not usuario or not contrasena:
            return False, "Por favor, ingresa usuario y contraseña.", None
        return self.dao.validar_usuario(usuario, contrasena, rol_seleccionado)
