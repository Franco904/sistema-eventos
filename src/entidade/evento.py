from datetime import datetime

from src.entidade.local import Local
from src.entidade.organizador import Organizador
import src.entidade.participacao
from src.entidade.participante import Participante


class Evento:
    def __init__(self,
                 id: int,
                 titulo: str,
                 local: Local,
                 data_horario_evento: list,
                 capacidade: int,
                 organizadores: list
                 ):
        if isinstance(id, int) \
                and isinstance(titulo, str) \
                and isinstance(local, Local) \
                and isinstance(data_horario_evento[0], int) \
                and isinstance(data_horario_evento[1], int) \
                and isinstance(data_horario_evento[2], int) \
                and isinstance(data_horario_evento[3], int) \
                and isinstance(data_horario_evento[4], int) \
                and isinstance(capacidade, int) \
                and isinstance(organizadores, list):

            self.__id = id
            self.__titulo = titulo
            self.__local = local
            self.__data_horario_evento = datetime(data_horario_evento[0],
                                                  data_horario_evento[1],
                                                  data_horario_evento[2],
                                                  data_horario_evento[3],
                                                  data_horario_evento[4])
            self.__capacidade = capacidade
            self.__organizadores = organizadores
            self.__participantes = []
            self.__participacoes = []

    @property
    def id(self):
        return self.__id

    @property
    def titulo(self):
        return self.__titulo

    @property
    def local(self):
        return self.__local

    @property
    def data_horario_evento(self):
        return self.__data_horario_evento

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def organizadores(self):
        return self.__organizadores

    @property
    def participantes(self):
        return self.__participantes

    @property
    def participacoes(self):
        return self.__participacoes

    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            raise TypeError

    @local.setter
    def local(self, local: Local):
        if isinstance(local, Local) and local is not None:
            self.__local = local
        else:
            raise TypeError

    @organizadores.setter
    def organizadores(self, organizadores: list):
        if isinstance(organizadores, list):
            for o in organizadores:
                if not isinstance(o, Organizador):
                    raise TypeError
            self.__organizadores = organizadores
        else:
            raise TypeError

    @participantes.setter
    def participantes(self, participantes: list):
        if isinstance(participantes, list):
            for p in participantes:
                if not isinstance(p, Participante):
                    raise TypeError
            self.__participantes = participantes
        else:
            raise TypeError

    @participacoes.setter
    def participacoes(self, participacoes: list):
        if isinstance(participacoes, list):
            for p in participacoes:
                if not isinstance(p, src.entidade.participacao.Participacao):
                    raise TypeError
            self.__participacoes = participacoes
        else:
            raise TypeError

    def adicionar_organizador(self, organizador: Organizador):
        if isinstance(organizador, Organizador) and organizador is not None:
            if organizador in self.__organizadores:
                raise Exception
            self.__organizadores.append(organizador)
        else:
            raise TypeError

    def adicionar_participante(self, participante: Participante):
        if isinstance(participante, Participante) and participante is not None:
            if participante in self.__participantes:
                raise Exception
            self.__participantes.append(participante)
        else:
            raise TypeError

    def adicionar_participacao(self, participacao: src.entidade.participacao.Participacao):
        if isinstance(participacao, src.entidade.participacao.Participacao) and participacao is not None:
            if participacao in self.__participacoes:
                raise Exception
            self.__participacoes.append(participacao)
        else:
            raise TypeError

    def excluir_organizador(self, organizador: Organizador):
        if isinstance(organizador, Organizador) \
                and organizador not in self.__organizadores \
                and organizador is not None:
            self.__organizadores.remove(organizador)
        else:
            raise TypeError

    def excluir_participante(self, participante: Participante):
        if isinstance(participante, Participante) and participante is not None:
            self.__participantes.remove(participante)
        else:
            raise TypeError

    def excluir_participacao(self, participacao: src.entidade.participacao.Participacao):
        if isinstance(participacao, src.entidade.participacao.Participacao) and participacao is not None:
            self.__participacoes.remove(participacao)
        else:
            raise TypeError


l = Local(0, 'Centro de Eventos NGR')
o1 = Organizador('10101010101', 'Rogerio Gomes', [1984, 4, 23])
o2 = Organizador('30303030300', 'Guilherme Freitas', [1982, 8, 3])

# evento = Evento(1, '', l, [2022, 2, 26, 19, 30], 500, [o1, o2])
