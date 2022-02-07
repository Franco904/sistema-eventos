from datetime import datetime

from src.entidade.enums.status_participante import StatusParticipante
from src.entidade.evento import Evento
from src.entidade.local import Local
from src.entidade.organizador import Organizador
from src.tela.tela_evento import TelaEvento
from src.tela.tela_participacao import TelaParticipacao


class ControladorEvento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__eventos = []
        self.__tela_evento = TelaEvento()
        self.__tela_participacao = TelaParticipacao()

    @property
    def eventos(self):
        return self.__eventos

    @property
    def tela_evento(self):
        return self.__tela_evento

    def adicionar_evento(self):
        # dados_evento = self.__tela_evento.pegar_dados_evento(
        #     self.__controlador_sistema.controladores['controlador_locais'].locais,
        #     self.__controlador_sistema.controladores['controlador_organizadores'].organizadores
        # )
        try:
            # organizadores = self.__controlador_sistema.controladores['controlador_organizadores'].organizadores
            # organizadores_incluidos = list(map(lambda op: organizadores[op - 1], dados_evento['opcoes_organizador']))

            # evento = Evento(dados_evento['id_evento'],
            #                 dados_evento['titulo'],
            #                 self.__controlador_sistema.controladores['controlador_locais'].locais[
            #                     dados_evento['opcao_local'] - 1
            #                 ],
            #                 [
            #                     dados_evento['ano'],
            #                     dados_evento['mes'],
            #                     dados_evento['dia'],
            #                     dados_evento['hora'],
            #                     dados_evento['minuto']
            #                 ],
            #                 dados_evento['capacidade'],
            #                 organizadores_incluidos)
            evento = Evento(1,
                            'Festival',
                            Local(1, 'Local 1'),
                            [
                                2022,
                                3,
                                1,
                                14,
                                00
                            ],
                            500,
                            [Organizador('12833158904', 'Franco', [2003, 9, 4]),
                             Organizador('12833158905', 'Fulano', [1950, 12, 2])])

            self.__eventos.append(evento)
            self.__tela_evento.mostrar_mensagem('Evento adicionado na lista')

        except TypeError:
            self.__tela_evento.mostrar_mensagem('Algum dado foi inserido incorretamente')

    def excluir_evento(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                self.__eventos.remove(evento)
                self.__tela_evento.mostrar_mensagem('Evento removido da lista')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')

    def alterar_evento(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)
            try:
                if evento is not None:
                    novos_dados_evento = self.__tela_evento.pegar_dados_evento(
                        self.__controlador_sistema.controladores['controlador_locais'].locais,
                        self.__controlador_sistema.controladores['controlador_organizadores'].organizadores
                    )
                    organizadores = self.__controlador_sistema.controladores['controlador_organizadores'].organizadores
                    organizadores_incluidos = list(
                        map(lambda op: organizadores[op - 1], novos_dados_evento['opcoes_organizador'])
                    )

                    evento.id_evento = novos_dados_evento['id_evento']
                    evento.titulo = novos_dados_evento['nome']
                    evento.local = self.__controlador_sistema.controladores['controlador_locais'].locais[
                        novos_dados_evento['opcao_local'] - 1
                        ]
                    evento.data_horario_evento = [
                        novos_dados_evento['ano'],
                        novos_dados_evento['mes'],
                        novos_dados_evento['dia'],
                        novos_dados_evento['hora'],
                        novos_dados_evento['minuto']
                    ]
                    evento.capacidade = novos_dados_evento['capacidade']
                    evento.organizadores = organizadores_incluidos

                    self.__tela_evento.mostrar_mensagem('Dados do evento alterados com sucesso')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')

            except TypeError:
                self.__tela_evento.mostrar_mensagem('Algum dado foi inserido incorretamente')

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
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def pegar_evento_por_id(self, id_evento):
        for evento in self.__eventos:
            if evento.id_evento == id_evento:
                return evento
        return None

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
            return True
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')
            return False

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
                self.__tela_evento.mostrar_mensagem('Não há eventos ocorridos para listar')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

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
                self.__tela_evento.mostrar_mensagem('Não há eventos futuros para listar')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

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
                    self.__tela_evento.mostrar_mensagem('Não há organizadores para listar')

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
                    self.__tela_evento.mostrar_mensagem('Não há participantes para listar')

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
                    self.__tela_evento.mostrar_mensagem('Não há participações para listar')

    def listar_participantes_autorizados(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes

                for participante in participantes:
                    if participante.status_participante == StatusParticipante.autorizado:
                        print('\nCPF DO PARTICIPANTE: ', participante.cpf)
                        print('NOME DO PARTICIPANTE: ', participante.nome)
                        print('DATA DE NASCIMENTO DO PARTICIPANTE: ', participante.data_nascimento.strftime('%d/%m/%Y'))
                        print('ENDEREÇO DO PARTICIPANTE: ')
                        print('Logradouro: ', participante.endereco.logradouro)
                        print('Número de endereço: ', participante.endereco.num_endereco)
                        print('CEP: ', participante.endereco.cep)
                        print('\n')

    def listar_participantes_nao_autorizados(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes

                for participante in participantes:
                    if participante.status_participante == StatusParticipante.nao_autorizado \
                            or participante.status_participante == StatusParticipante.a_confirmar:
                        print('\nCPF DO PARTICIPANTE: ', participante.cpf)
                        print('NOME DO PARTICIPANTE: ', participante.nome)
                        print('DATA DE NASCIMENTO DO PARTICIPANTE: ', participante.data_nascimento.strftime('%d/%m/%Y'))
                        print('ENDEREÇO DO PARTICIPANTE: ')
                        print('Logradouro: ', participante.endereco.logradouro)
                        print('Número de endereço: ', participante.endereco.num_endereco)
                        print('CEP: ', participante.endereco.cep)
                        print('\n')

    def ranking_eventos_por_publico(self):
        dados_evento = {}
        for evento in self.__eventos:
            dados_evento[f'{evento.titulo}'].append(f'{len(evento.participacoes)}')

        eventos_rankeados = dict(sorted(dados_evento.items(), key=lambda item: item[1]))

        self.__tela_evento.mostrar_eventos_rankeados(eventos_rankeados)

    def adicionar_organizador(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_sistema.controladores['controlador_organizadores'].lista_organizadores()
                cpf_organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                    .tela_organizador.selecionar_organizador()
                organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                    .pega_organizador_por_cpf(cpf_organizador)

                if organizador is not None:
                    try:
                        evento.adicionar_organizador(organizador)
                    except TypeError:
                        self.__tela_evento.mostrar_mensagem('O organizador é inválido ou já existe na lista')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Organizador não cadastrado')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')

    def adicionar_participante(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_sistema.controladores['controlador_participantes'].lista_participantes()
                cpf_participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                    .tela_participante.selecionar_participante()
                participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                    .pega_participante_por_cpf(cpf_participante)

                if participante is not None:
                    try:
                        evento.adicionar_participante(participante)
                    except TypeError:
                        self.__tela_evento.mostrar_mensagem('O participante é inválido ou já existe na lista')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Participante não cadastrado')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')

    def adicionar_participacao(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_sistema.controladores['controlador_participacoes'].listar_participacoes()
                dados_participacao = self.__controlador_sistema.controladores['controlador_participacoes'] \
                    .tela_participacao.selecionar_participacao()
                participacao = self.__controlador_sistema.controladores['controlador_participacoes'] \
                    .pegar_participacao(dados_participacao)

                if participacao is not None:
                    try:
                        evento.adicionar_participacao(participacao)
                    except TypeError:
                        self.__tela_evento.mostrar_mensagem('O participação é inválida ou já existe na lista')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Participação não cadastrada')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')

    def excluir_organizador(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_sistema.controladores['controlador_organizadores'].lista_organizadores()
                cpf_organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                    .tela_organizador.selecionar_organizador()
                organizador = self.__controlador_sistema.controladores['controlador_organizadores'] \
                    .pega_organizador_por_cpf(cpf_organizador)

                if organizador is not None:
                    try:
                        evento.excluir_organizador(organizador)
                    except TypeError:
                        self.__tela_evento.mostrar_mensagem('O organizador é inválido ou já existe na lista')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Organizador não cadastrado')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')

    def excluir_participante(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_sistema.controladores['controlador_participantes'].lista_participantes()
                cpf_participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                    .tela_participante.selecionar_participante()
                participante = self.__controlador_sistema.controladores['controlador_participantes'] \
                    .pega_participante_por_cpf(cpf_participante)

                if participante is not None:
                    try:
                        evento.excluir_participante(participante)
                    except TypeError:
                        self.__tela_evento.mostrar_mensagem('O participante é inválido ou já existe na lista')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Participante não cadastrado')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')

    def excluir_participacao(self):
        self.listar_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pegar_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_sistema.controladores['controlador_participacoes'].lista_participacoes()
                id_participacao = self.__controlador_sistema.controladores['controlador_participacoes'] \
                    .tela_participacao.selecionar_participacao()
                participacao = self.__controlador_sistema.controladores['controlador_participacoes'] \
                    .pega_participacao_por_id(id_participacao)

                if participacao is not None:
                    try:
                        evento.excluir_participacao(participacao)
                    except TypeError:
                        self.__tela_evento.mostrar_mensagem('A participação é inválida ou já existe na lista')
                else:
                    self.__tela_evento.mostrar_mensagem('ATENÇÃO: Participação não cadastrada')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.__controlador_sistema.controladores['controlador_locais'].abrir_tela,
                        2: self.__controlador_sistema.controladores['controlador_organizadores'].abrir_tela,
                        3: self.__controlador_sistema.controladores['controlador_participantes'].abrir_tela,
                        4: self.__controlador_sistema.controladores['controlador_participacoes'].abrir_tela,
                        5: self.adicionar_evento, 6: self.excluir_evento, 7: self.alterar_evento,
                        8: self.mostrar_evento,
                        9: self.listar_eventos, 10: self.listar_eventos_ocorridos, 11: self.listar_eventos_futuros,
                        12: self.listar_organizadores_evento, 13: self.listar_participantes_evento,
                        14: self.listar_participacoes_evento, 15: self.listar_participantes_autorizados,
                        16: self.listar_participantes_nao_autorizados, 17: self.ranking_eventos_por_publico,
                        18: self.adicionar_organizador, 19: self.excluir_organizador,
                        20: self.adicionar_participante, 21: self.excluir_participante,
                        22: self.adicionar_participacao, 23: self.excluir_participacao,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_evento.tela_opcoes()]()
