from src.dao.dao import Dao
from src.entidade.local import Local


class LocalDao(Dao):
    def __init__(self):
        super().__init__('locais.pkl')

    def add_local(self, local: Local):
        if local is not None and isinstance(local, Local):
            super().add(local.id, local)

    def remove_local(self, local: Local):
        if local is not None and isinstance(local, Local):
            super().remove(local.id)

    def update_local(self, local: Local):
        if local is not None and isinstance(local, Local):
            super().update(local.id, local)

    def get_local(self, id_local: int):
        if isinstance(id_local, int):
            return super().get(id_local)
