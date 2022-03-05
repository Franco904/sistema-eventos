class TelaParticipacao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('\n-------- Participações ----------')
        print('1 - Adicionar participação')
        print('2 - Adicionar horario de saída da participação')
        print('3 - Excluir participação')
        print('4 - Alterar horário de entrada da participação')
        print('5 - Mostrar participação')
        print('6 - Listar participações')
        print('0 - Retornar')
        print("-" * 40)

        opcao = int(input('Escolha uma opção: '))
        while opcao not in [0, 1, 2, 3, 4, 5, 6]:
            opcao = int(input('Escolha uma opção: '))
        return opcao

    def pegar_dados_participacao(self, eventos, participantes):
        print('\n-------- CADASTRAR PARTICIPAÇÃO ----------')
        id = int(input('Id da participação: '))

        if len(eventos) > 0:
            print('Selecione um dos eventos cadastrados:')

            for i, e in enumerate(eventos):
                print(f'[ {i + 1} ] Id: {e.id_evento}, Nome: {e.titulo}')

            opcao_evento = int(input('Escolha uma opção: '))
            while opcao_evento > len(eventos) or opcao_evento < 1:
                opcao_evento = int(input('Escolha uma opção: '))
        else:
            print('Não há eventos cadastrados para listar.')
            print('Acesse a tela de eventos para cadastrar um evento.')
            return

        hora = int(input('Hora de entrada no evento: '))
        minuto = int(input('Minuto de entrada no evento: '))

        if len(participantes) > 0:
            print('Selecione um dos participantes cadastrados:')

            for i, p in enumerate(participantes):
                print(f'[ {i + 1} ] CPF: {p.cpf}, Nome: {p.nome}')

            opcao_participante = int(input('Escolha uma opção: '))
            while opcao_participante > len(participantes) or opcao_participante < 1:
                opcao_participante = int(input('Escolha uma opção: '))
        else:
            print('Não há participantes cadastrados para listar.')
            print('Acesse a tela de participantes para cadastrar um participante.')
            return

        return {'id': id, 'opcao_evento': opcao_evento, 'hora_entrada': hora, 'minuto_entrada': minuto,
                'opcao_participante': opcao_participante}

    def alterar_horario_entrada(self):
        print('\n-------- ALTERAR HORÁRIO DE ENTRADA DA PARTICIPAÇÃO ----------')
        hora = int(input('Hora de saída: '))
        minuto = int(input('Minuto de saída: '))

        return {'hora_entrada': hora, 'minuto_entrada': minuto}

    def pegar_horario_saida(self):
        print('\n-------- REGISTRAR HORÁRIO DE SAÍDA DA PARTICIPAÇÃO ----------')
        hora = int(input('Hora de saída: '))
        minuto = int(input('Minuto de saída: '))

        return {'hora_saida': hora, 'minuto_saida': minuto}

    def mostrar_participacao(self, dados_participacao):
        print("-" * 40)
        print('ID DA PARTICIPAÇÃO: ', dados_participacao['id'])
        print('ID DO EVENTO: ', dados_participacao['id_evento'])
        print('HORÁRIO DE ENTRADA DO PARTICIPANTE: ', dados_participacao['data_horario_entrada'].strftime('%H:%M'))
        print('HORÁRIO DE SAÍDA DO PARTICIPANTE:  ', end='')
        if dados_participacao['data_horario_saida'] is None:
            print('Não cadastrado')
        else:
            print(dados_participacao['data_horario_saida'].strftime('%H:%M'))
        print('CPF DO PARTICIPANTE: ', dados_participacao['cpf_participante'])
        print("-" * 40)

    def selecionar_participacao(self):
        id = int(input('\nId da participação: '))
        return id

    def mostrar_mensagem(self, msg):
        print(msg)
