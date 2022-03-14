from src.dao.dao import Dao
from src.entidade.evento import Evento


class EventoDao(Dao):
    def __init__(self):
        super().__init__('eventos.pkl')

    def add_evento(self, evento: Evento):
        if evento is not None and isinstance(evento, Evento):
            super().add(evento.id_evento, evento)

    def remove_evento(self, evento: Evento):
        if evento is not None and isinstance(evento, Evento):
            super().remove(evento.id_evento)

    def update_evento(self, evento: Evento):
        if evento is not None and isinstance(evento, Evento):
            super().update(evento.id_evento, evento)

    def get_evento(self, id_evento: int):
        if isinstance(id_evento, int):
            return super().get(id_evento)
