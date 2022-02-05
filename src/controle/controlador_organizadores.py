from src.tela.tela_organizador import TelaOrganizador
from src.entidade.organizador import Organizador


class ControladorOrganizador:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__organizadores = []
        self.__tela_organizador = TelaOrganizador()

    def adiciona_organizador(self):
        dados_organizador = self.__tela_organizador.pegar_dados_local()
        organizador = Organizador(dados_organizador["cpf"], dados_organizador["nome"],
                                  [dados_organizador["dia_nascimento"],
                                   dados_organizador["mes_nascimento"],
                                   dados_organizador["ano_nascimento"]])
        self.__organizadores.append(organizador)

    def exclui_organizador(self):
        self.lista_organizadores()
        cpf_organizador = self.__tela_organizador.selecionar_organizador()
        organizador = self.pega_organizador_por_cpf(cpf_organizador)

        if(organizador is not None):
            self.__organizadores.remove(organizador)
            self.lista_organizadores()
        else:
            self.__tela_organizador.mostrar_mensagem("ATENÇÃO: Organizador não cadastrado")

    def altera_organizador(self):
        self.lista_organizadores()
        cpf_organizador = self.__tela_organizador.selecionar_organizador()
        organizador = self.pega_organizador_por_cpf(cpf_organizador)

        if (organizador is not None):
            novos_dados_organizador = self.__tela_organizador.pegar_dados_organizador()
            organizador.cpf = novos_dados_organizador["cpf"]
            organizador.nome = novos_dados_organizador["nome"]
            organizador.data_nascimento = [novos_dados_organizador["dia_nascimento"],
                                           novos_dados_organizador["mes_nascimento"],
                                           novos_dados_organizador["ano_nascimento"]]
            self.lista_organizadores()
        else:
            self.__tela_organizador.mostrar_mensagem("ATENÇÃO: Organizador não cadastrado")

    def pega_organizador_por_cpf(self, cpf_organizador):
        for organizador in self.__organizadores:
            if organizador.cpf == cpf_organizador:
                return organizador
        return None

    def lista_organizadores(self):
        for organizador in self.__organizadores:
            self.__tela_organizador.consultar_organizador({"cpf": organizador.cpf, "nome": organizador.nome,
                                                           "dia_nascimento": organizador.data_nascimento[0],
                                                           "mes_nascimento": organizador.data_nascimento[1],
                                                           "ano_nascimento": organizador.data_nascimento[2],})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_organizador, 2: self.exclui_organizador, 3: self.altera_organizador,
                        4: self.pega_organizador_por_cpf, 5: self.lista_organizadores(), 0: self.retornar()}

        continua = True
        while continua:
            lista_opcoes[self.__tela_local.tela_opcoes()]()
