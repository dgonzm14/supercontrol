class RegistroLogic:
    def __init__(self, dao):
        self.dao = dao

    def registrar_usuario(self, campos):
        if not all(campos):
            return False, "Completa todos los campos."
        return self.dao.insertar_usuario(campos)
