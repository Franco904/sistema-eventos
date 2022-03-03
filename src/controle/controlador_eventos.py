from datetime import datetime

from src.entidade.enums.status_participante import StatusParticipante
from src.entidade.evento import Evento
from src.tela.tela_evento import TelaEvento


class ControladorEvento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__eventos = []
        self.__tela_evento = TelaEvento()

    @property
    def eventos(self):
        return self.__eventos

    @property
    def tela_evento(self):
        return self.__tela_evento

    # OK
    def adicionar_evento(self):
        locais = self.__controlador_sistema.controladores['controlador_locais'].locais
        organizadores = self.__controlador_sistema.controladores['controlador_organizadores'].organizadores

        # dados_evento = self.__tela_evento.pegar_dados_evento(locais, organizadores)
        #
        # if dados_evento is None:
        #     return
        #
        # # Faz a verificação da existência do evento na lista
        # for evento in self.__eventos:
        #     if evento.id_evento == dados_evento['id_evento']:
        #         self.__tela_evento.mostrar_mensagem('O id inserido já pertence a um evento na lista.')
        #         return
        try:
            # organizadores_incluidos = list(map(lambda op: organizadores[op - 1], dados_evento['opcoes_organizador']))

            # evento = Evento(dados_evento['id_evento'],
            #                 dados_evento['titulo'],
            #                 locais[dados_evento['opcao_local'] - 1],
            #                 [
            #                     dados_evento['ano'],
            #                     dados_evento['mes'],
            #                     dados_evento['dia'],
            #                     dados_evento['hora'],
            #                     dados_evento['minuto']
            #                 ],
            #                 dados_evento['capacidade'],
            #                 organizadores_incluidos)

            evento = Evento(
                1,
                'Evento 1',
                locais[0],
                [2022, 2, 2, 14, 40],
                500,
                [organizadores[0]]
            )

            self.__eventos.append(evento)
            self.__tela_evento.mostrar_mensagem('Evento adicionado na lista.')

        except TypeError:
            self.__tela_evento.mostrar_mensagem('Algum dado foi inserido incorretamente.')

    # OK
    def excluir_evento(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                self.__eventos.remove(evento)
                self.__tela_evento.mostrar_mensagem('Evento removido da lista.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # OK
    def alterar_evento(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)
            try:
                if evento is not None:
                    locais = self.__controlador_sistema.controladores['controlador_locais'].locais
                    organizadores = self.__controlador_sistema.controladores['controlador_organizadores'].organizadores

                    novos_dados_evento = self.__tela_evento.pegar_dados_evento(locais, organizadores)

                    if novos_dados_evento is None:
                        return

                    # Faz a verificação da existência do evento na lista e deixa alterar se for o id atual
                    for e in self.__eventos:
                        if e.id_evento == novos_dados_evento['id_evento']\
                                and evento.id_evento != novos_dados_evento['id_evento']:
                            self.__tela_evento.mostrar_mensagem('O id inserido já pertence a um evento na lista.')
                            return

                    organizadores_incluidos = list(
                        map(lambda op: organizadores[op - 1], novos_dados_evento['opcoes_organizador'])
                    )

                    evento.id_evento = novos_dados_evento['id_evento']
                    evento.titulo = novos_dados_evento['titulo']
                    evento.local = locais[novos_dados_evento['opcao_local'] - 1]
                    evento.data_horario_evento = [
                        novos_dados_evento['ano'],
                        novos_dados_evento['mes'],
                        novos_dados_evento['dia'],
                        novos_dados_evento['hora'],
                        novos_dados_evento['minuto']
                    ]
                    evento.capacidade = novos_dados_evento['capacidade']
                    evento.organizadores = organizadores_incluidos

                    self.__tela_evento.mostrar_mensagem('Dados do evento alterados com sucesso.')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

            except TypeError:
                self.__tela_evento.mostrar_mensagem('Algum dado foi inserido incorretamente.')

    # OK
    def mostrar_evento(self):
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                self.__tela_evento.mostrar_detalhes_evento({
                    'id_evento': evento.id_evento,
                    'titulo': evento.titulo,
                    'local': evento.local,
                    'data_horario_evento': evento.data_horario_evento,
                    'capacidade': evento.capacidade,
                })
                self.__tela_evento.mostrar_organizadores(evento.organizadores)
                self.__tela_evento.mostrar_participantes(evento.participantes)
                self.__tela_evento.mostrar_participacoes(evento.participacoes)
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    # OK
    def pegar_evento_por_id(self, id_evento):
        for evento in self.__eventos:
            if evento.id_evento == id_evento:
                return evento
        return None

    # OK
    def listar_eventos(self):
        if len(self.__eventos) > 0:
            for evento in self.__eventos:
                self.__tela_evento.mostrar_detalhes_evento({
                    'id_evento': evento.id_evento,
                    'titulo': evento.titulo,
                    'local': evento.local,
                    'data_horario_evento': evento.data_horario_evento,
                    'capacidade': evento.capacidade,
                })
                self.__tela_evento.mostrar_organizadores(evento.organizadores)
                self.__tela_evento.mostrar_participantes(evento.participantes)
                self.__tela_evento.mostrar_participacoes(evento.participacoes)
            # return True
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')
            # return False

    # OK
    def listar_eventos_ocorridos(self):
        if len(self.__eventos) > 0:
            eventos_ocorridos = list(filter(lambda e: e.data_horario_evento < datetime.now(), self.__eventos))

            if len(eventos_ocorridos) > 0:
                for evento in eventos_ocorridos:
                    self.__tela_evento.mostrar_detalhes_evento({
                        'id_evento': evento.id_evento,
                        'titulo': evento.titulo,
                        'local': evento.local,
                        'data_horario_evento': evento.data_horario_evento,
                        'capacidade': evento.capacidade,
                    })
                    self.__tela_evento.mostrar_organizadores(evento.organizadores)
                    self.__tela_evento.mostrar_participantes(evento.participantes)
                    self.__tela_evento.mostrar_participacoes(evento.participacoes)
            else:
                self.__tela_evento.mostrar_mensagem('Não há eventos ocorridos para listar.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    # OK
    def listar_eventos_futuros(self):
        if len(self.__eventos) > 0:
            eventos_futuros = list(filter(lambda e: e.data_horario_evento > datetime.now(), self.__eventos))

            if len(eventos_futuros) > 0:
                for evento in eventos_futuros:
                    self.__tela_evento.mostrar_detalhes_evento({
                        'id_evento': evento.id_evento,
                        'titulo': evento.titulo,
                        'local': evento.local,
                        'data_horario_evento': evento.data_horario_evento,
                        'capacidade': evento.capacidade,
                    })
                    self.__tela_evento.mostrar_organizadores(evento.organizadores)
                    self.__tela_evento.mostrar_participantes(evento.participantes)
                    self.__tela_evento.mostrar_participacoes(evento.participacoes)
            else:
                self.__tela_evento.mostrar_mensagem('Não há eventos futuros para listar.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    # ANALISAR
    def ranking_eventos_por_publico(self):
        dados_evento = {}

        if len(self.__eventos) > 0:
            for evento in self.__eventos:
                dados_evento[f'{evento.titulo}'].append(f'{len(evento.participacoes)}')

            eventos_rankeados = dict(sorted(dados_evento.items(), key=lambda item: item[1]))

            self.__tela_evento.mostrar_eventos_rankeados(eventos_rankeados)
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    # OK
    def listar_organizadores_evento(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                organizadores = evento.organizadores

                if len(organizadores) > 0:
                    self.__tela_evento.listar_organizadores_evento(organizadores)
                else:
                    self.__tela_evento.mostrar_mensagem('Não há organizadores para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # ANALISAR
    def listar_participantes_evento(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes

                if len(participantes) > 0:
                    self.__tela_evento.listar_participantes_evento(participantes)
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participantes para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # ANALISAR
    def listar_participacoes_evento(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participacoes = evento.participacoes

                if len(participacoes) > 0:
                    self.__tela_evento.listar_participacoes_evento(participacoes)
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participações para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # ANALISAR
    def listar_participantes_com_comprovante(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes
                if len(participantes) > 0:
                    participantes_com_comprovante = list(filter(
                        lambda p: p.status_participante == StatusParticipante.autorizado
                        or p.status_participante == StatusParticipante.nao_autorizado, participantes))

                    self.__tela_evento.listar_participantes_evento(participantes_com_comprovante)
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participantes para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # ANALISAR
    def listar_participantes_sem_comprovante(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes

                if len(participantes) > 0:
                    participantes_sem_comprovante = list(filter(
                        lambda p: p.status_participante == StatusParticipante.a_confirmar, participantes))

                    self.__tela_evento.listar_participantes_evento(participantes_sem_comprovante)
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participantes para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # OK
    def adicionar_organizador(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                organizadores = self.__controlador_sistema.controladores['controlador_organizadores'].organizadores
                if len(evento.organizadores) == len(organizadores):
                    self.__tela_evento.mostrar_mensagem('Todos os organizadores cadastrados já foram inseridos na '
                                                        'lista.')
                    return

                self.__controlador_sistema.controladores['controlador_organizadores'].listar_organizadores()
                cpf_organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                    .tela_organizador.selecionar_organizador()
                organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                    .pegar_organizador_por_cpf(cpf_organizador)

                if organizador is not None:
                    try:
                        evento.adicionar_organizador(organizador)
                        self.__tela_evento.mostrar_mensagem('Organizador adicionado na lista.')
                    except TypeError:
                        self.__tela_evento.mostrar_mensagem('O organizador é inválido ou já existe na lista.')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Organizador não cadastrado.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # ANALISAR
    def adicionar_participante(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = self.__controlador_sistema.controladores['controlador_participantes'].participantes
                if len(evento.participantes) == len(participantes):
                    self.__tela_evento.mostrar_mensagem('Todos os participantes cadastrados já foram inseridos na '
                                                        'lista.')
                    return

                self.__controlador_sistema.controladores['controlador_participantes'].listar_participantes()
                cpf_participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                    .tela_participante.selecionar_participante()
                participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                    .pegar_participante_por_cpf(cpf_participante)

                if participante is not None:
                    try:
                        evento.adicionar_participante(participante)
                        self.__tela_evento.mostrar_mensagem('Participante adicionado na lista.')
                    except TypeError:
                        self.__tela_evento.mostrar_mensagem('O participante é inválido ou já existe na lista.')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Participante não cadastrado.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # ANALISAR
    def adicionar_participacao(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participacoes = self.__controlador_sistema.controladores['controlador_participacoes'].participacoes
                if len(evento.participacoes) == len(participacoes):
                    self.__tela_evento.mostrar_mensagem('Todos as participacões cadastradas já foram inseridas na '
                                                        'lista.')
                    return

                self.__controlador_sistema.controladores['controlador_participacoes'].listar_participacoes()
                dados_participacao = self.__controlador_sistema.controladores['controlador_participacoes'] \
                    .tela_participacao.selecionar_participacao()
                participacao = self.__controlador_sistema.controladores['controlador_participacoes'] \
                    .pegar_participacao(dados_participacao)

                if participacao is not None:
                    try:
                        evento.adicionar_participacao(participacao)
                        self.__tela_evento.mostrar_mensagem('Participação adicionada na lista.')
                    except TypeError:
                        self.__tela_evento.mostrar_mensagem('O participação é inválida ou já existe na lista.')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Participação não cadastrada.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # OK
    def excluir_organizador(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                organizadores = evento.organizadores
                if len(organizadores) > 0:
                    self.__tela_evento.listar_organizadores_evento(organizadores)

                    cpf_organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                        .tela_organizador.selecionar_organizador()
                    organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                        .pegar_organizador_por_cpf(cpf_organizador)

                    if organizador is not None:
                        try:
                            evento.excluir_organizador(organizador)
                            self.__tela_evento.mostrar_mensagem('Organizador excluído da lista.')
                        except (KeyError, TypeError):
                            self.__tela_evento.mostrar_mensagem('O organizador é inválido ou não existe na lista.')
                    else:
                        self.__tela_evento.mostrar_mensagem('ATENÇÃO: Organizador não cadastrado.')
                else:
                    self.__tela_evento.mostrar_mensagem('Não há organizadores para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # ANALISAR
    def excluir_participante(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes
                if len(participantes) > 0:
                    self.__tela_evento.listar_participantes_evento(participantes)

                    cpf_participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                        .tela_participante.selecionar_participante()
                    participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                        .pegar_participante_por_cpf(cpf_participante)

                    if participante is not None:
                        try:
                            evento.excluir_participante(participante)
                            self.__tela_evento.mostrar_mensagem('Participante excluído da lista.')
                        except (KeyError, TypeError):
                            self.__tela_evento.mostrar_mensagem('O participante é inválido ou não existe na lista.')
                    else:
                        self.__tela_evento.mostrar_mensagem('ATENÇÃO: Participante não cadastrado.')
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participantes para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # ANALISAR
    def excluir_participacao(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participacoes = evento.participacoes
                if len(participacoes) > 0:
                    self.__tela_evento.listar_participacoes_evento(participacoes)

                    id_participacao = self.__controlador_sistema.controladores['controlador_participacoes'] \
                        .tela_participacao.selecionar_participacao()
                    participacao = self.__controlador_sistema.controladores['controlador_participacoes'] \
                        .pegar_participacao_por_id(id_participacao)

                    if participacao is not None:
                        try:
                            evento.excluir_participacao(participacao)
                            self.__tela_evento.mostrar_mensagem('Participação excluída da lista.')
                        except TypeError:
                            self.__tela_evento.mostrar_mensagem('A participação é inválida ou não existe na lista.')
                    else:
                        self.__tela_evento.mostrar_mensagem('ATENÇÃO: Participação não cadastrada.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')

    # OK
    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    # OK
    def abrir_tela(self):
        lista_opcoes = {1: self.adicionar_evento,
                        2: self.excluir_evento,
                        3: self.alterar_evento,
                        4: self.mostrar_evento,
                        5: self.listar_eventos,
                        6: self.listar_eventos_ocorridos,
                        7: self.listar_eventos_futuros,
                        8: self.ranking_eventos_por_publico,
                        9: self.listar_organizadores_evento,
                        10: self.listar_participantes_evento,
                        11: self.listar_participacoes_evento,
                        12: self.listar_participantes_com_comprovante,
                        13: self.listar_participantes_sem_comprovante,
                        14: self.adicionar_organizador,
                        15: self.excluir_organizador,
                        16: self.adicionar_participante,
                        17: self.excluir_participante,
                        18: self.adicionar_participacao,
                        19: self.excluir_participacao,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_evento.tela_opcoes()]()
