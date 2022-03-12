import PySimpleGUI as sg


class TelaParticipacao:
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

            self.fechar_tela()

        self.fechar_tela()
        return opcao

    def inicializar_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Participações', font=('Arial', 16), justification='center')],
            [sg.Text('Escolha uma opção abaixo:')],

            [sg.Radio('Adicionar participação', 'RB', key='1')],
            [sg.Radio('Adicionar horário de saída da participação', 'RB', key='2')],
            [sg.Radio('Excluir participação', 'RB', key='3')],
            [sg.Radio('Alterar horário de entrada da participação', 'RB', key='4')],
            [sg.Radio('Mostrar participação', 'RB', key='5')],
            [sg.Radio('Listar participações', 'RB', key='6')],
            [sg.Radio('Retornar', 'RB', key='0')],

            [sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def pegar_dados_participacao(self, eventos: list, participantes: list):
        self.inicializar_pegar_dados(eventos, participantes)
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            id_participacao = int(values['id'])
            hora = int(values['hora'])
            minuto = int(values['minuto'])
            evento = list(filter(lambda e: e.titulo == values['evento'], eventos))[0]
            participante = list(filter(lambda p: p.nome == values['participante'], participantes))[0]

            return {'id': id_participacao, 'evento': evento, 'hora_entrada': hora, 'minuto_entrada': minuto,
                    'participante': participante}

        self.__window.close()
        return None

    def inicializar_pegar_dados(self, eventos: list, participantes: list):
        sg.ChangeLookAndFeel('DarkTeal4')

        if len(eventos) > 0:
            eventosNomes = list(map(lambda e: e.titulo, eventos))
        else:
            self.mostrar_mensagem('Não há eventos cadastrados para listar.\n\n'
                                  'Acesse a tela de eventos para cadastrar um evento.\n')
            return

        if len(participantes) > 0:
            participantesNomes = list(map(lambda p: p.nome, participantes))
        else:
            self.mostrar_mensagem('Não há participantes cadastrados para listar.\n\n'
                                  'Acesse a tela de participantes para cadastrar um participante.\n')
            return

        layout = [
            [sg.Text('Cadastrar Participação', font=('Arial', 14))],
            [sg.Text('Id:'), sg.InputText(size=(4, 1), key='id')],
            [sg.Text('Participante:', size=(12, 1)),
             sg.Combo(participantesNomes, readonly=True, size=(16, 1), key='participante')],
            [sg.Text('Evento:', size=(12, 1)),
             sg.Combo(eventosNomes, readonly=True, size=(16, 1), key='evento')],
            [sg.Text('Hora de entrada:'), sg.InputText(size=(2, 1), key='hora')],
            [sg.Text('Minuto de entrada:'), sg.InputText(size=(2, 1), key='minuto')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def alterar_horario_entrada(self):
        self.inicializar_pegar_horario_entrada()
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            hora = int(values['hora'])
            minuto = int(values['minuto'])

            return {'hora_entrada': hora, 'minuto_entrada': minuto}

        self.__window.close()
        return None

    def inicializar_pegar_horario_entrada(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        column = [[sg.Text('Alterar Horário de Entrada', font=('Arial', 14))]]

        layout = [
            [sg.Column(column, pad=0)],
            [sg.Text('Hora:'), sg.InputText(size=(2, 1), key='hora')],
            [sg.Text('Minuto:'), sg.InputText(size=(2, 1), key='minuto')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Eventos', layout)

    def pegar_horario_saida(self):
        self.inicializar_pegar_horario_saida()
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            dia = int(values['dia'])
            hora = int(values['hora'])
            minuto = int(values['minuto'])

            return {'dia_saida': dia, 'hora_saida': hora, 'minuto_saida': minuto}

        self.__window.close()
        return None

    def inicializar_pegar_horario_saida(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        column = [[sg.Text('Adicionar Horário de Saída', font=('Arial', 14))]]

        layout = [
            [sg.Column(column, pad=0)],
            [sg.Text('Dia:'), sg.InputText(size=(2, 1), key='dia')],
            [sg.Text('Hora:'), sg.InputText(size=(2, 1), key='hora')],
            [sg.Text('Minuto:'), sg.InputText(size=(2, 1), key='minuto')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Eventos', layout)

    def mostrar_participacao(self, dados_participacao):
        self.inicializar_mostrar_participacao(dados_participacao)
        button, values = self.__window.read()

        if button in [None, 'OK']:
            self.__window.close()

    def inicializar_mostrar_participacao(self, dados_participacao):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Dados da Participação', font=('Arial', 14))],
            [sg.Text('Id:'), sg.Text(dados_participacao['id'])],
            [sg.Text('Id do evento:'), sg.Text(dados_participacao['id_evento'])],
            [sg.Text('Horário de entrada:'), sg.Text(dados_participacao['data_horario_entrada'].strftime('%H:%M'))],
        ]

        if dados_participacao['data_horario_saida'] is None:
            layout.append([sg.Text('Horário de saída:'), sg.Text('Não cadastrado')])
        else:
            layout.append([sg.Text('Horário de saída:'),
                           sg.Text(dados_participacao['data_horario_saida'].strftime('%H:%M'))])
        layout.append([sg.Text('Nome do participante:'),
                       sg.Text(dados_participacao['participante'].nome)])

        layout.append([sg.Cancel('OK')])

        self.__window = sg.Window('Sistema de Eventos', layout)

    def selecionar_participacao(self):
        self.inicializar_selecionar_participacao()
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()
            id_participacao = int(values['id'])
            return id_participacao

        self.__window.close()
        return None

    def inicializar_selecionar_participacao(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Selecionar Participação', font=('Arial', 14))],
            [sg.Text('Id da participação que deseja selecionar: '), sg.InputText(size=(4, 1), key='id')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Eventos', layout)

    def fechar_tela(self):
        self.__window.close()

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)
