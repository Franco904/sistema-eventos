from datetime import datetime

from src.entidade.participante import Participante


class Participacao:
    def __init__(self, id: int, id_evento: int, data_horario_entrada: list,
                 participante: Participante):
        if isinstance(id, int) \
                and isinstance(id_evento, int) \
                and isinstance(data_horario_entrada[0], int) \
                and isinstance(data_horario_entrada[1], int) \
                and isinstance(data_horario_entrada[2], int) \
                and isinstance(data_horario_entrada[3], int) \
                and isinstance(data_horario_entrada[4], int) \
                and isinstance(participante, Participante):
            self.__id = id
            self.__id_evento = id_evento
            self.__data_horario_entrada = datetime(data_horario_entrada[0],
                                                   data_horario_entrada[1],
                                                   data_horario_entrada[2],
                                                   data_horario_entrada[3],
                                                   data_horario_entrada[4])
            self.__data_horario_saida = None
            self.__participante = participante
        else:
            raise TypeError

    @property
    def id(self):
        return self.__id

    @property
    def id_evento(self):
        return self.__id_evento

    @property
    def data_horario_entrada(self):
        return self.__data_horario_entrada

    @property
    def data_horario_saida(self):
        return self.__data_horario_saida

    @property
    def participante(self):
        return self.__participante

    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError

    @id_evento.setter
    def id_evento(self, id_evento: int):
        if isinstance(id_evento, int):
            self.__id_evento = id_evento
        else:
            raise TypeError

    @data_horario_entrada.setter
    def data_horario_entrada(self, data_horario_entrada: list):
        if isinstance(data_horario_entrada[0], int) \
                and isinstance(data_horario_entrada[1], int) \
                and isinstance(data_horario_entrada[2], int) \
                and isinstance(data_horario_entrada[3], int) \
                and isinstance(data_horario_entrada[4], int):
            self.__data_horario_entrada = datetime(data_horario_entrada[0],
                                                   data_horario_entrada[1],
                                                   data_horario_entrada[2],
                                                   data_horario_entrada[3],
                                                   data_horario_entrada[4])
        else:
            raise TypeError

    @data_horario_saida.setter
    def data_horario_saida(self, data_horario_saida: list):
        if isinstance(data_horario_saida[0], int) \
                and isinstance(data_horario_saida[1], int) \
                and isinstance(data_horario_saida[2], int) \
                and isinstance(data_horario_saida[3], int) \
                and isinstance(data_horario_saida[4], int):
            self.__data_horario_saida = datetime(data_horario_saida[0],
                                                 data_horario_saida[1],
                                                 data_horario_saida[2],
                                                 data_horario_saida[3],
                                                 data_horario_saida[4])
        else:
            raise TypeError

    @participante.setter
    def participante(self, participante: Participante):
        if isinstance(participante, Participante) and participante is not None:
            self.__participante = participante
        else:
            raise TypeError
