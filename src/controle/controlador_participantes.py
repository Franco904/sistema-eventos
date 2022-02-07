from src.entidade.participante import Participante
from src.tela.tela_participante import TelaParticipante


class ControladorParticipante:
    def __init__(self, controlador_eventos):
        self.__controlador_eventos = controlador_eventos
        self.__participantes = []
        self.__tela_participante = TelaParticipante()

    @property
    def participantes(self):
        return self.__participantes

    @property
    def tela_participante(self):
        return self.__tela_participante

    def adiciona_participante(self):
        dados_participante = self.__tela_participante.pegar_dados_participante()
        try:
            participante = Participante(dados_participante['cpf'],
                                        dados_participante['nome'],
                                        [
                                            dados_participante['ano'],
                                            dados_participante['mes'],
                                            dados_participante['dia']
                                        ],
                                        [
                                            dados_participante['logradouro'],
                                            dados_participante['num_endereco'],
                                            dados_participante['cep']
                                        ])
            self.__participantes.append(participante)
            self.__tela_participante.mostrar_mensagem('Participante adicionado na lista')

        except TypeError:
            self.__tela_participante.mostrar_mensagem('Algum dado foi inserido incorretamente')

    def exclui_participante(self):
        self.lista_participantes()
        if len(self.__participantes) > 0:
            cpf_participante = self.__tela_participante.selecionar_participante()
            participante = self.pega_participante_por_cpf(cpf_participante)

            if participante is not None:
                self.__participantes.remove(participante)
                self.__tela_participante.mostrar_mensagem('Participante removido da lista')
            else:
                self.__tela_participante.mostrar_mensagem('ATENÇÃO: Participante não cadastrado')

    def altera_participante(self):
        self.lista_participantes()
        if len(self.__participantes) > 0:
            cpf_participante = self.__tela_participante.selecionar_participante()
            participante = self.pega_participante_por_cpf(cpf_participante)
            try:
                if participante is not None:
                    novos_dados_participante = self.__tela_participante.pegar_dados_participante()

                    participante.cpf = novos_dados_participante['cpf']
                    participante.nome = novos_dados_participante['nome']
                    participante.data_nascimento = [
                        novos_dados_participante['ano'],
                        novos_dados_participante['mes'],
                        novos_dados_participante['dia']
                    ]
                    participante.endereco = [
                        novos_dados_participante['logradouro'],
                        novos_dados_participante['num_endereco'],
                        novos_dados_participante['cep']
                    ]
                    self.__tela_participante.mostrar_mensagem('Dados do participante alterados com sucesso')
                else:
                    self.__tela_participante.mostrar_mensagem('ATENÇÃO: Participante não cadastrado')

            except TypeError:
                self.__tela_participante.mostrar_mensagem('Algum dado foi inserido incorretamente')

    def salva_comprovante_saude(self):
        self.lista_participantes()
        if len(self.__participantes) > 0:
            cpf_participante = self.__tela_participante.selecionar_participante()
            participante = self.pega_participante_por_cpf(cpf_participante)
            try:
                if participante is not None:
                    novos_dados_comprovante = self.__tela_participante.pegar_dados_comprovante()

                    participante.comprovante_saude = [
                        novos_dados_comprovante['primeira_dose'],
                        novos_dados_comprovante['segunda_dose'],
                        [
                            novos_dados_comprovante['ano'],
                            novos_dados_comprovante['mes'],
                            novos_dados_comprovante['dia'],
                            novos_dados_comprovante['hora'],
                            novos_dados_comprovante['minuto']
                        ],
                        novos_dados_comprovante['resultado_pcr']
                    ]
                    self.__tela_participante.mostrar_mensagem('Comprovante de saúde do participante salvo com sucesso')
                else:
                    self.__tela_participante.mostrar_mensagem('ATENÇÃO: Participante não cadastrado')

            except TypeError:
                self.__tela_participante.mostrar_mensagem('Algum dado foi inserido incorretamente')

    def mostra_participante(self):
        if len(self.__participantes) > 0:
            cpf_participante = self.__tela_participante.selecionar_participante()
            participante = self.pega_participante_por_cpf(cpf_participante)

            if participante is not None:
                self.__tela_participante.mostrar_participante({
                    'cpf': participante.cpf,
                    'nome': participante.nome,
                    'data_nascimento': participante.data_nascimento,
                    'endereco': participante.endereco,
                    'status': participante.status_participante,
                    'comprovante_saude': participante.comprovante_saude
                })
            else:
                self.__tela_participante.mostrar_mensagem('ATENÇÃO: Participante não cadastrado')
        else:
            self.__tela_participante.mostrar_mensagem('Não há participantes cadastrados para listar')

    def pega_participante_por_cpf(self, cpf_participante):
        for participante in self.__participantes:
            if participante.cpf == cpf_participante:
                return participante
        return None

    def lista_participantes(self):
        if len(self.__participantes) > 0:
            for participante in self.__participantes:
                self.__tela_participante.mostrar_participante({
                    'cpf': participante.cpf,
                    'nome': participante.nome,
                    'data_nascimento': participante.data_nascimento,
                    'endereco': participante.endereco,
                    'status': participante.status_participante,
                    'comprovante_saude': participante.comprovante_saude
                })
        else:
            self.__tela_participante.mostrar_mensagem('Não há participantes cadastrados para listar')

    def retornar(self):
        self.__controlador_eventos.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_participante, 2: self.exclui_participante, 3: self.altera_participante,
                        4: self.mostra_participante, 5: self.lista_participantes, 6: self.salva_comprovante_saude,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_participante.tela_opcoes()]()
