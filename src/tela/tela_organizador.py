import PySimpleGUI as sg


class TelaOrganizador:
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
            [sg.Text('Organizadores', font=('Arial', 16), justification='center')],
            [sg.Text('Escolha uma opção abaixo:')],

            [sg.Radio('Adicionar organizador', 'RB', key='1')],
            [sg.Radio('Excluir organizador', 'RB', key='2')],
            [sg.Radio('Alterar organizador', 'RB', key='3')],
            [sg.Radio('Mostrar organizador', 'RB', key='4')],
            [sg.Radio('Listar organizadores', 'RB', key='5')],
            [sg.Radio('Retornar', 'RB', key='0')],

            [sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def pegar_dados_organizador(self, editando: bool):
        self.inicializar_pegar_dados(editando)
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            if editando:
                values['cpf'] = -1

            cpf = values['cpf']
            nome = values['nome']
            dia_nascimento = int(values['dia_nascimento'])
            mes_nascimento = int(values['mes_nascimento'])
            ano_nascimento = int(values['ano_nascimento'])

            return {'cpf': cpf, 'nome': nome, 'dia_nascimento': dia_nascimento, 'mes_nascimento': mes_nascimento,
                    'ano_nascimento': ano_nascimento}

        self.__window.close()
        return None

    def inicializar_pegar_dados(self, editando: bool):
        sg.ChangeLookAndFeel('DarkTeal4')

        if not editando:
            column = [
                [sg.Text('Cadastrar Organizador', font=('Arial', 14))],
                [sg.Text('CPF:'), sg.InputText(size=(11, 1), key='cpf')]
            ]
        else:
            column = [[sg.Text('Alterar Organizador', font=('Arial', 14))]]

        layout = [
            [sg.Column(column, pad=0)],
            [sg.Text('Nome:'), sg.InputText(size=(24, 1), key='nome')],
            [sg.Text('Dia de nascimento:'), sg.InputText(size=(2, 1), key='dia_nascimento')],
            [sg.Text('Mês de nascimento:'), sg.InputText(size=(2, 1), key='mes_nascimento')],
            [sg.Text('Ano de nascimento:'), sg.InputText(size=(4, 4), key='ano_nascimento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Eventos', layout)

    def mostrar_organizador(self, dados_organizador):
        self.inicializar_mostrar_organizador(dados_organizador)
        button, values = self.__window.read()

        if button in [None, 'OK']:
            self.__window.close()

    def inicializar_mostrar_organizador(self, dados_organizador):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Dados do Organizador', font=('Arial', 14))],
            [sg.Text('CPF:'), sg.Text(dados_organizador['cpf'])],
            [sg.Text('Nome:'), sg.Text(dados_organizador['nome'])],
            [sg.Text('Data de nascimento:'), sg.Text(dados_organizador['data_nascimento'])],

            [sg.Cancel('OK')]
        ]
        self.__window = sg.Window('Sistema de Eventos', layout)

    def selecionar_organizador(self):
        self.inicializar_selecionar_organizador()
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            cpf_organizador = values['cpf']
            return cpf_organizador

        self.__window.close()
        return None

    def inicializar_selecionar_organizador(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Selecionar Organizador', font=('Arial', 14))],
            [sg.Text('CPF do organizador que deseja selecionar: '), sg.InputText(size=(11, 1), key='cpf')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Eventos', layout)

    def fechar_tela(self):
        self.__window.close()

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)
