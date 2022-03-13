from src.dao.dao import Dao
from src.entidade.participante import Participante


class ParticipanteDao(Dao):
    def __init__(self):
        super().__init__('pkl/participantes.pkl')

    def add_participante(self, participante: Participante):
        if participante is not None and isinstance(participante, Participante):
            super().add(participante.cpf, participante)

    def remove_participante(self, participante: Participante):
        if participante is not None and isinstance(participante, Participante):
            super().remove(participante.cpf)

    def update_participante(self, participante: Participante):
        if participante is not None and isinstance(participante, Participante):
            super().update(participante.cpf, participante)

    def get_participante(self, cpf_participante: str):
        if isinstance(cpf_participante, str):
            return super().get(cpf_participante)
