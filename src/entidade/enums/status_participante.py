from enum import Enum


class StatusParticipante(Enum):
    autorizado = 'Autorizado'
    nao_autorizado = 'Não autorizado'
    a_confirmar = 'A confirmar'
