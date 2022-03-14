import PySimpleGUI as sg


class TelaSistema:
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
            [sg.Text('Sistema de Eventos', size=(16, 1), font=('Arial', 16), justification='center')],
            [sg.Text('Escolha uma opção abaixo:')],

            [sg.Radio('Opções de eventos', 'RB', key='1')],
            [sg.Radio('Opções de locais', 'RB', key='2')],
            [sg.Radio('Opções de organizadores', 'RB', key='3')],
            [sg.Radio('Opções de participantes', 'RB', key='4')],
            [sg.Radio('Opções de participações', 'RB', key='5')],
            [sg.Radio('Finalizar sistema', 'RB', key='0')],

            [sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def mostrar_mensagem(self, msg: str):
        sg.Popup(msg)
