from enum import Enum


class ResultadoPcr(Enum):
    positivo = 'Positivo'
    negativo = 'Negativo'
    nao_realizado = 'Não realizado'
