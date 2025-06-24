class RegistroController:
    def __init__(self, logic):
        self.logic = logic

    def registrar_usuario(self, campos):
        return self.logic.registrar_usuario(campos)
