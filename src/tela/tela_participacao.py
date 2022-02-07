class TelaParticipacao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('\n-------- Participações ----------')
        print('1 - Adicionar Participação')
        print('2 - Adicionar Horario de Saída')
        print('3 - Excluir Participação')
        print('4 - Alterar Participação')
        print('5 - Mostrar Participação')
        print('6 - Listar Participações')
        print('0 - Retornar')

        try:
            opcao = int(input('Escolha uma opção: '))
            while opcao not in [0, 1, 2, 3, 4, 5, 6]:
                opcao = int(input('Escolha uma opção: '))
            return opcao
        except ValueError:
            self.mostrar_mensagem('Valores numéricos devem ser inteiros')

    def pegar_dados_participacao(self):
        print('\n-------- CADASTRAR PARTICIPAÇÃO ----------')
        try:
            id = input('ID da Participação: ')
            id_evento = input('ID do Evento: ')
            dia = int(input('Dia do Evento: '))
            mes = int(input('Mês do Evento: '))
            ano = int(input('Ano do Evento: '))
            hora = int(input('Hora de Entrada: '))
            minuto = int(input('Minuto de Entrada: '))
            cpf_participante = str(input('CPF do Participante: '))

            return {'id': id, 'id_evento': id_evento, 'dia_evento': dia, 'mes_evento': mes,
                    'ano_evento': ano, 'hora_entrada': hora, 'minuto_entrada': minuto,
                    'cpf_participante': cpf_participante}
        except ValueError:
            self.mostrar_mensagem('Valores de data devem ser inteiros')

    def pegar_horario_saida_participacao(self):
        print('\n-------- CADASTRAR HORÁRIO SAÍDA PARTICIPAÇÃO ----------')
        try:
            dia = int(input('Dia do Evento: '))
            mes = int(input('Mês do Evento: '))
            ano = int(input('Ano do Evento: '))
            hora = int(input('Hora de Saída: '))
            minuto = int(input('Minuto de Saída: '))

            return {'dia_evento': dia, 'mes_evento': mes, 'ano_evento': ano, 'hora_saida': hora,
                    'minuto_saida': minuto}
        except ValueError:
            self.mostrar_mensagem('Valores de data devem ser inteiros')

    def mostrar_participacao(self, dados_participacao):
        print('\nID DA PARTICIPAÇÃO: ', dados_participacao['id'])
        print('ID DO EVENTO: ', dados_participacao['id_evento'])
        print('CPF DO PARTICIPANTE: ', dados_participacao['id_evento'])
        print('HORARIO DE ENTRADA DO PARTICIPANTE: {0}'.format(dados_participacao['data_horario_entrada']))
        print('HORARIO DE SAÍDA DO PARTICIPANTE: {0}'.format(dados_participacao['data_horario_saida']))

    def selecionar_participacao(self):
        id_evento = input('ID do Evento: ')
        cpf_participante = input('CPF do participante: ')
        return {'id_evento': id_evento, 'cpf_participante': cpf_participante}

    def adicionar_horario_saida(self):
        id = input('ID da Participação: ')
        dia = int(input('Dia do Evento: '))
        mes = int(input('Mês do Evento: '))
        ano = int(input('Ano do Evento: '))
        hora = int(input('Hora de Saída: '))
        minuto = int(input('Minuto de Saída: '))
        return {'id': id, 'dia_evento': dia, 'mes_evento': mes, 'ano_evento': ano, 'hora_saida': hora,
                'minuto_saida': minuto}

    def mostrar_mensagem(self, msg):
        print(msg)