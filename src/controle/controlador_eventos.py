from datetime import datetime

from src.controle.controlador_locais import ControladorLocal
from src.controle.controlador_organizadores import ControladorOrganizador
from src.controle.controlador_participantes import ControladorParticipante
from src.controle.controlador_participacoes import ControladorParticipacao
from src.entidade.evento import Evento
from src.tela.tela_evento import TelaEvento
from src.tela.tela_participacao import TelaParticipacao


class ControladorEvento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_locais = ControladorLocal(self)
        self.__controlador_organizadores = ControladorOrganizador(self)
        self.__controlador_participantes = ControladorParticipante(self)
        self.__controlador_participacoes = ControladorParticipacao(self)
        self.__eventos = []
        self.__tela_evento = TelaEvento()
        self.__tela_participacao = TelaParticipacao()

    def adiciona_evento(self):
        dados_evento = self.__tela_evento.pegar_dados_evento(
            self.__controlador_locais.locais,
            self.__controlador_organizadores.organizadores
        )
        try:
            organizadores = self.__controlador_organizadores.organizadores
            organizadores_incluidos = list(map(lambda op: organizadores[op - 1], dados_evento['opcoes_organizador']))

            evento = Evento(dados_evento['id'],
                            dados_evento['titulo'],
                            self.__controlador_locais.locais[
                                dados_evento['opcao_local'] - 1
                                ],
                            [
                                dados_evento['ano'],
                                dados_evento['mes'],
                                dados_evento['dia'],
                                dados_evento['hora'],
                                dados_evento['minuto']
                            ],
                            dados_evento['capacidade'],
                            organizadores_incluidos)

            self.__eventos.append(evento)
            self.__tela_evento.mostrar_mensagem('Evento adicionado na lista')

        except TypeError:
            self.__tela_evento.mostrar_mensagem('Algum dado foi inserido incorretamente')

    def exclui_evento(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                self.__eventos.remove(evento)
                self.__tela_evento.mostrar_mensagem('Evento removido da lista')
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')

    def altera_evento(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)
            try:
                if evento is not None:
                    novos_dados_evento = self.__tela_evento.pegar_dados_evento(
                        self.__controlador_locais.locais,
                        self.__controlador_organizadores.organizadores
                    )
                    organizadores = self.__controlador_organizadores.organizadores
                    organizadores_incluidos = list(
                        map(lambda op: organizadores[op - 1], novos_dados_evento['opcoes_organizador'])
                    )

                    evento.id = novos_dados_evento['id']
                    evento.titulo = novos_dados_evento['nome']
                    evento.local = self.__controlador_locais.locais[
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

    def mostra_evento(self):
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                self.__tela_evento.mostrar_detalhes_evento({
                    'id': evento.cpf,
                    'titulo': evento.nome,
                    'local': evento.local,
                    'data_horario_evento': evento.data_horario_evento,
                    'capacidade': evento.capacidade,
                })
                self.__tela_evento.mostrar_organizadores(evento.organizadores)
                self.__tela_evento.mostrar_participantes(evento.participantes)
                # self.__tela_evento.mostra_participacoes(evento.participacoes)
            else:
                self.__tela_evento.mostrar_mensagem('ATENÇÃO: Evento não cadastrado')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def pega_evento_por_id(self, id_evento):
        for evento in self.__eventos:
            if evento.id == id_evento:
                return evento
        return None

    def lista_eventos(self):
        if len(self.__eventos) > 0:
            for evento in self.__eventos:
                self.__tela_evento.mostrar_detalhes_evento({
                    'id': evento.cpf,
                    'titulo': evento.nome,
                    'local': evento.local,
                    'data_horario_evento': evento.data_horario_evento,
                    'capacidade': evento.capacidade,
                })
                self.__tela_evento.mostrar_organizadores(evento.organizadores)
                self.__tela_evento.mostrar_participantes(evento.participantes)
                # self.__tela_evento.mostrar_participacoes(evento.participacoes)
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def lista_eventos_ocorridos(self):
        if len(self.__eventos) > 0:
            eventos_ocorridos = list(filter(lambda e: e.data_horario_evento < datetime.now(), self.__eventos))
            for evento in eventos_ocorridos:
                self.__tela_evento.mostrar_detalhes_evento({
                    'id': evento.cpf,
                    'titulo': evento.nome,
                    'local': evento.local,
                    'data_horario_evento': evento.data_horario_evento,
                    'capacidade': evento.capacidade,
                })
                self.__tela_evento.mostrar_organizadores(evento.organizadores)
                self.__tela_evento.mostrar_participantes(evento.participantes)
                # self.__tela_evento.mostrar_participacoes(evento.participacoes)
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def lista_eventos_futuros(self):
        if len(self.__eventos) > 0:
            eventos_futuros = list(filter(lambda e: e.data_horario_evento > datetime.now(), self.__eventos))
            for evento in eventos_futuros:
                self.__tela_evento.mostrar_detalhes_evento({
                    'id': evento.cpf,
                    'titulo': evento.nome,
                    'local': evento.local,
                    'data_horario_evento': evento.data_horario_evento,
                    'capacidade': evento.capacidade,
                })
                self.__tela_evento.mostrar_organizadores(evento.organizadores)
                self.__tela_evento.mostrar_participantes(evento.participantes)
                # self.__tela_evento.mostrar_participacoes(evento.participacoes)
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    # eventos_rankeados = []
    # for evento in self.__eventos:
    #     eventos_rankeados.append({'nome': '', 'participacoes': len(evento.participacoes)})

    def ranking_eventos_por_publico(self):
        dados_evento = {}
        for evento in self.__eventos:
            dados_evento[f'{evento.nome}'].append(f'{len(evento.participacoes)}')

        eventos_rankeados = dict(sorted(dados_evento.items(), key=lambda item: item[1]))

        self.__tela_evento.mostrar_eventos_rankeados(eventos_rankeados)

    def adicionar_organizador(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_organizadores.lista_organizadores()
                cpf_organizador = self.__controlador_organizadores.tela_organizador.selecionar_organizador()
                # validacao
                organizador = self.__controlador_organizadores.pega_organizador_por_cpf(cpf_organizador)

                evento.adicionar_organizador(organizador)
                # validacao
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def adicionar_participante(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_participantes.lista_participantes()
                cpf_participante = self.__controlador_participantes.tela_participante.selecionar_participante()
                # validacao
                participante = self.__controlador_participantes.pega_participante_por_cpf(cpf_participante)

                evento.adicionar_participante(participante)
                # validacao
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def adicionar_participacao(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_participacoes.listar_participacoes()
                dados_participacao = self.__tela_participacao.selecionar_participacao()
                participacao = self.__controlador_participacoes.pegar_participacao(dados_participacao)
                evento.adicionar_participacao(participacao)
            else:
                self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def excluir_organizador(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_organizadores.lista_organizadores()
                cpf_organizador = self.__controlador_organizadores.tela_organizador.selecionar_organizador()
                # validacao
                organizador = self.__controlador_organizadores.pega_organizador_por_cpf(cpf_organizador)

                evento.excluir_organizador(organizador)
                # validacao
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def excluir_participante(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                self.__controlador_participantes.lista_participantes()
                cpf_participante = self.__controlador_participantes.tela_participante.selecionar_participante()
                # validacao
                participante = self.__controlador_participantes.pega_participante_por_cpf(cpf_participante)

                evento.excluir_participante(participante)
                # validacao
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    # def excluir_participacao(self):
    #     self.lista_eventos()
    #     if len(self.__eventos) > 0:
    #         id_evento = self.__tela_evento.selecionar_evento()
    #         evento = self.pega_evento_por_id(id_evento)
    #
    #         if evento is not None:
    #             self.__controlador_participacoes.lista_participacoes()
    #             id_participacao = self.__controlador_participacoes.selecionar_participacao()
    #             # validacao
    #             participacao = self.__controlador_participacoes.pega_participacao_por_id(id_participacao)
    #
    #             evento.excluir_participacao(participacao)
    #             # validacao
    #     else:
    #         self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def listar_organizadores(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                evento.listar_organizadores()
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def listar_participantes(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                evento.listar_participantes()
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    # def listar_participacoes(self):
    #     self.lista_eventos()
    #     if len(self.__eventos) > 0:
    #         id_evento = self.__tela_evento.selecionar_evento()
    #         evento = self.pega_evento_por_id(id_evento)
    #
    #         if evento is not None:
    #             evento.listar_participacoes()
    #     else:
    #         self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def lista_participantes_imunizados(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes

                for participante in participantes:
                    if participante.comprovante_saude.imunizado or participante.comprovante_saude.pcr_autorizado:
                        print('\nCPF DO PARTICIPANTE: ', participante.cpf)
                        print('NOME DO PARTICIPANTE: ', participante.nome)
                        print('DATA DE NASCIMENTO DO PARTICIPANTE: ', participante.data_nascimento.strftime('%d/%m/%Y'))
                        print('ENDEREÇO DO PARTICIPANTE: ')
                        print('Logradouro: ', participante.endereco.logradouro)
                        print('Número de endereço: ', participante.endereco.num_endereco)
                        print('CEP: ', participante.endereco.cep)
                        print('\n')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def lista_participantes_nao_imunizados(self):
        self.lista_eventos()
        if len(self.__eventos) > 0:
            id_evento = self.__tela_evento.selecionar_evento()
            evento = self.pega_evento_por_id(id_evento)

            if evento is not None:
                participantes = evento.participantes

                for participante in participantes:
                    if not (participante.comprovante_saude.imunizado or participante.comprovante_saude.pcr_autorizado):
                        print('\nCPF DO PARTICIPANTE: ', participante.cpf)
                        print('NOME DO PARTICIPANTE: ', participante.nome)
                        print('DATA DE NASCIMENTO DO PARTICIPANTE: ', participante.data_nascimento.strftime('%d/%m/%Y'))
                        print('ENDEREÇO DO PARTICIPANTE: ')
                        print('Logradouro: ', participante.endereco.logradouro)
                        print('Número de endereço: ', participante.endereco.num_endereco)
                        print('CEP: ', participante.endereco.cep)
                        print('\n')
        else:
            self.__tela_evento.mostrar_mensagem('Não há eventos cadastrados para listar')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_evento, 2: self.exclui_evento, 3: self.altera_evento,
                        4: self.mostra_evento, 5: self.lista_eventos, 9: self.__controlador_locais.abre_tela, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_evento.tela_opcoes()]()
