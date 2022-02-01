from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, cpf: int, nome: str):
        if isinstance(cpf, int) and isinstance(nome, str):
            self.__cpf = cpf
            self.__nome = nome
        else:
            raise TypeError

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int) and len(cpf.__str__()) == 11:
            self.__cpf = cpf
        else:
            raise TypeError

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError