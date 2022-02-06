from src.entidade.pessoa import Pessoa


class Organizador(Pessoa):
    def __init__(self, cpf: str, nome: str, data_nascimento: list):
        super().__init__(cpf, nome, data_nascimento)
