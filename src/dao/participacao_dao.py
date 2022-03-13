from src.dao.dao import Dao
from src.entidade.participacao import Participacao


class ParticipacaoDao(Dao):
    def __init__(self):
        super().__init__('pkl/participacoes.pkl')

    def add_participacao(self, participacao: Participacao):
        if participacao is not None and isinstance(participacao, Participacao):
            super().add(participacao.id, participacao)

    def remove_participacao(self, participacao: Participacao):
        if participacao is not None and isinstance(participacao, Participacao):
            super().remove(participacao.id)

    def update_participacao(self, participacao: Participacao):
        if participacao is not None and isinstance(participacao, Participacao):
            super().update(participacao.id, participacao)

    def get_participacao(self, id_participacao: int):
        if isinstance(id_participacao, int):
            return super().get(id_participacao)
