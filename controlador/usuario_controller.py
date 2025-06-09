from modelo.dao.usuario_dao import UsuarioDAO


class UsuarioController:
    def __init__(self, conexion):
        self.dao = UsuarioDAO(conexion)

    def obtener_usuarios(self):
        try:
            return self.dao.obtener_usuarios()
        except Exception as e:
            # Para que la vista gestione el error, aquí podrías retornar lista vacía o lanzar.
            return []

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


