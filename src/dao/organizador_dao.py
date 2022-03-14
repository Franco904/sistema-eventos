from src.dao.dao import Dao
from src.entidade.organizador import Organizador


class OrganizadorDao(Dao):
    def __init__(self):
        super().__init__('organizadores.pkl')

    def add_organizador(self, organizador: Organizador):
        if organizador is not None and isinstance(organizador, Organizador):
            super().add(organizador.cpf, organizador)

    def remove_organizador(self, organizador: Organizador):
        if organizador is not None and isinstance(organizador, Organizador):
            super().remove(organizador.cpf)

    def update_organizador(self, organizador: Organizador):
        if organizador is not None and isinstance(organizador, Organizador):
            super().update(organizador.cpf, organizador)

    def get_organizador(self, cpf_organizador: str):
        if isinstance(cpf_organizador, str):
            return super().get(cpf_organizador)
