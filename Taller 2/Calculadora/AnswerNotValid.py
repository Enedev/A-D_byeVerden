
class AnswerNotValid(Exception):
    def __init__(self, mensaje=" Alguna de las respuestas ingresadas fue inválida ..."):
        super().__init__(mensaje)
