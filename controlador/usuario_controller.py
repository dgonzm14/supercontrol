from modelo.usuario_logic import UsuarioLogic

class UsuarioController:
    def __init__(self, logic: UsuarioLogic):
        self.logic = logic

    def obtener_usuarios(self):
        try:
            return self.logic.obtener_usuarios()
        except Exception:
            return []

    def aniadir_usuario(self, campos):
        return self.logic.aniadir_usuario(campos)

    def eliminar_usuario(self, usuario):
        return self.logic.eliminar_usuario(usuario)




