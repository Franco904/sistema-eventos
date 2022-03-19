from datetime import datetime

from src.dao.evento_dao import EventoDao
from src.entidade.evento import Evento
from src.exceptions.exceptions import RemoveItemException, AddItemException, EventoFullCapacityException
from src.tela.tela_evento import TelaEvento


class ControladorEvento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__evento_dao = EventoDao()
        self.__tela_evento = TelaEvento()

    @property
    def evento_dao(self):
        return self.__evento_dao

    @property
    def eventos(self):
        return self.__evento_dao.get_all()

    @property
    def tela_evento(self):
        return self.__tela_evento

    def adicionar_evento(self):
        locais = self.__controlador_sistema.controladores['controlador_locais'].locais
        organizadores = self.__controlador_sistema.controladores['controlador_organizadores'].organizadores

        dados_evento = self.__tela_evento.pegar_dados_evento(locais, organizadores, False)

        if dados_evento is None:
            return

        # Faz a verificação da existência do evento na lista
        for evento in self.eventos:
            if evento.id_evento == dados_evento['id_evento']:
                self.__tela_evento.mostrar_mensagem('O id inserido já pertence a um evento na lista.')
                return

        try:
            evento = Evento(dados_evento['id_evento'],
                            dados_evento['titulo'],
                            dados_evento['local'],
                            [
                                dados_evento['ano'],
                                dados_evento['mes'],
                                dados_evento['dia'],
                                dados_evento['hora'],
                                dados_evento['minuto']
                            ],
                            dados_evento['capacidade'],
                            dados_evento['organizadores'])

            self.__evento_dao.add_evento(evento)
            self.__tela_evento.mostrar_mensagem('Evento adicionado na lista.')

        except TypeError:
            self.__tela_evento.mostrar_mensagem('Algum dado foi inserido incorretamente.')

    def excluir_evento(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                controlador_participacoes = self.__controlador_sistema.controladores['controlador_participacoes']
                participacoes = controlador_participacoes.participacoes

                participacoes_excluir = list(filter(lambda p: p.id_evento == id_evento, participacoes))

                self.__evento_dao.remove_evento(evento)
                self.__tela_evento.mostrar_mensagem('Evento removido da lista.')

                # Exclui as participações que estão associadas ao evento recém excluído
                for participacao in participacoes_excluir:
                    controlador_participacoes.participacao_dao.remove_participacao(participacao)
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def alterar_evento(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                locais = self.__controlador_sistema.controladores['controlador_locais'].locais
                organizadores = self.__controlador_sistema.controladores['controlador_organizadores'].organizadores

                novos_dados_evento = self.__tela_evento.pegar_dados_evento(locais, organizadores, True)

                if novos_dados_evento is None:
                    return

                try:
                    evento.titulo = novos_dados_evento['titulo']
                    evento.local = novos_dados_evento['local']
                    evento.data_horario_evento = [
                        novos_dados_evento['ano'],
                        novos_dados_evento['mes'],
                        novos_dados_evento['dia'],
                        novos_dados_evento['hora'],
                        novos_dados_evento['minuto']
                    ]
                    evento.capacidade = novos_dados_evento['capacidade']
                    evento.organizadores = novos_dados_evento['organizadores']

                    self.__evento_dao.update_evento(evento)
                    self.__tela_evento.mostrar_mensagem('Dados do evento alterados com sucesso.')

                except TypeError:
                    self.__tela_evento.mostrar_mensagem('Algum dado foi inserido incorretamente.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def mostrar_evento(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                self.__tela_evento.mostrar_detalhes_evento({
                    'id_evento': evento.id_evento,
                    'titulo': evento.titulo,
                    'local': evento.local,
                    'data_horario_evento': evento.data_horario_evento,
                    'capacidade': evento.capacidade,
                    'organizadores': self.montar_organizador_string(evento.organizadores),
                    'participantes': self.montar_participante_string(evento.participantes),
                    'participacoes': self.montar_participacao_string(evento.participacoes)
                })
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def pegar_evento_por_id(self, id_evento):
        try:
            return self.__evento_dao.get_evento(id_evento)
        except KeyError:
            return None

    def listar_eventos(self):
        if len(self.eventos) > 0:
            for evento in self.eventos:
                self.__tela_evento.mostrar_detalhes_evento({
                    'id_evento': evento.id_evento,
                    'titulo': evento.titulo,
                    'local': evento.local,
                    'data_horario_evento': evento.data_horario_evento,
                    'capacidade': evento.capacidade,
                    'organizadores': evento.organizadores,
                    'participantes': evento.participantes,
                    'participacoes': evento.participacoes
                })

            return True
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')
            return False

    def listar_eventos_ocorridos(self):
        if len(self.eventos) > 0:
            eventos_ocorridos = list(filter(lambda e: e.data_horario_evento < datetime.now(), self.eventos))

            if len(eventos_ocorridos) > 0:
                for evento in eventos_ocorridos:
                    self.__tela_evento.mostrar_detalhes_evento({
                        'id_evento': evento.id_evento,
                        'titulo': evento.titulo,
                        'local': evento.local,
                        'data_horario_evento': evento.data_horario_evento,
                        'capacidade': evento.capacidade,
                        'organizadores': evento.organizadores,
                        'participantes': evento.participantes,
                        'participacoes': evento.participacoes
                    })
            else:
                self.__tela_evento.mostrar_mensagem('Não há eventos ocorridos para listar.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def listar_eventos_futuros(self):
        if len(self.eventos) > 0:
            eventos_futuros = list(filter(lambda e: e.data_horario_evento > datetime.now(), self.eventos))

            if len(eventos_futuros) > 0:
                for evento in eventos_futuros:
                    self.__tela_evento.mostrar_detalhes_evento({
                        'id_evento': evento.id_evento,
                        'titulo': evento.titulo,
                        'local': evento.local,
                        'data_horario_evento': evento.data_horario_evento,
                        'capacidade': evento.capacidade,
                        'organizadores': evento.organizadores,
                        'participantes': evento.participantes,
                        'participacoes': evento.participacoes
                    })
            else:
                self.__tela_evento.mostrar_mensagem('Não há eventos futuros para listar.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def ranking_eventos_por_publico(self):
        dados_evento = {}

        if len(self.eventos) > 0:
            for evento in self.eventos:
                if len(evento.participacoes) > 0:
                    dados_evento[f'{evento.titulo}'] = (len(evento.participacoes))

            eventos_rankeados = dict(sorted(dados_evento.items(), key=lambda item: item[1], reverse=True))

            self.__tela_evento.mostrar_eventos_rankeados(eventos_rankeados)

        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def listar_organizadores_evento(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                organizadores = evento.organizadores

                if len(organizadores) > 0:
                    tela_organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                        .tela_organizador

                    for organizador in organizadores:
                        tela_organizador.mostrar_organizador({
                            'cpf': organizador.cpf,
                            'nome': organizador.nome,
                            'data_nascimento': organizador.data_nascimento
                        })
                else:
                    self.__tela_evento.mostrar_mensagem('Não há organizadores do evento para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def listar_participantes_evento(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes

                if len(participantes) > 0:
                    tela_participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                        .tela_participante

                    for participante in participantes:
                        tela_participante.mostrar_participante({
                            'cpf': participante.cpf,
                            'nome': participante.nome,
                            'data_nascimento': participante.data_nascimento,
                            'endereco': participante.endereco,
                            'status': participante.status_participante,
                            'comprovante_saude': participante.comprovante_saude
                        })
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participantes do evento para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def listar_participantes_com_comprovante(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes

                if len(participantes) > 0:
                    participantes_com_comprovante = list(
                        filter(lambda p: p.comprovante_saude is not None, participantes)
                    )

                    if len(participantes_com_comprovante) > 0:
                        tela_participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                            .tela_participante

                        for participante in participantes_com_comprovante:
                            tela_participante.mostrar_participante({
                                'cpf': participante.cpf,
                                'nome': participante.nome,
                                'data_nascimento': participante.data_nascimento,
                                'endereco': participante.endereco,
                                'status': participante.status_participante,
                                'comprovante_saude': participante.comprovante_saude
                            })
                    else:
                        self.__tela_evento.mostrar_mensagem('Não há participantes do evento com comprovante de saúde '
                                                            'para listar.')
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participantes do evento para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def listar_participantes_sem_comprovante(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes

                if len(participantes) > 0:
                    participantes_sem_comprovante = list(
                        filter(lambda p: p.comprovante_saude is None, participantes)
                    )

                    if len(participantes_sem_comprovante) > 0:
                        tela_participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                            .tela_participante

                        for participante in participantes_sem_comprovante:
                            tela_participante.mostrar_participante({
                                'cpf': participante.cpf,
                                'nome': participante.nome,
                                'data_nascimento': participante.data_nascimento,
                                'endereco': participante.endereco,
                                'status': participante.status_participante,
                                'comprovante_saude': participante.comprovante_saude
                            })
                    else:
                        self.__tela_evento.mostrar_mensagem('Não há participantes do evento sem comprovante de saúde '
                                                            'para listar.')
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participantes do evento para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def listar_participacoes_evento(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participacoes = evento.participacoes

                if len(participacoes) > 0:
                    tela_participacao = self.__controlador_sistema.controladores['controlador_participacoes'] \
                        .tela_participacao

                    for participacao in participacoes:
                        tela_participacao.mostrar_participacao({
                            'id': participacao.id,
                            'id_evento': participacao.id_evento,
                            'data_horario_entrada': participacao.data_horario_entrada,
                            'data_horario_saida': participacao.data_horario_saida,
                            'participante': participacao.participante,
                        })
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participações do evento para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def adicionar_organizador(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                organizadores = self.__controlador_sistema.controladores['controlador_organizadores'].organizadores

                if len(organizadores) > 0:
                    # Verifica se há organizadores a inserir na lista do evento
                    if len(evento.organizadores) == len(organizadores):
                        self.__tela_evento.mostrar_mensagem('Todos os organizadores cadastrados já foram inseridos na '
                                                            'lista.')
                        return

                    cpf_organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                        .tela_organizador.selecionar_organizador(organizadores)
                    if cpf_organizador is None:
                        return

                    organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                        .pegar_organizador_por_cpf(cpf_organizador)

                    if organizador is not None:
                        try:
                            evento.adicionar_organizador(organizador)
                            self.__tela_evento.mostrar_mensagem('Organizador adicionado na lista.')

                            self.__evento_dao.update_evento(evento)

                        except TypeError:
                            self.__tela_evento.mostrar_mensagem('O organizador é inválido.')
                        except AddItemException:
                            self.__tela_evento.mostrar_mensagem('O organizador já existe na lista de organizadores do '
                                                                'evento.')

                    else:
                        self.__tela_evento.mostrar_mensagem('ATENÇÃO: Organizador não cadastrado.')
                else:
                    self.__tela_evento.mostrar_mensagem('Não há organizadores para listar.')
                    self.__tela_evento.mostrar_mensagem('Acesse a tela de organizadores para cadastrar um '
                                                        'organizador.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def adicionar_participante(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = self.__controlador_sistema.controladores['controlador_participantes'].participantes

                if len(participantes) > 0:
                    # Verifica se há participantes a inserir na lista do evento
                    if len(evento.participantes) == len(participantes):
                        self.__tela_evento.mostrar_mensagem('Todos os participantes cadastrados já foram inseridos na '
                                                            'lista.')
                        return

                    cpf_participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                        .tela_participante.selecionar_participante(participantes)
                    if cpf_participante is None:
                        return

                    participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                        .pegar_participante_por_cpf(cpf_participante)

                    if participante is not None:
                        try:
                            evento.adicionar_participante(participante)
                            self.__tela_evento.mostrar_mensagem('Participante adicionado na lista.')

                            self.__evento_dao.update_evento(evento)

                        except TypeError:
                            self.__tela_evento.mostrar_mensagem('O participante é inválido.')
                        except AddItemException:
                            self.__tela_evento.mostrar_mensagem('O participante já existe na lista de participantes do '
                                                                'evento.')
                        except EventoFullCapacityException:
                            self.__tela_evento.mostrar_mensagem('O evento já alcançou a sua capacidade máxima de '
                                                                'participantes.')

                    else:
                        self.__tela_evento.mostrar_mensagem('ATENÇÃO: Participante não cadastrado.')
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participantes para listar.')
                    self.__tela_evento.mostrar_mensagem('Acesse a tela de participantes para cadastrar um '
                                                        'participante.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def excluir_organizador(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                organizadores = evento.organizadores

                if len(organizadores) > 0:
                    cpf_organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                        .tela_organizador.selecionar_organizador(organizadores)
                    if cpf_organizador is None:
                        return

                    organizador = list(filter(lambda o: o.cpf == cpf_organizador, evento.organizadores))[0]

                    try:
                        evento.excluir_organizador(organizador)
                        self.__tela_evento.mostrar_mensagem('Organizador excluído da lista.')

                        self.__evento_dao.update_evento(evento)
                    except TypeError:
                        self.__tela_evento.mostrar_mensagem('O organizador é inválido.')
                    except RemoveItemException:
                        self.__tela_evento.mostrar_mensagem('O organizador não existe na lista de organizadores do '
                                                            'evento.')

                else:
                    self.__tela_evento.mostrar_mensagem('Não há organizadores do evento para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def excluir_participante(self):
        if len(self.eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento(self.eventos)
            if id_evento is None:
                return

            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes

                if len(participantes) > 0:
                    cpf_participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                        .tela_participante.selecionar_participante(participantes)
                    if cpf_participante is None:
                        return

                    participante = list(filter(lambda p: p.cpf == cpf_participante, evento.participantes))[0]

                    if participante is not None:
                        try:
                            evento.excluir_participante(participante)
                            self.__tela_evento.mostrar_mensagem('Participante excluído da lista.')

                            self.__evento_dao.update_evento(evento)

                        except TypeError:
                            self.__tela_evento.mostrar_mensagem('O participante é inválido.')
                        except RemoveItemException:
                            self.__tela_evento.mostrar_mensagem('O participante não existe na lista de participantes '
                                                                'do evento.')

                    else:
                        self.__tela_evento.mostrar_mensagem('ATENÇÃO: Participante não cadastrado.')
                else:
                    self.__tela_evento.mostrar_mensagem('Não há participantes do evento para listar.')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado.')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar.')

    def montar_organizador_string(self, organizadores: list):
        orgString = ''
        if len(organizadores) == 0:
            orgString = 'Nenhum organizador inserido'
        else:
            for organizador in organizadores:
                if organizador.cpf == organizadores[-1].cpf:
                    orgString += organizador.nome
                else:
                    orgString += organizador.nome + ', '

        return orgString

    def montar_participante_string(self, participantes: list):
        partString = ''
        if len(participantes) == 0:
            partString = 'Nenhum participante inserido'
        else:
            for participante in participantes:
                if participante.cpf == participantes[-1].cpf:
                    partString += participante.nome
                else:
                    partString += participante.nome + ', '

        return partString

    def montar_participacao_string(self, participacoes: list):
        pcaoString = ''
        if len(participacoes) == 0:
            pcaoString = 'Nenhuma participação inserida'
        else:
            for participacao in participacoes:
                if participacao.id == participacoes[-1].id:
                    pcaoString += participacao.participante.nome
                else:
                    pcaoString += participacao.participante.nome + ', '

        return pcaoString

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.adicionar_evento,
                        2: self.excluir_evento,
                        3: self.alterar_evento,
                        4: self.mostrar_evento,
                        5: self.adicionar_organizador,
                        6: self.excluir_organizador,
                        7: self.adicionar_participante,
                        8: self.excluir_participante,
                        9: self.abrir_tela_listagens,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_evento.tela_opcoes()]()

    def abrir_tela_listagens(self):
        lista_opcoes = {1: self.listar_eventos,
                        2: self.listar_eventos_ocorridos,
                        3: self.listar_eventos_futuros,
                        4: self.ranking_eventos_por_publico,
                        5: self.listar_organizadores_evento,
                        6: self.listar_participantes_evento,
                        7: self.listar_participantes_com_comprovante,
                        8: self.listar_participantes_sem_comprovante,
                        9: self.listar_participacoes_evento,
                        0: self.retornar_para_eventos}
        continua = True
        while continua:
            lista_opcoes[self.__tela_evento.opcoes_listagem()]()

    def retornar_para_eventos(self):
        self.abrir_tela()
