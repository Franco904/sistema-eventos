import PySimpleGUI as sg


class TelaLocal:
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
            [sg.Text('Locais', size=(16, 1), font=('Arial', 16), justification='center')],
            [sg.Text('Escolha uma opção abaixo:')],

            [sg.Radio('Adicionar local', 'RB', key='1')],
            [sg.Radio('Excluir local', 'RB', key='2')],
            [sg.Radio('Alterar local', 'RB', key='3')],
            [sg.Radio('Mostrar local', 'RB', key='4')],
            [sg.Radio('Listar locais', 'RB', key='5')],
            [sg.Radio('Retornar', 'RB', key='0')],

            [sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def pegar_dados_local(self, editando: bool):
        self.inicializar_pegar_dados(editando)
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            if editando:
                values['id'] = -1

            id = int(values['id'])
            nome = values['nome']

            return {'id': id, 'nome': nome}

        self.__window.close()
        return None

    def inicializar_pegar_dados(self, editando: bool):
        sg.ChangeLookAndFeel('DarkTeal4')

        if not editando:
            column = [
                [sg.Text('Cadastrar Local', size=(16, 1), font=('Arial', 14))],
                [sg.Text('Id:', size=(5, 1)), sg.InputText(size=(24, 1), key='id')]
            ]
        else:
            column = [[sg.Text('Alterar Local', size=(16, 1), font=('Arial', 14))]]

        layout = [
            [sg.Column(column, pad=0)],
            [sg.Text('Nome:', size=(5, 1)), sg.InputText(size=(24, 1), key='nome')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def mostrar_local(self, dados_local):
        self.inicializar_mostrar_local(dados_local)
        button, values = self.__window.read()

        if button in [None, 'OK']:
            self.__window.close()

    def inicializar_mostrar_local(self, dados_local):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Dados do Local', size=(16, 1), font=('Arial', 14))],
            [sg.Text('Id do local: '), sg.Text(dados_local['id'])],
            [sg.Text('Nome do local: '), sg.Text(dados_local['nome'])],

            [sg.Cancel('OK')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def selecionar_local(self, locais: list):
        self.inicializar_selecionar_local(locais)
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            id_local = int(values['id'].split()[-1])
            return id_local

        self.__window.close()
        return None

    def inicializar_selecionar_local(self, locais: list):
        sg.ChangeLookAndFeel('DarkTeal4')

        locaisIDs = list(map(lambda l: l.id, locais))
        locaisNomes = list(map(lambda l: l.nome, locais))
        locais_labels = []
        for contador in range(len(locais)):
            locais_labels.append(f"{locaisNomes[contador]} - ID: {locaisIDs[contador]}")
        locais_labels.sort()

        layout = [
            [sg.Text('Selecionar Local', size=(16, 1), font=('Arial', 14))],
            [sg.Text('Local:', size=(12, 1)),
             sg.Combo(locais_labels, readonly=True, size=(40, 1), key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def fechar_tela(self):
        self.__window.close()

    def mostrar_mensagem(self, msg: str):
        sg.Popup(msg)
