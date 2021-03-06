from datetime import datetime

from src.dao.participacao_dao import ParticipacaoDao
from src.entidade.enums.status_participante import StatusParticipante
from src.entidade.participacao import Participacao
from src.exceptions.exceptions import RemoveItemException, AddItemException, EventoFullCapacityException
from src.tela.tela_participacao import TelaParticipacao


class ControladorParticipacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__participacao_dao = ParticipacaoDao()
        self.__tela_participacao = TelaParticipacao()

    @property
    def participacao_dao(self):
        return self.__participacao_dao

    @property
    def participacoes(self):
        return self.__participacao_dao.get_all()

    @property
    def tela_participacao(self):
        return self.__tela_participacao

    def participacoes_dados(self):
        participacoes_ids = list(map(lambda p: p.id, self.participacoes))
        participacoes_eventos = list(map(lambda p: p.id_evento, self.participacoes))
        participacoes_participantes_nomes = list(map(lambda p: p.participante.nome, self.participacoes))

        return {
            'ids': participacoes_ids,
            'eventos': participacoes_eventos,
            'participantes': participacoes_participantes_nomes
        }

    def adicionar_participacao(self):
        eventos = self.__controlador_sistema.controladores['controlador_eventos'].eventos
        participantes = self.__controlador_sistema.controladores['controlador_participantes'].participantes

        dados_participacao = self.__tela_participacao.pegar_dados_participacao(eventos, participantes)

        if dados_participacao is None:
            return

        evento = dados_participacao['evento']
        participante = dados_participacao['participante']

        for participacao in self.participacoes:
            # Faz a verificação da existência da participação na lista
            if participacao.id == dados_participacao['id']:
                self.__tela_participacao.mostrar_mensagem('O id inserido já pertence a uma participação na lista.')
                return

            # Verifica se existe uma participação duplicada mesmo com ids de participação diferentes
            if participacao.id_evento == evento.id_evento \
                    and participacao.participante.cpf == participante.cpf:
                self.__tela_participacao.mostrar_mensagem(
                    'Uma participação desse participante no evento informado já foi cadastrada na lista.')
                return

        if dados_participacao['hora_entrada'] <= evento.data_horario_evento.hour:
            if dados_participacao['hora_entrada'] == evento.data_horario_evento.hour:
                if dados_participacao['minuto_entrada'] < evento.data_horario_evento.minute:
                    self.__tela_participacao.mostrar_mensagem('A participação não pode ser adicionada na lista pois o '
                                                              'horário de entrada informado é anterior ao horário do '
                                                              'evento.')
                    return
            else:
                self.__tela_participacao.mostrar_mensagem('A participação não pode ser adicionada na lista pois o '
                                                          'horário de entrada informado é anterior ao horário do '
                                                          'evento.')
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
                    participante
                )
                participante.status_participante = StatusParticipante.autorizado

                # Já adiciona ao evento o participante atrelado
                try:
                    evento.adicionar_participante(participante)

                except TypeError:
                    self.__tela_participacao.mostrar_mensagem('O participante é inválido.')
                except AddItemException:
                    pass
                except EventoFullCapacityException:
                    self.__tela_participacao.mostrar_mensagem('O evento já alcançou a sua capacidade máxima de '
                                                              'participantes.')
                    return

                try:
                    evento.adicionar_participacao(participacao)

                except TypeError:
                    self.__tela_participacao.mostrar_mensagem('A participação é inválida.')
                except AddItemException:
                    self.__tela_participacao.mostrar_mensagem(
                        'A participação já existe na lista de participações do '
                        'evento.')

                self.__participacao_dao.add_participacao(participacao)
                self.__tela_participacao.mostrar_mensagem('Participação adicionada no evento com sucesso.')

                # Atualiza evento com participação/participante inserido
                self.__controlador_sistema.controladores['controlador_eventos'].evento_dao.update_evento(evento)

            except TypeError:
                self.__tela_participacao.mostrar_mensagem('Algum dado foi inserido incorretamente.')

        else:
            self.__tela_participacao.mostrar_mensagem('O participante não possui um '
                                                      'comprovante válido.')
            participante.status_participante = StatusParticipante.nao_autorizado

    def adicionar_horario_saida(self):
        if len(self.participacoes) > 0:
            id_participacao = self.__tela_participacao.selecionar_participacao(self.participacoes_dados())
            if id_participacao is None:
                return

            participacao = self.pegar_participacao_por_id(id_participacao)

            if participacao is not None:
                eventos = self.__controlador_sistema.controladores['controlador_eventos'].eventos
                evento = list(filter(lambda e: e.id_evento == participacao.id_evento, eventos))[0]

                try:
                    horario_saida_participacao = self.__tela_participacao.pegar_horario_saida()
                    if datetime(
                            evento.data_horario_evento.year,
                            evento.data_horario_evento.month,
                            horario_saida_participacao['dia_saida'],
                            horario_saida_participacao['hora_saida'],
                            horario_saida_participacao['minuto_saida']
                    ) > participacao.data_horario_entrada:

                        participacao.data_horario_saida = [
                            evento.data_horario_evento.year,
                            evento.data_horario_evento.month,
                            evento.data_horario_evento.day,
                            horario_saida_participacao['hora_saida'],
                            horario_saida_participacao['minuto_saida']
                        ]
                        self.__participacao_dao.update_participacao(participacao)
                        self.__tela_participacao.mostrar_mensagem('Horário de saída da participação registrado com '
                                                                  'sucesso.')
                    else:
                        self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Horário de saída informado é anterior ao '
                                                                  'horário de entrada')
                except TypeError:
                    self.__tela_participacao.mostrar_mensagem('Algum dado foi inserido incorretamente.')

            else:
                self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Participação não cadastrada.')
        else:
            self.__tela_participacao.mostrar_mensagem('Não há participações cadastradas para listar.')

    def excluir_participacao(self):
        if len(self.participacoes) > 0:
            id_participacao = self.__tela_participacao.selecionar_participacao(self.participacoes_dados())
            if id_participacao is None:
                return

            participacao = self.pegar_participacao_por_id(id_participacao)

            if participacao is not None:
                evento = self.__controlador_sistema.controladores['controlador_eventos'].pegar_evento_por_id(
                    participacao.id_evento)

                if evento is not None:
                    participacao_evento = list(filter(lambda pcao: pcao.id == id_participacao, evento.participacoes))[0]

                    try:
                        participante_evento = list(filter(
                            lambda p: p.cpf == participacao_evento.participante.cpf, evento.participantes))[0]

                        evento.excluir_participante(participante_evento)

                    except IndexError:
                        pass
                    except TypeError:
                        self.__tela_participacao.mostrar_mensagem('O participante é inválido.')
                    except RemoveItemException:
                        pass

                    try:
                        evento.excluir_participacao(participacao_evento)

                    except TypeError:
                        self.__tela_participacao.mostrar_mensagem('A participação é inválida.')
                    except RemoveItemException:
                        self.__tela_participacao.mostrar_mensagem('A participação não existe na lista de participações '
                                                                  'do evento.')

                else:
                    self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

                self.__participacao_dao.remove_participacao(participacao)
                self.__tela_participacao.mostrar_mensagem('Participação removida da lista.')

                # Atualiza evento com participação/participante removido
                self.__controlador_sistema.controladores['controlador_eventos'].evento_dao.update_evento(evento)
            else:
                self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Participação não cadastrada.')
        else:
            self.__tela_participacao.mostrar_mensagem('Não há participações cadastradas para listar.')

    def alterar_horario_entrada(self):
        if len(self.participacoes) > 0:
            id_participacao = self.__tela_participacao.selecionar_participacao(self.participacoes_dados())
            if id_participacao is None:
                return

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
                    self.__participacao_dao.update_participacao(participacao)
                    self.__tela_participacao.mostrar_mensagem('Horário de entrada da participação alterado com '
                                                              'sucesso.')

                except TypeError:
                    self.__tela_participacao.mostrar_mensagem('Algum dado foi inserido incorretamente.')

            else:
                self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Participação não cadastrada.')
        else:
            self.__tela_participacao.mostrar_mensagem('Não há participações cadastradas para listar.')

    def mostrar_participacao(self):
        if len(self.participacoes) > 0:
            id_participacao = self.__tela_participacao.selecionar_participacao(self.participacoes_dados())
            if id_participacao is None:
                return

            participacao = self.pegar_participacao_por_id(id_participacao)

            if participacao is not None:
                self.__tela_participacao.mostrar_participacao({
                    'id': participacao.id,
                    'id_evento': participacao.id_evento,
                    'data_horario_entrada': participacao.data_horario_entrada,
                    'data_horario_saida': participacao.data_horario_saida,
                    'participante': participacao.participante
                })
            else:
                self.__tela_participacao.mostrar_mensagem('ATENÇÃO: Participação não cadastrada')
        else:
            self.__tela_participacao.mostrar_mensagem('Não há participações cadastradas para listar.')

    def pegar_participacao_por_id(self, id_participacao):
        try:
            return self.__participacao_dao.get_participacao(id_participacao)
        except KeyError:
            return None

    def listar_participacoes(self):
        if len(self.participacoes) > 0:
            for participacao in self.participacoes:
                self.__tela_participacao.mostrar_participacao({
                    'id': participacao.id,
                    'id_evento': participacao.id_evento,
                    'data_horario_entrada': participacao.data_horario_entrada,
                    'data_horario_saida': participacao.data_horario_saida,
                    'participante': participacao.participante
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
