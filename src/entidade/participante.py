from datetime import date

from comprovante_saude import ComprovanteSaude
from endereco import Endereco
from enums.status_participante import StatusParticipante
from pessoa import Pessoa


class Participante(Pessoa):
    def __init__(self, cpf: str, nome: str, data_nascimento: list, endereco: list):
        super().__init__(cpf, nome)
        if isinstance(data_nascimento[0], int) \
                and isinstance(data_nascimento[1], int) \
                and isinstance(data_nascimento[2], int):

            if 0 <= (date.today().year - data_nascimento[0]) <= 150:
                self.__endereco = Endereco(endereco[0], endereco[1], endereco[2])
                self.__data_nascimento = date(data_nascimento[0], data_nascimento[1], data_nascimento[2])
                self.__status_participante = StatusParticipante.a_confirmar
                self.__comprovante_saude = None
            else:
                raise TypeError
        else:
            raise TypeError

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def status_participante(self):
        return self.__status_participante

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
            self.__data_nascimento = date(data_nascimento[0], data_nascimento[1], data_nascimento[2])
        else:
            raise TypeError

    @status_participante.setter
    def status_participante(self, status_participante: StatusParticipante):
        if isinstance(status_participante, StatusParticipante):
            self.__status_participante = status_participante
        else:
            raise TypeError

    @endereco.setter
    def endereco(self, endereco: list):
        self.__endereco = Endereco(endereco[0], endereco[1], endereco[2])

    @comprovante_saude.setter
    def comprovante_saude(self, comprovante_saude: list):
        self.__comprovante_saude = ComprovanteSaude(comprovante_saude[0], comprovante_saude[1],
                                                    comprovante_saude[2], comprovante_saude[3])
