from src.entidade.participacao import Participacao
from src.tela.tela_participacao import TelaParticipacao


class ControladorParticipacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__participacoes = []
        self.__tela_participacao = TelaParticipacao()

    @property
    def participacoes(self):
        return self.__participacoes

    @property
    def tela_participacao(self):
        return self.__tela_participacao

    def adicionar_participacao(self):
        dados_participacao = self.__tela_participacao.pegar_dados_participacao()
        try:
            participacao = Participacao(dados_participacao["id"], dados_participacao["id_evento"],
                                        [dados_participacao["ano_evento"],
                                         dados_participacao["mes_evento"],
                                         dados_participacao["dia_evento"],
                                         dados_participacao["hora_entrada"],
                                         dados_participacao["minuto_entrada"]],
                                        dados_participacao["cpf_participante"])
            self.__participacoes.append(participacao)
            self.__tela_participacao.mostrar_mensagem('participacao adicionado na lista.')

        except TypeError:
            self.__tela_participacao.mostrar_mensagem("Algum dado foi inserido incorretamente.")

    def adicionar_horario_saida(self):
        if len(self.__participacoes) > 0:
            self.listar_participacoes()
            dados_participacao = self.__tela_participacao.selecionar_participacao()
            participacao = self.pegar_participacao(dados_participacao)
            try:
                if participacao is not None:
                    horario_saida_participacao = self.__tela_participacao.pegar_horario_saida_participacao()
                    participacao.data_horario_saida = [horario_saida_participacao["ano_evento"],
                                                       horario_saida_participacao["mes_evento"],
                                                       horario_saida_participacao["dia_evento"],
                                                       horario_saida_participacao["hora_saida"],
                                                       horario_saida_participacao["minuto_saida"]]
                    self.__tela_participacao.mostrar_mensagem('Dados de saída da participacao alterados com sucesso')
                else:
                    self.__tela_participacao.mostrar_mensagem("ATENÇÃO: Dados de saída da participacao não cadastrados")
            except TypeError:
                self.__tela_participacao.mostrar_mensagem("Algum dado foi inserido incorretamente.")
        else:
            self.__tela_participacao.mostrar_mensagem('Não há participações cadastradas')

    def excluir_participacao(self):
        self.listar_participacoes()
        if len(self.__participacoes) > 0:
            dados_participacao = self.__tela_participacao.selecionar_participacao()
            participacao = self.pegar_participacao(dados_participacao)

            if participacao is not None:
                self.__participacoes.remove(participacao)
                self.__tela_participacao.mostrar_mensagem('participacao removido na lista')
            else:
                self.__tela_participacao.mostrar_mensagem("ATENÇÃO: participação não cadastrado")

    def alterar_participacao(self):
        if len(self.__participacoes) > 0:
            self.listar_participacoes()
            dados_participacao = self.__tela_participacao.selecionar_participacao()
            participacao = self.pegar_participacao(dados_participacao)
            try:
                if participacao is not None:
                    novos_dados_participacao = self.__tela_participacao.pegar_dados_participacao()
                    participacao.id = novos_dados_participacao["id"]
                    participacao.id_evento = novos_dados_participacao["id_evento"]
                    participacao.data_horario_entrada = [novos_dados_participacao["ano_evento"],
                                                         novos_dados_participacao["mes_evento"],
                                                         novos_dados_participacao["dia_evento"],
                                                         novos_dados_participacao["hora_entrada"],
                                                         novos_dados_participacao["minuto_entrada"]]
                    participacao.cpf_participante = [novos_dados_participacao["cpf_participante"]]

                    self.__tela_participacao.mostrar_mensagem('Dados do participacao alterados com sucesso')
                else:
                    self.__tela_participacao.mostrar_mensagem("ATENÇÃO: participacão não cadastrada")
            except TypeError:
                self.__tela_participacao.mostrar_mensagem("Algum dado foi inserido incorretamente.")
        else:
            self.__tela_participacao.mostrar_mensagem('Não há participações cadastradas')

    def mostrar_participacao(self):
        if len(self.__participacoes) > 0:
            dados_participacao = self.__tela_participacao.selecionar_participacao()
            participacao = self.pegar_participacao(dados_participacao)

            if participacao is not None:
                self.__tela_participacao.mostrar_participacao({"id": participacao.id,
                                                               "id_evento": participacao.id_evento,
                                                               "cpf_participante": participacao.cpf_participante,
                                                               "data_horario_entrada": participacao.data_horario_entrada,
                                                               "data_horario_saida": participacao.data_horario_saida})
            else:
                self.__tela_participacao.mostrar_mensagem('ATENÇÃO: participacao não cadastrado')
        else:
            self.__tela_participacao.mostrar_mensagem('Não há participacoes cadastrados para listar')

    def pegar_participacao(self, dados_participacao):
        for participacao in self.__participacoes:
            if participacao.id_evento == dados_participacao["id_evento"]\
                    and participacao.cpf_participante == dados_participacao["cpf_participante"]:
                return participacao
        return None

    def listar_participacoes(self):
        if len(self.__participacoes) == 0:
            self.__tela_participacao.mostrar_mensagem('Não há participacoes cadastrados para listar')
        else:
            for participacao in self.__participacoes:
                self.__tela_participacao.mostrar_participacao({"id": participacao.id,
                                                               "id_evento": participacao.id_evento,
                                                               "cpf_participante": participacao.cpf_participante,
                                                               "data_horario_entrada": participacao.data_horario_entrada,
                                                               "data_horario_saida": participacao.data_horario_saida})

    def retornar(self):
        self.__controlador_sistema.controladores['controlador_eventos'].abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_participacao, 2: self.adicionar_horario_saida, 3: self.excluir_participacao,
                        4: self.alterar_participacao, 5: self.mostrar_participacao, 6: self.listar_participacoes,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_participacao.tela_opcoes()]()