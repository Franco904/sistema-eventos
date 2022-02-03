import re
from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, cpf: str, nome: str):
        if isinstance(cpf, str):
            cpf = cpf.replace('.', '').replace('-', '')
        else:
            raise TypeError
        if len(cpf) == 11 \
                and not re.search(r'\D', cpf) \
                and isinstance(nome, str):
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
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            cpf = cpf.replace('.', '').replace('-', '')
        else:
            raise TypeError
        if len(cpf) == 11 \
                and not re.search(r'\D', cpf):
            self.__cpf = cpf
        else:
            raise TypeError

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError
