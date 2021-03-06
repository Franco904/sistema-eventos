import PySimpleGUI as sg


class TelaEvento:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        opcao = -1
        while opcao == -1:
            self.inicializar_opcoes()
            button, values = self.__window.read()

            if values['0'] or button is None:
                opcao = 0
                break

            for i, key in enumerate(values, 1):
                if values[key]:
                    opcao = i

            self.__window.close()

        self.__window.close()
        return opcao

    def inicializar_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Eventos', size=(16, 1), font=('Arial', 16), justification='center')],
            [sg.Text('Escolha uma opção abaixo:')],

            [sg.Radio('Adicionar evento', 'RB', key='1')],
            [sg.Radio('Excluir evento', 'RB', key='2')],
            [sg.Radio('Alterar evento', 'RB', key='3')],
            [sg.Radio('Mostrar evento', 'RB', key='4')],
            [sg.Radio('Adicionar organizador ao evento', 'RB', key='5')],
            [sg.Radio('Excluir organizador do evento', 'RB', key='6')],
            [sg.Radio('Adicionar participante ao evento', 'RB', key='7')],
            [sg.Radio('Excluir participante do evento', 'RB', key='8')],
            [sg.Radio('Opções de listagem', 'RB', key='9')],
            [sg.Radio('Retornar', 'RB', key='0')],

            [sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def opcoes_listagem(self):
        opcao = -1
        while opcao == -1:
            self.inicializar_opcoes_listagem()
            button, values = self.__window.read()

            if values['0'] or button is None:
                opcao = 0
                break

            for i, key in enumerate(values, 1):
                if values[key]:
                    opcao = i

            self.__window.close()

        self.__window.close()
        return opcao

    def inicializar_opcoes_listagem(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Eventos', size=(16, 1), font=('Arial', 16), justification='center')],
            [sg.Text('Escolha uma opção abaixo:')],

            [sg.Radio('Listar eventos', 'RB', key='1')],
            [sg.Radio('Listar eventos ocorridos', 'RB', key='2')],
            [sg.Radio('Listar eventos futuros', 'RB', key='3')],
            [sg.Radio('Ranking de eventos por público', 'RB', key='4')],
            [sg.Radio('Listar organizadores do evento', 'RB', key='5')],
            [sg.Radio('Listar participantes do evento', 'RB', key='6')],
            [sg.Radio('Listar participantes com comprovante', 'RB', key='7')],
            [sg.Radio('Listar participantes sem comprovante', 'RB', key='8')],
            [sg.Radio('Listar participações do evento', 'RB', key='9')],
            [sg.Radio('Retornar', 'RB', key='0')],

            [sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def pegar_dados_evento(self, locais: list, organizadores: list, editando: bool):
        self.inicializar_pegar_dados(locais, organizadores, editando)
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            if editando:
                values['id_evento'] = -1

            local = list(filter(lambda l: l.nome == values['local'], locais))[0]
            organizadoresIncluidos = []
            for organizador in organizadores:
                for o in values['organizadores']:
                    if organizador.nome == o:
                        organizadoresIncluidos.append(organizador)

            return {'id_evento': int(values['id_evento']),
                    'titulo': values['titulo'],
                    'local': local,
                    'ano': int(values['ano']),
                    'mes': int(values['mes']),
                    'dia': int(values['dia']),
                    'hora': int(values['hora']),
                    'minuto': int(values['minuto']),
                    'capacidade': int(values['capacidade']),
                    'organizadores': organizadoresIncluidos}

        self.__window.close()
        return None

    def inicializar_pegar_dados(self, locais: list, organizadores: list, editando: bool):
        if len(locais) > 0:
            locaisTitulos = list(map(lambda l: l.nome, locais))
        else:
            self.mostrar_mensagem('Não há locais cadastrados para listar.\n\n'
                                  'Acesse a tela de locais para cadastrar um local.\n')
            return

        if len(organizadores) > 0:
            organizadoresNomes = list(map(lambda o: o.nome, organizadores))
        else:
            self.mostrar_mensagem('Não há organizadores cadastrados para listar.\n\n'
                                  'Acesse a tela de organizadores para cadastrar um organizador.')
            return

        if not editando:
            columnIdEvento = [
                [sg.Text('Cadastrar Evento', size=(16, 1), font=('Arial', 14))],
                [
                    sg.Text('Id do evento:', size=(12, 1)), sg.InputText(size=(18, 1), key='id_evento'),
                    sg.Text('   Ano de realização do evento:', size=(24, 1)),
                    sg.InputText(size=(18, 1), key='ano'),
                ]
            ]
        else:
            columnIdEvento = [
                [sg.Text('Alterar Evento', size=(16, 1), font=('Arial', 14))],
                [
                    sg.Text('', size=(30, 1)),
                    sg.Text('  Ano de realização do evento:', size=(24, 1)),
                    sg.InputText(size=(32, 1), key='ano'),
                ]
            ]

        layout = [
            [sg.Column(columnIdEvento, pad=0)],
            [
                sg.Text('Título:', size=(12, 1)), sg.InputText(size=(18, 1), key='titulo'),
                sg.Text('   Mês de realização do evento:', size=(24, 1)), sg.InputText(size=(24, 1), key='mes')
            ],
            [
                sg.Text('Local:', size=(12, 1)), sg.Combo(locaisTitulos, readonly=True, size=(16, 1), key='local'),
                sg.Text('   Dia de realização do evento:', size=(24, 1)), sg.InputText(size=(24, 1), key='dia')
            ],
            [
                sg.Text('Capacidade:', size=(12, 1)), sg.InputText(size=(18, 1), key='capacidade'),
                sg.Text('   Hora de realização do evento:', size=(24, 1)), sg.InputText(size=(24, 1), key='hora')
            ],
            [
                sg.Text('Organizador(es):', size=(12, 1)), sg.Listbox(organizadoresNomes, select_mode='multiple',
                                                                      size=(16, 3), key='organizadores'),
                sg.Text('   Minuto de realização do evento:', size=(24, 1)), sg.InputText(size=(24, 1), key='minuto')
            ],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def mostrar_detalhes_evento(self, dados_evento: dict):
        self.inicializar_detalhes_evento(dados_evento)
        button, values = self.__window.read()

        if button in [None, 'OK']:
            self.__window.close()

    def inicializar_detalhes_evento(self, dados_evento: dict):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Dados do Evento', size=(16, 1), font=('Arial', 14))],
            [sg.Text('Id do evento: '), sg.Text(dados_evento['id_evento'])],
            [sg.Text('Título do evento: '), sg.Text(dados_evento['titulo'])],
            [sg.Text('Local do evento: '), sg.Text(dados_evento['local'].nome)],
            [sg.Text('Data e horário do evento: '), sg.Text(dados_evento['data_horario_evento']
                                                            .strftime('%d/%m/%Y, %H:%M'))],
            [sg.Text('Capacidade do evento: '), sg.Text(dados_evento['capacidade'])],
            [sg.Text('Organizadores: '), sg.Text(dados_evento['organizadores'])],
            [sg.Text('Participantes: '), sg.Text(dados_evento['participantes'])],
            [sg.Text('Participações confirmadas: '),
             sg.Text(dados_evento['participacoes'])
             ],

            [sg.Cancel('OK')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def mostrar_eventos_rankeados(self, eventos: dict):
        self.inicializar_mostrar_eventos_rankeados(eventos)
        button, values = self.__window.read()

        if button in [None, 'OK']:
            self.__window.close()

    def inicializar_mostrar_eventos_rankeados(self, eventos: dict):
        sg.ChangeLookAndFeel('DarkTeal4')

        if len(eventos) == 0:
            layout = [
                [sg.Text('Os eventos da lista não possuem participações cadastradas.')],
                [sg.Cancel('OK')]
            ]
        else:
            layout = [
                [sg.Text('Eventos Rankeados por Público', size=(26, 1), font=('Arial', 14))],
                [sg.Frame('', [[sg.Text('Título do evento : Público')]])],
                [sg.Frame('', [
                    [sg.Text(f'{titulo} : {participacoes}')] for titulo, participacoes in eventos.items()
                ]
                          )],

                [sg.Cancel('OK')]
            ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def selecionar_evento(self, dados_eventos: dict):
        self.inicializar_selecionar_evento(dados_eventos)
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            if values['id'] == '':
                self.mostrar_mensagem('Nenhuma opção selecionada para mostrar.')
                return None

            id_evento = int(values['id'].split()[-1])
            return id_evento

        self.__window.close()
        return None

    def inicializar_selecionar_evento(self, dados_eventos: dict):
        sg.ChangeLookAndFeel('DarkTeal4')

        eventos_labels = []

        for contador in range(len(dados_eventos["ids"])):
            eventos_labels.append(f'{dados_eventos["titulos"][contador]} - ID: {dados_eventos["ids"][contador]}')
        eventos_labels.sort()

        layout = [
            [sg.Text('Selecionar Evento', size=(16, 1), font=('Arial', 14))],
            [sg.Text('Evento:', size=(12, 1)),
             sg.Combo(eventos_labels, readonly=True, size=(40, 1), key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    @staticmethod
    def mostrar_mensagem(msg: str):
        sg.Popup(msg)
