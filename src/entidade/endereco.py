import re


class Endereco:
    def __init__(self, logradouro: str, num_endereco: int, cep: str):
        if isinstance(cep, str):
            cep = cep.replace('-', '')
        else:
            raise TypeError
        if isinstance(logradouro, str) \
                and isinstance(num_endereco, int) \
                and num_endereco > 0 \
                and len(cep) == 8 \
                and not re.search(r'\D', cep):
            self.__logradouro = logradouro
            self.__num_endereco = num_endereco
            self.__cep = cep
        else:
            raise TypeError

    @property
    def logradouro(self):
        return self.__logradouro

    @property
    def num_endereco(self):
        return self.__num_endereco

    @property
    def cep(self):
        return self.__cep

    @logradouro.setter
    def logradouro(self, logradouro: str):
        if isinstance(logradouro, str):
            self.__logradouro = logradouro
        else:
            raise TypeError

    @num_endereco.setter
    def num_endereco(self, num_endereco: int):
        if isinstance(num_endereco, int):
            self.__num_endereco = num_endereco
        else:
            raise TypeError

    @cep.setter
    def cep(self, cep: str):
        if isinstance(cep, str):
            cep = cep.replace('-', '')
        else:
            raise TypeError
        if len(cep) == 8 \
                and not re.search(r'\D', cep):
            self.__cep = cep
        else:
            raise TypeError
