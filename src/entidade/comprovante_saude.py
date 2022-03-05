from datetime import datetime

from src.entidade.enums.resultado_pcr import ResultadoPcr


class ComprovanteSaude:
    def __init__(self,
                 primeira_dose: bool,
                 segunda_dose: bool,
                 data_horario_teste: list,
                 resultado_pcr: ResultadoPcr):
        if isinstance(primeira_dose, bool) \
                and isinstance(segunda_dose, bool) \
                and isinstance(data_horario_teste[0], int) \
                and isinstance(data_horario_teste[1], int) \
                and isinstance(data_horario_teste[2], int) \
                and isinstance(data_horario_teste[3], int) \
                and isinstance(data_horario_teste[4], int) \
                and isinstance(resultado_pcr, ResultadoPcr):
            self.__primeira_dose = primeira_dose
            self.__segunda_dose = segunda_dose
            self.__data_horario_teste = datetime(data_horario_teste[0],
                                                 data_horario_teste[1],
                                                 data_horario_teste[2],
                                                 data_horario_teste[3],
                                                 data_horario_teste[4])
            self.__resultado_pcr = resultado_pcr
        else:
            raise TypeError

    @property
    def primeira_dose(self):
        return self.__primeira_dose

    @property
    def segunda_dose(self):
        return self.__segunda_dose

    @property
    def data_horario_teste(self):
        return self.__data_horario_teste

    @property
    def resultado_pcr(self):
        return self.__resultado_pcr

    @primeira_dose.setter
    def primeira_dose(self, primeira_dose: bool):
        if isinstance(primeira_dose, bool):
            self.__primeira_dose = primeira_dose
        else:
            raise TypeError

    @segunda_dose.setter
    def segunda_dose(self, segunda_dose: bool):
        if isinstance(segunda_dose, bool):
            self.__segunda_dose = segunda_dose
        else:
            raise TypeError

    @data_horario_teste.setter
    def data_horario_teste(self, data_horario_teste: list):
        if isinstance(data_horario_teste[0], int) \
                and isinstance(data_horario_teste[1], int) \
                and isinstance(data_horario_teste[2], int) \
                and isinstance(data_horario_teste[3], int) \
                and isinstance(data_horario_teste[4], int):
            self.__data_horario_teste = datetime(data_horario_teste[0],
                                                 data_horario_teste[1],
                                                 data_horario_teste[2],
                                                 data_horario_teste[3],
                                                 data_horario_teste[4])
        else:
            raise TypeError

    @resultado_pcr.setter
    def resultado_pcr(self, resultado_pcr: ResultadoPcr):
        if isinstance(resultado_pcr, ResultadoPcr):
            self.__resultado_pcr = resultado_pcr
        else:
            raise TypeError

    def imunizado(self):
        return self.__primeira_dose and self.__segunda_dose

    def pcr_autorizado(self, data_horario_list: list):
        if isinstance(data_horario_list[0], int) \
                and isinstance(data_horario_list[1], int) \
                and isinstance(data_horario_list[2], int) \
                and isinstance(data_horario_list[3], int) \
                and isinstance(data_horario_list[4], int):
            data_horario_evento = datetime(data_horario_list[0],
                                           data_horario_list[1],
                                           data_horario_list[2],
                                           data_horario_list[3],
                                           data_horario_list[4])

            diferenca = data_horario_evento - self.__data_horario_teste
            return self.__resultado_pcr == ResultadoPcr.negativo and diferenca.total_seconds() <= 259200
        else:
            raise TypeError
