from datetime import datetime

from evento import Evento
from participante import Participante


class Participacao():
    def __init__(self, id: int, data_horario_entrada: datetime, data_horario_saida: datetime,
                 participante: Participante, evento: Evento):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError
        if isinstance(data_horario_entrada, datetime):
            self.__data_horario_entrada = data_horario_entrada
        else:
            raise TypeError
        if isinstance(data_horario_entrada, datetime):
            self.__data_horario_saida = data_horario_saida
        else:
            raise TypeError
        if isinstance(participante, Participante):
            self.__participante = participante
        else:
            raise TypeError
        if isinstance(evento, Evento):
            self.__evento = evento
        else:
            raise TypeError

    @property
    def id(self):
        return self.__id

    @property
    def data_horario_entrada(self):
        return self.__data_horario_entrada

    @property
    def data_horario_saida(self):
        return self.__data_horario_saida

    @property
    def participante(self):
        return self.__participante

    @property
    def evento(self):
        return self.__evento

    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError

    @data_horario_entrada.setter
    def data_horario_entrada(self, data_horario_entrada: datetime):
        if isinstance(data_horario_entrada, datetime):
            self.__data_horario_entrada = data_horario_entrada
        else:
            raise TypeError

    @data_horario_saida.setter
    def data_horario_saida(self, data_horario_saida: datetime):
        if isinstance(data_horario_saida, datetime):
            self.__data_horario_saida = data_horario_saida
        else:
            raise TypeError

    @participante.setter
    def participante(self, participante: Participante):
        if isinstance(participante, Participante):
            self.__participante = participante
        else:
            raise TypeError

    @evento.setter
    def evento(self, evento: Evento):
        if isinstance(evento, Evento):
            self.__evento = evento
        else:
            raise TypeError
