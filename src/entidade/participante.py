from src.entidade.comprovante_saude import ComprovanteSaude
from src.entidade.endereco import Endereco
from src.entidade.enums.status_participante import StatusParticipante
from src.entidade.pessoa import Pessoa


class Participante(Pessoa):
    def __init__(self, cpf: str, nome: str, data_nascimento: list, endereco: list):
        super().__init__(cpf, nome, data_nascimento)
        self.__endereco = Endereco(endereco[0], endereco[1], endereco[2])
        self.__status_participante = StatusParticipante.a_confirmar
        self.__comprovante_saude = None

    @property
    def status_participante(self):
        return self.__status_participante

    @property
    def comprovante_saude(self):
        return self.__comprovante_saude

    @property
    def endereco(self):
        return self.__endereco

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
