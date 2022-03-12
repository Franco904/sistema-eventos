from src.dao.organizador_dao import OrganizadorDao
from src.entidade.organizador import Organizador
from src.tela.tela_organizador import TelaOrganizador


class ControladorOrganizador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__organizadores_dao = OrganizadorDao()
        self.__tela_organizador = TelaOrganizador()

    @property
    def organizadores(self):
        return self.__organizadores_dao.get_all()

    @property
    def tela_organizador(self):
        return self.__tela_organizador

    def adicionar_organizador(self):
        dados_organizador = self.__tela_organizador.pegar_dados_organizador(False)

        if dados_organizador is None:
            return

        # Faz a verificação da existência do organizador na lista
        for organizador in self.organizadores:
            if organizador.cpf == dados_organizador['cpf']:
                self.__tela_organizador.mostrar_mensagem('O cpf inserido já pertence a um organizador na lista.')
                return

        try:
            organizador = Organizador(
                dados_organizador['cpf'],
                dados_organizador['nome'],
                [
                    dados_organizador['ano_nascimento'],
                    dados_organizador['mes_nascimento'],
                    dados_organizador['dia_nascimento']
                ])

            self.__organizadores_dao.add_organizador(organizador)
            self.__tela_organizador.mostrar_mensagem('Organizador adicionado na lista.')

        except TypeError:
            self.__tela_organizador.mostrar_mensagem('Algum dado foi inserido incorretamente.')

    def excluir_organizador(self):
        if len(self.organizadores) > 0:
            cpf_organizador = self.__tela_organizador.selecionar_organizador()
            organizador = self.pegar_organizador_por_cpf(cpf_organizador)

            if organizador is not None:
                self.__organizadores_dao.remove_organizador(organizador)
                self.__tela_organizador.mostrar_mensagem('Organizador removido na lista.')

            else:
                self.__tela_organizador.mostrar_mensagem('ATENÇÃO: Organizador não cadastrado.')

    def alterar_organizador(self):
        if len(self.organizadores) > 0:
            cpf_organizador = self.__tela_organizador.selecionar_organizador()
            organizador = self.pegar_organizador_por_cpf(cpf_organizador)

            if organizador is not None:
                novos_dados_organizador = self.__tela_organizador.pegar_dados_organizador(True)

                if novos_dados_organizador is None:
                    return

                try:
                    organizador.nome = novos_dados_organizador['nome']
                    organizador.data_nascimento = [novos_dados_organizador['ano_nascimento'],
                                                   novos_dados_organizador['mes_nascimento'],
                                                   novos_dados_organizador['dia_nascimento']]

                    self.__organizadores_dao.update_organizador(organizador)
                    self.__tela_organizador.mostrar_mensagem('Dados do organizador alterados com sucesso.')

                except TypeError:
                    self.__tela_organizador.mostrar_mensagem('Algum dado foi inserido incorretamente.')

            else:
                self.__tela_organizador.mostrar_mensagem('ATENÇÃO: Organizador não cadastrado.')

    def mostrar_organizador(self):
        if len(self.organizadores) > 0:
            cpf_organizador = self.__tela_organizador.selecionar_organizador()
            organizador = self.pegar_organizador_por_cpf(cpf_organizador)

            if organizador is not None:
                self.__tela_organizador.mostrar_organizador({
                    'cpf': organizador.cpf,
                    'nome': organizador.nome,
                    'data_nascimento': organizador.data_nascimento
                })
            else:
                self.__tela_organizador.mostrar_mensagem('ATENÇÃO: Organizador não cadastrado.')
        else:
            self.__tela_organizador.mostrar_mensagem('Não há organizadores cadastrados para listar.')

    def pegar_organizador_por_cpf(self, cpf_organizador):
        try:
            return self.__organizadores_dao.get_organizador(cpf_organizador)
        except KeyError:
            return None

    def listar_organizadores(self):
        if len(self.organizadores) > 0:
            for organizador in self.organizadores:
                self.__tela_organizador.mostrar_organizador({
                    'cpf': organizador.cpf,
                    'nome': organizador.nome,
                    'data_nascimento': organizador.data_nascimento
                })
        else:
            self.__tela_organizador.mostrar_mensagem('Não há organizadores cadastrados para listar.')

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.adicionar_organizador, 2: self.excluir_organizador, 3: self.alterar_organizador,
                        4: self.mostrar_organizador, 5: self.listar_organizadores, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_organizador.tela_opcoes()]()
