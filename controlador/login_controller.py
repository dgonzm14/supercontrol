class LoginController:
    def __init__(self, logic):
        self.logic = logic

    def login(self, usuario, contrasena, rol_seleccionado):
        return self.logic.verificar_credenciales(usuario, contrasena, rol_seleccionado)


