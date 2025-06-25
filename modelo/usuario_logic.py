from modelo.dao.usuario_dao import UsuarioDAO

class UsuarioLogic:
    def __init__(self, dao: UsuarioDAO):
        self.dao = dao

    def obtener_usuarios(self):
        return self.dao.obtener_usuarios()

    def aniadir_usuario(self, campos):
        if not all(campos):
            return False, "Todos los campos son obligatorios."

        try:
            self.dao.insertar_usuario(*campos)
            return True, "Usuario añadido correctamente."
        except Exception as e:
            return False, f"No se pudo añadir el usuario:\n{e}"

    def eliminar_usuario(self, usuario):
        try:
            self.dao.eliminar_usuario_por_nombre(usuario)
            return True, f"Usuario '{usuario}' eliminado."
        except Exception as e:
            return False, f"No se pudo eliminar el usuario:\n{e}"

