from datetime import datetime
from pessoa import Pessoa
from endereco import Endereco
from comprovante_saude import ComprovanteSaude
from enums.status_participante import StatusParticipante
from enums.resultado_pcr import ResultadoPcr


class Participante(Pessoa):
    def __init__(self, cpf: str, nome: str, data_nascimento: list, endereco: list):
        super().__init__(cpf, nome)
        if isinstance(data_nascimento[0], int) \
                and isinstance(data_nascimento[1], int) \
                and isinstance(data_nascimento[2], int):
            self.__data_nascimento = datetime(data_nascimento[0], data_nascimento[1], data_nascimento[2], 0, 0)
        else:
            raise TypeError
        self.__endereco = Endereco(endereco[0], endereco[1], endereco[2])
        self.__status = StatusParticipante.a_confirmar
        self.__comprovante_saude = ComprovanteSaude(False, False, [2022, 3, 2, 19, 52], ResultadoPcr.nao_realizado)

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def status(self):
        return self.__status

    @property
    def comprovante_saude(self):
        return self.__comprovante_saude

    @property
    def endereco(self):
        return self.__endereco

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: list):
        if isinstance(data_nascimento[0], int) \
                and isinstance(data_nascimento[1], int) \
                and isinstance(data_nascimento[2], int):
            self.__data_nascimento = datetime(data_nascimento[0], data_nascimento[1], data_nascimento[2], 0, 0)
        else:
            raise TypeError

    @status.setter
    def status(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError

    @endereco.setter
    def endereco(self, endereco: list):
        self.__endereco = Endereco(endereco[0], endereco[1], endereco[2])

    @comprovante_saude.setter
    def comprovante_saude(self, status_participante: StatusParticipante):
        if isinstance(status_participante, StatusParticipante):
            self.__status_participante = status_participante
        else:
            raise TypeError
