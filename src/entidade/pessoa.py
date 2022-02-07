import re
from abc import ABC, abstractmethod
from datetime import date


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, cpf: str, nome: str, data_nascimento: list):
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
        if isinstance(data_nascimento[0], int) \
                and isinstance(data_nascimento[1], int) \
                and isinstance(data_nascimento[2], int):
            if 0 <= (date.today().year - data_nascimento[0]) <= 150:
                self.__data_nascimento = date(data_nascimento[0], data_nascimento[1], data_nascimento[2])
            else:
                raise TypeError

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

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

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: list):
        if isinstance(data_nascimento[0], int) \
                and isinstance(data_nascimento[1], int) \
                and isinstance(data_nascimento[2], int):
            self.__data_nascimento = date(data_nascimento[0], data_nascimento[1], data_nascimento[2])
        else:
            raise TypeError
