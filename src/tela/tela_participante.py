from datetime import datetime

import PySimpleGUI as sg

from src.entidade.enums.resultado_pcr import ResultadoPcr


class TelaParticipante:
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
            [sg.Text('Participantes', font=('Arial', 16), justification='center')],
            [sg.Text('Escolha uma opção abaixo:')],

            [sg.Radio('Adicionar Participante', 'RB', key='1')],
            [sg.Radio('Excluir Participante', 'RB', key='2')],
            [sg.Radio('Alterar Participante', 'RB', key='3')],
            [sg.Radio('Mostrar Participante', 'RB', key='4')],
            [sg.Radio('Listar Participantes', 'RB', key='5')],
            [sg.Radio('Salvar comprovante de saúde do participante', 'RB', key='6')],
            [sg.Radio('Retornar', 'RB', key='0')],

            [sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('Sistema de Eventos', layout)

    def pegar_dados_participante(self, editando: bool):
        self.inicializar_pegar_dados(editando)
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            if editando:
                values['cpf'] = -1

            cpf = values['cpf']
            nome = values['nome']
            dia = int(values['dia_nascimento'])
            mes = int(values['mes_nascimento'])
            ano = int(values['ano_nascimento'])
            logradouro = values['logradouro']
            num_endereco = int(values['num_endereco'])
            cep = values['cep']

            return {'cpf': cpf, 'nome': nome, 'dia': dia, 'mes': mes, 'ano': ano,
                    'logradouro': logradouro, 'num_endereco': num_endereco, 'cep': cep}

        self.__window.close()
        return None

    def inicializar_pegar_dados(self, editando: bool):
        sg.ChangeLookAndFeel('DarkTeal4')

        if not editando:
            column = [
                [sg.Text('Cadastrar Participante', font=('Arial', 14))],
                [sg.Text('CPF:'), sg.InputText(size=(11, 1), key='cpf')]
            ]
        else:
            column = [[sg.Text('Alterar Participante', font=('Arial', 14))]]

        layout = [
            [sg.Column(column, pad=0)],
            [sg.Text('Nome:'), sg.InputText(size=(24, 1), key='nome')],
            [sg.Text('Dia de nascimento:'), sg.InputText(size=(2, 1), key='dia_nascimento')],
            [sg.Text('Mês de nascimento:'), sg.InputText(size=(2, 1), key='mes_nascimento')],
            [sg.Text('Ano de nascimento:'), sg.InputText(size=(4, 4), key='ano_nascimento')],
            [sg.Text('Logradouro (endereço):'), sg.InputText(size=(24, 1), key='logradouro')],
            [sg.Text('Número (endereço):'), sg.InputText(size=(4, 1), key='num_endereco')],
            [sg.Text('CEP (endereço):'), sg.InputText(size=(8, 8), key='cep')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Eventos', layout)

    def pegar_dados_comprovante(self):
        ano = mes = dia = hora = minuto = 12
        self.inicializar_pegar_dados_comprovante()
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            primeira_dose = values['primeira_dose']
            segunda_dose = values['segunda_dose']
            teste_pcr = values['teste_pcr']

            resultado_pcr = ResultadoPcr.nao_realizado

            if teste_pcr:
                self.inicializar_pegar_dados_pcr()
                button, values = self.__window.read()

                if button == 'Confirmar':
                    self.__window.close()

                    ano = int(values['ano'])
                    mes = int(values['mes'])
                    dia = int(values['dia'])
                    hora = int(values['hora'])
                    minuto = int(values['minuto'])
                    pcr_positivo = values['pcr_positivo']
                    pcr_negativo = values['pcr_negativo']
                    if pcr_positivo:
                        resultado_pcr = ResultadoPcr.positivo
                    if pcr_negativo:
                        resultado_pcr = ResultadoPcr.negativo

            return {'primeira_dose': primeira_dose, 'segunda_dose': segunda_dose,
                    'ano': ano, 'mes': mes, 'dia': dia, 'hora': hora, 'minuto': minuto,
                    'resultado_pcr': resultado_pcr}

        self.__window.close()
        return None

    def inicializar_pegar_dados_comprovante(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        column = [
            [sg.Text('REGISTRAR COMPROVANTE DE SAÚDE DO PARTICIPANTE', font=('Arial', 14))],
        ]

        layout = [
            [sg.Column(column, pad=0)],
            [sg.Checkbox('Primeira Dose da Vacina', key='primeira_dose')],
            [sg.Checkbox('Segunda Dose da Vacina', key='segunda_dose')],
            [sg.Checkbox('Realizou Teste PCR', key='teste_pcr')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Eventos', layout)

    def inicializar_pegar_dados_pcr(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        column = [
            [sg.Text('REGISTRAR TESTE PCR DO PARTICIPANTE', font=('Arial', 14))],
        ]

        layout = [
            [sg.Column(column, pad=0)],
            [sg.Text('Ano:'), sg.InputText(size=(4, 4), key='ano')],
            [sg.Text('Mês:'), sg.InputText(size=(2, 1), key='mes')],
            [sg.Text('Dia:'), sg.InputText(size=(2, 1), key='dia')],
            [sg.Text('Hora:'), sg.InputText(size=(2, 1), key='hora')],
            [sg.Text('Minuto:'), sg.InputText(size=(2, 1), key='minuto')],
            [
                sg.Text('Resultado:'),
                sg.Radio('Positivo', 'resultados', key='pcr_positivo'),
                sg.Radio('Negativo', 'resultados', key='pcr_negativo'),
            ],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Eventos', layout)

    def mostrar_participante(self, dados_participante):
        self.inicializar_mostrar_participante(dados_participante)
        button, values = self.__window.read()

        if button in [None, 'OK']:
            self.__window.close()

    def inicializar_mostrar_participante(self, dados_participante):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [[sg.Text('Dados do Participante', font=('Arial', 14))],
                  [sg.Text('CPF:'), sg.Text(dados_participante['cpf'])],
                  [sg.Text('Nome:'), sg.Text(dados_participante['nome'])],
                  [sg.Text('Data de nascimento:'), sg.Text(dados_participante['data_nascimento'].strftime('%d/%m/%Y'))],
                  [sg.Text('Endereço do Participante', font=('Arial', 14))],
                  [sg.Text('Logradouro:'), sg.Text(dados_participante['endereco'].logradouro)],
                  [sg.Text('Número de endereço:'), sg.Text(dados_participante['endereco'].num_endereco)],
                  [sg.Text('CEP:'), sg.Text(dados_participante['endereco'].cep)],
                  [sg.Text('Status:'), sg.Text(dados_participante['status'].value)],
                  [sg.Text('Comprovante de Saúde do Participante', font=('Arial', 14))]]

        if dados_participante['comprovante_saude'] is None:
            layout.append([sg.Text('Não Cadastrado')])
        else:
            layout.append([sg.Text('Primeira Dose Vacinal:'),
                           sg.Text('Sim' if dados_participante['comprovante_saude'].primeira_dose else 'Não')])
            layout.append([sg.Text('Primeira Dose Vacinal:'),
                           sg.Text('Sim' if dados_participante['comprovante_saude'].segunda_dose else 'Não')])
            if dados_participante['comprovante_saude'].data_horario_teste == datetime(12, 12, 12, 12, 12):
                layout.append([sg.Text('Data e horário do teste PCR: Não realizado')])
            else:
                layout.append([sg.Text('Data e horário do teste PCR:'),
                               sg.Text(dados_participante['comprovante_saude'].data_horario_teste.strftime(
                                   '%d/%m/%Y, %H:%M'))])
                layout.append([sg.Text('Resultado do teste PCR:'),
                               sg.Text(dados_participante['comprovante_saude'].resultado_pcr.value)])

        layout.append([sg.Cancel('OK')])

        self.__window = sg.Window('Sistema de Eventos', layout)

    def selecionar_participante(self):
        self.inicializar_selecionar_participante()
        button, values = self.__window.read()

        if button == 'Confirmar':
            self.__window.close()

            cpf_participante = values['cpf']
            return cpf_participante

        self.__window.close()
        return None

    def inicializar_selecionar_participante(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Selecionar Participante', font=('Arial', 14))],
            [sg.Text('CPF do participante que deseja selecionar: '), sg.InputText(size=(11, 1), key='cpf')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Eventos', layout)

    def fechar_tela(self):
        self.__window.close()

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)
