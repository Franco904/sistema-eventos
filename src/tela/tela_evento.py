class TelaEvento:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('\n-------- OPÇÕES ----------')
        print("1 - Tela Local")
        print("2 - Tela Organizador")
        print("3 - Tela Participante")
        print("4 - Tela Participação")
        print('5 - Adicionar evento')
        print('6 - Excluir evento')
        print('7 - Alterar evento')
        print('8 - Mostrar evento')
        print('9 - Listar eventos')
        print('10 - Listar eventos ocorridos')
        print('11 - Listar eventos futuros')
        print('12 - Ranking de eventos por público')

        print('0 - Retornar')
        print("-" * 40)

        try:
            opcao = int(input('Escolha uma opção: '))
            return opcao
        except ValueError:
            self.mostrar_mensagem('Valores numéricos devem ser inteiros')

    def pegar_dados_evento(self, locais: list, organizadores: list):
        print('\n-------- CADASTRAR EVENTO ----------')
        try:
            id_evento = int(input('Id do evento: '))
            titulo = input('Título: ')
            opcao_local = None
            if len(locais) > 0:
                print('Selecione um dos locais cadastrados:')

                for i, l in enumerate(locais):
                    print(f'[ {i + 1} ] Id: {l.id}, Nome: {l.nome}')
                try:
                    opcao_local = int(input('Escolha uma opção: '))
                    while opcao_local > len(locais) or opcao_local < 1:
                        opcao_local = int(input('Escolha uma opção: '))
                except ValueError:
                    self.mostrar_mensagem('Valores numéricos devem ser inteiros')
            else:
                self.mostrar_mensagem('Não há locais cadastrados para listar')
                return

            ano = int(input('Ano de realização do evento: '))
            mes = int(input('Mês de realização do evento: '))
            dia = int(input('Dia de realização do evento: '))
            hora = int(input('Hora de realização do evento: '))
            minuto = int(input('Minuto de realização do evento: '))
            capacidade = int(input('Capacidade do evento: '))
            opcoes_organizador = []
            if len(organizadores) > 0:
                print('Selecione um dos organizadores cadastrados:')

                for i, o in enumerate(organizadores):
                    print(f'[ {i + 1} ] CPF: {o.cpf}, Nome: {o.nome}')
                try:
                    continuar = True
                    while continuar:
                        opcao_organizador = int(input('Escolha uma opção: '))
                        while opcao_organizador > len(organizadores) or opcao_organizador < 1:
                            opcao_organizador = int(input('Escolha uma opção: '))

                        if opcao_organizador in opcoes_organizador:
                            self.mostrar_mensagem('O organizador já foi incluído na lista')
                        else:
                            opcoes_organizador.append(opcao_organizador)

                            if len(organizadores) > 1:
                                cont = input('Deseja incluir mais organizadores? [S/N]: ').upper().strip()[0]
                                while cont not in 'SN':
                                    cont = input('Deseja incluir mais organizadores? [S/N]: ').upper().strip()[0]
                                continuar = True if cont == 'S' else False
                            else:
                                continuar = False

                except ValueError:
                    self.mostrar_mensagem('Valores numéricos devem ser inteiros')
            else:
                self.mostrar_mensagem('Não há organizadores cadastrados para listar')
                return

            return {'id_evento': id_evento, 'titulo': titulo, 'opcao_local': opcao_local, 'ano': ano,
                    'mes': mes, 'dia': dia, 'hora': hora, 'minuto': minuto, 'capacidade': capacidade,
                    'opcoes_organizador': opcoes_organizador}

        except ValueError:
            self.mostrar_mensagem('Valores de data/número devem ser inteiros')

    def mostrar_detalhes_evento(self, dados_evento):
        print("-" * 40)
        print('ID DO EVENTO: ', dados_evento['id_evento'])
        print('TÍTULO DO EVENTO: ', dados_evento['titulo'])
        print('LOCAL DO EVENTO: ', dados_evento['local'].nome)
        print('DATA E HORÁRIO DO EVENTO: ', dados_evento['data_horario_evento'].strftime('%d/%m/%Y'))
        print('CAPACIDADE: ', dados_evento['capacidade'])
        print("-" * 40)

    def mostrar_organizadores(self, organizadores):
        print('ORGANIZADORES:')
        for o in organizadores:
            print(o.nome) if o.cpf == organizadores[-1].cpf else print(o.nome, ', ', end='')

    def mostrar_participantes(self, participantes):
        print('PARTICIPANTES: ', end='')
        if len(participantes) == 0:
            print('Não há participantes cadastrados')
        else:
            for p in participantes:
                print(p.nome) if p.cpf == participantes[-1].cpf else print(p.nome, ', ', end='')

    def mostrar_participacoes(self, participacoes):
        print('PARTICIPAÇÕES CONFIRMADAS: ', end='')
        if len(participacoes) == 0:
            print('Não há participações cadastradas')
        # else:
        #     for p in participacoes:
        #         print(p.participante.nome) if p.id == participacoes[-1].id \
        #             else print(p.participante.nome, ', ', end='')

        # Tirar os comentários após criar controlador de participações

    def mostrar_eventos_rankeados(self, eventos):
        print("-" * 40)
        print('EVENTOS RANKEADOS POR PÚBLICO: ', end='')
        if len(eventos) == 0:
            print('Não há eventos cadastrados')
        else:
            print('\nTítulo do evento : Público')
            for titulo, participacoes in eventos.items():
                print(titulo, ' : ', participacoes)
        print("-" * 40)

    def selecionar_evento(self):
        try:
            id_evento = int(input('\nId do evento que deseja selecionar: '))
            return id_evento
        except ValueError:
            self.mostrar_mensagem('Valores de numéricos devem ser inteiros')

    def mostrar_mensagem(self, msg):
        print(msg)
