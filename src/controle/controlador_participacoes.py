from src.entidade.enums.status_participante import StatusParticipante
from src.entidade.participacao import Participacao
from src.tela.tela_participacao import TelaParticipacao
from datetime import datetime


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
        eventos = self.__controlador_sistema.controladores['controlador_eventos'].eventos
        participantes = self.__controlador_sistema.controladores['controlador_participantes'].participantes

        dados_participacao = self.__tela_participacao.pegar_dados_participacao(eventos, participantes)

        if dados_participacao is None:
            return

        evento = eventos[dados_participacao['opcao_evento'] - 1]
        participante = participantes[dados_participacao['opcao_participante'] - 1]

        for participacao in self.__participacoes:
            # Faz a verificação da existência da participação na lista
            if participacao.id == dados_participacao['id']:
                self.__tela_participacao.mostrar_mensagem('O id inserido já pertence a uma participação na lista.')
                return

            # Verifica se existe uma participação duplicada mesmo com ids de participação diferentes
            if participacao.id_evento == evento.id_evento \
                    and participacao.cpf_participante == participante.cpf:
                self.__tela_participacao.mostrar_mensagem(
                    'Uma participação desse participante no evento informado já foi cadastrada na lista.')
                return

        if dados_participacao['hora_entrada'] <= evento.data_horario_evento.hour:
            if dados_participacao['hora_entrada'] == evento.data_horario_evento.hour:
                if dados_participacao['minuto_entrada'] < evento.data_horario_evento.minute:
                    self.__tela_participacao.mostrar_mensagem('A participação não pode ser adicionada na lista pois o '
                                                              'horário de entrada informado é anterior ao horário do evento.')
                    return
            else:
                self.__tela_participacao.mostrar_mensagem('A participação não pode ser adicionada na lista pois o '
                                                          'horário de entrada informado é anterior ao horário do evento.')
                return
        # Verifica se o participante está autorizado a entrar no evento
        if participante.comprovante_saude is None:
            participante.status_participante = StatusParticipante.a_confirmar
            self.__tela_participacao.mostrar_mensagem('A participação não pode ser adicionada na lista pois o '
                                                      'participante não possui um comprovante de saúde cadastrado.')
            self.__tela_participacao.mostrar_mensagem('Acesse a tela de participantes e cadastre um comprovante de '
                                                      'saúde para esse participante')

        elif participante.comprovante_saude.imunizado() or participante.comprovante_saude.pcr_autorizado([
            evento.data_horario_evento.year,
            evento.data_horario_evento.month,
            evento.data_horario_evento.day,
            evento.data_horario_evento.hour,
            evento.data_horario_evento.minute
        ]):

            try:
                participacao = Participacao(
                    dados_participacao['id'],
                    evento.id_evento,
                    [
                        evento.data_horario_evento.year,
                        evento.data_horario_evento.month,
                        evento.data_horario_evento.day,
                        dados_participacao['hora_entrada'],
                        dados_participacao['minuto_entrada']
                    ],
                    participante.cpf
                )
                participante.status_participante = StatusParticipante.autorizado
                self.__participacoes.append(participacao)
                self.__tela_participacao.mostrar_mensagem('Participação adicionada na lista.')

            except TypeError:
                self.__tela_participacao.mostrar_mensagem('Algum dado foi inserido incorretamente.')

        else:
            self.__tela_participacao.mostrar_mensagem('O participante não possui um '
                                                      'comprovante válido.')
            participante.status_participante = StatusParticipante.nao_autorizado

    def adicionar_horario_saida(self):
        self.listar_participacoes()

        if len(self.__participacoes) > 0:
            id_participacao = self.__tela_participacao.selecionar_participacao()
            participacao = self.pegar_participacao_por_id(id_participacao)

            if participacao is not None:
                eventos = self.__controlador_sistema.controladores['controlador_eventos'].eventos
                evento = list(filter(lambda e: e.id_evento == participacao.id_evento, eventos))[0]

                try:
                    horario_saida_participacao = self.__tela_participacao.pegar_horario_saida()
                    if datetime(evento.data_horario_evento.year, evento.data_horario_evento.month, horario_saida_participacao['dia_saida'], horario_saida_participacao['hora_saida'], horario_saida_participacao['minuto_saida']) > participacao.data_horario_entrada:
                        participacao.data_horario_saida = [
                            evento.data_horario_evento.year,
                            evento.data_horario_evento.month,
                            evento.data_horario_evento.day,
                            horario_saida_participacao['hora_saida'],
                            horario_saida_participacao['minuto_saida']
                        ]
                        self.__tela_participacao.mostrar_mensagem('Horário de saída da participação registrado com '
                                                                  'sucesso.')
                    else:
                        self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Horário de saída informado é anterior ao horário de entrada')
                except TypeError:
                    self.__tela_participacao.mostrar_mensagem('Algum dado foi inserido incorretamente.')

            else:
                self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Participação não cadastrada.')

    def excluir_participacao(self):
        self.listar_participacoes()

        if len(self.__participacoes) > 0:
            id_participacao = self.__tela_participacao.selecionar_participacao()
            participacao = self.pegar_participacao_por_id(id_participacao)

            if participacao is not None:
                self.__participacoes.remove(participacao)
                self.__tela_participacao.mostrar_mensagem('Participação removida da lista.')

            else:
                self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Participação não cadastrada.')

    def alterar_horario_entrada(self):
        self.listar_participacoes()

        if len(self.__participacoes) > 0:
            id_participacao = self.__tela_participacao.selecionar_participacao()
            participacao = self.pegar_participacao_por_id(id_participacao)

            if participacao is not None:
                novos_dados_participacao = self.__tela_participacao.alterar_horario_entrada()

                if novos_dados_participacao is None:
                    return

                eventos = self.__controlador_sistema.controladores['controlador_eventos'].eventos
                evento = list(filter(lambda e: e.id_evento == participacao.id_evento, eventos))[0]

                try:
                    participacao.data_horario_entrada = [
                        evento.data_horario_evento.year,
                        evento.data_horario_evento.month,
                        evento.data_horario_evento.day,
                        novos_dados_participacao['hora_entrada'],
                        novos_dados_participacao['minuto_entrada']
                    ]
                    self.__tela_participacao.mostrar_mensagem('Horário de entrada da participação alterado com '
                                                              'sucesso.')

                except TypeError:
                    self.__tela_participacao.mostrar_mensagem('Algum dado foi inserido incorretamente.')

            else:
                self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Participação não cadastrada.')

    def mostrar_participacao(self):
        if len(self.__participacoes) > 0:
            id_participacao = self.__tela_participacao.selecionar_participacao()
            participacao = self.pegar_participacao_por_id(id_participacao)

            if participacao is not None:
                self.__tela_participacao.mostrar_participacao({
                    'id': participacao.id,
                    'id_evento': participacao.id_evento,
                    'data_horario_entrada': participacao.data_horario_entrada,
                    'data_horario_saida': participacao.data_horario_saida,
                    'cpf_participante': participacao.cpf_participante
                })
            else:
                self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Participação não cadastrada')
        else:
            self.__tela_participacao.mostrar_mensagem('Não há participações cadastradas para listar.')

    def pegar_participacao_por_id(self, id_participacao):
        for participacao in self.__participacoes:
            if participacao.id == id_participacao:
                return participacao
        return None

    def listar_participacoes(self):
        if len(self.__participacoes) > 0:
            for participacao in self.__participacoes:
                self.__tela_participacao.mostrar_participacao({
                    'id': participacao.id,
                    'id_evento': participacao.id_evento,
                    'data_horario_entrada': participacao.data_horario_entrada,
                    'data_horario_saida': participacao.data_horario_saida,
                    'cpf_participante': participacao.cpf_participante
                })
        else:
            self.__tela_participacao.mostrar_mensagem('Não há participações cadastradas para listar.')

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.adicionar_participacao,
                        2: self.adicionar_horario_saida,
                        3: self.excluir_participacao,
                        4: self.alterar_horario_entrada,
                        5: self.mostrar_participacao,
                        6: self.listar_participacoes,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_participacao.tela_opcoes()]()
