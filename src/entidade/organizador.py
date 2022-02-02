from pessoa import Pessoa


class Organizador(Pessoa):
    def __init__(self, cpf: int, nome: str):
        super().__init__(cpf, nome)
