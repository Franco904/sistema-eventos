from src.entidade.organizador import Organizador
from src.tela.tela_organizador import TelaOrganizador


class ControladorOrganizador:
    def __init__(self, controlador_eventos):
        self.__controlador_eventos = controlador_eventos
        self.__organizadores = []
        self.__tela_organizador = TelaOrganizador()

    @property
    def organizadores(self):
        return self.__organizadores

    @property
    def tela_organizador(self):
        return self.__tela_organizador

    def adiciona_organizador(self):
        dados_organizador = self.__tela_organizador.pegar_dados_organizador()
        try:
            organizador = Organizador(dados_organizador["cpf"], dados_organizador["nome"],
                                      [dados_organizador["ano_nascimento"],
                                       dados_organizador["mes_nascimento"],
                                       dados_organizador["dia_nascimento"]])
            self.__organizadores.append(organizador)
            self.__tela_organizador.mostrar_mensagem('Organizador adicionado na lista.')

        except TypeError:
            self.__tela_organizador.mostrar_mensagem("Algum dado foi inserido incorretamente.")

    def exclui_organizador(self):
        self.lista_organizadores()
        if len(self.__organizadores) > 0:
            cpf_organizador = self.__tela_organizador.selecionar_organizador()
            organizador = self.pega_organizador_por_cpf(cpf_organizador)

            if organizador is not None:
                self.__organizadores.remove(organizador)
                self.__tela_organizador.mostrar_mensagem('Organizador removido na lista')
            else:
                self.__tela_organizador.mostrar_mensagem("ATENÇÃO: Organizador não cadastrado")

    def altera_organizador(self):
        self.lista_organizadores()
        if len(self.__organizadores) > 0:
            cpf_organizador = self.__tela_organizador.selecionar_organizador()
            organizador = self.pega_organizador_por_cpf(cpf_organizador)
            try:
                if organizador is not None:
                    novos_dados_organizador = self.__tela_organizador.pegar_dados_organizador()
                    organizador.cpf = novos_dados_organizador["cpf"]
                    organizador.nome = novos_dados_organizador["nome"]
                    organizador.data_nascimento = [novos_dados_organizador["ano_nascimento"],
                                                   novos_dados_organizador["mes_nascimento"],
                                                   novos_dados_organizador["dia_nascimento"]]
                    self.__tela_organizador.mostrar_mensagem('Dados do organizador alterados com sucesso')
                else:
                    self.__tela_organizador.mostrar_mensagem("ATENÇÃO: Organizador não cadastrado")
            except TypeError:
                self.__tela_organizador.mostrar_mensagem("Algum dado foi inserido incorretamente.")

    def mostra_organizador(self):
        if len(self.__organizadores) > 0:
            cpf_organizador = self.__tela_organizador.selecionar_organizador()
            organizador = self.pega_organizador_por_cpf(cpf_organizador)

            if organizador is not None:
                self.__tela_organizador.mostrar_organizador({"cpf": organizador.cpf, "nome": organizador.nome,
                                                             "data_nascimento": organizador.data_nascimento})
            else:
                self.__tela_organizador.mostrar_mensagem('ATENÇÃO: Organizador não cadastrado')
        else:
            self.__tela_organizador.mostrar_mensagem('Não há organizadores cadastrados para listar')

    def pega_organizador_por_cpf(self, cpf_organizador):
        for organizador in self.__organizadores:
            if organizador.cpf == cpf_organizador:
                return organizador
        return None

    def lista_organizadores(self):
        if len(self.__organizadores) > 0:
            for organizador in self.__organizadores:
                self.__tela_organizador.mostrar_organizador({"cpf": organizador.cpf, "nome": organizador.nome,
                                                             "data_nascimento": organizador.data_nascimento})
        else:
            self.__tela_organizador.mostrar_mensagem('Não há organizadores cadastrados para listar')

    def retornar(self):
        self.__controlador_eventos.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_organizador, 2: self.exclui_organizador, 3: self.altera_organizador,
                        4: self.mostra_organizador, 5: self.lista_organizadores, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_organizador.tela_opcoes()]()
