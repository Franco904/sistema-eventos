import PySimpleGUI as sg

from src.tela.strings.strings import *


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
            [sg.Radio('Opções de Listagem', 'RB', key='9')],
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
            print('Não há organizadores cadastrados para listar.')
            print('Acesse a tela de organizadores para cadastrar um organizador.')
            return

        if not editando:
            columnIdEvento = [
                [sg.Text('Cadastrar evento', size=(16, 1), font=('Arial', 14))],
                [
                    sg.Text('Id do evento:', size=(12, 1)), sg.InputText(size=(18, 1), key='id_evento'),
                    sg.Text('   Ano de realização do evento:', size=(24, 1)),
                    sg.InputText(size=(18, 1), key='ano'),
                ]
            ]
        else:
            columnIdEvento = [
                [sg.Text('Alterar evento', size=(16, 1), font=('Arial', 14))],
                [
                    sg.Text('', size=(30, 1)),
                    sg.Text('  Ano de realização do evento:', size=(24, 1)),
                    sg.InputText(size=(24, 1), key='ano'),
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
            [sg.Text('Dados do evento', size=(16, 1), font=('Arial', 14))],
            [sg.Text('Id do evento: '), sg.Text(dados_evento['id_evento'])],
            [sg.Text('Título do evento: '), sg.Text(dados_evento['titulo'])],
            [sg.Text('Local do evento: '), sg.Text(dados_evento['local'].nome)],
            [sg.Text('Data e horário do evento: '), sg.Text(dados_evento['data_horario_evento']
                                                            .strftime('%d/%m/%Y, %H:%M'))],
            [sg.Text('Capacidade do evento: '), sg.Text(dados_evento['capacidade'])],
            [sg.Text('Organizadores: '), sg.Text(montar_organizador_string(dados_evento['organizadores']))],
            [sg.Text('Participantes: '), sg.Text(montar_participante_string(dados_evento['participantes']))],
            [sg.Text('Participações confirmadas: '),
             sg.Text(montar_participacao_string(dados_evento['participacoes']))
             ],

            [sg.Cancel('OK')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def mostrar_eventos_rankeados(self, eventos):
        self.inicializar_mostrar_eventos_rankeados(eventos)
        button, values = self.__window.read()

        if button in [None, 'OK']:
            self.__window.close()

    def inicializar_mostrar_eventos_rankeados(self, eventos):
        sg.ChangeLookAndFeel('DarkTeal4')

        if len(eventos) == 0:
            layout = [
                [sg.Text('Os eventos da lista não possuem participações cadastradas.')],
                [sg.Cancel('OK')]
            ]
        else:
            layout = [
                [sg.Text('Eventos rankeados por público', size=(24, 1), font=('Arial', 14))],
                [sg.Frame('', [[sg.Text('Título do evento : Público')]])],
                [sg.Frame('', [
                    [sg.Text(f'{titulo} : {participacoes}')] for titulo, participacoes in eventos.items()
                ]
                          )],

                [sg.Cancel('OK')]
            ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def selecionar_evento(self):
        self.inicializar_selecionar_evento()
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            id_evento = int(values['id_evento'])
            return id_evento

        self.__window.close()
        return None

    def inicializar_selecionar_evento(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Selecionar evento', size=(16, 1), font=('Arial', 14))],
            [sg.Text('Id do evento que deseja selecionar: '), sg.InputText(size=(16, 1), key='id_evento')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def mostrar_mensagem(self, msg: str):
        sg.Popup(msg)
