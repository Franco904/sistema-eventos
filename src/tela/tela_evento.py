class TelaEvento:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('\n-------- EVENTOS ----------')
        print("1 - Tela Local")
        print("2 - Tela Participação")
        print('3 - Adicionar evento')
        print('4 - Excluir evento')
        print('5 - Alterar evento')
        print('6 - Mostrar evento')
        print('7 - Listar eventos')
        print('8 - Listar eventos ocorridos')
        print('9 - Listar eventos futuros')
        print('10 - Ranking de eventos por público')
        print('0 - Retornar')

        try:
            opcao = int(input('Escolha uma opção: '))
            return opcao
        except ValueError:
            self.mostrar_mensagem('Valores numéricos devem ser inteiros')

    def pegar_dados_evento(self, locais: list, organizadores: list):
        print('\n-------- CADASTRAR EVENTO ----------')
        try:
            id = int(input('Id: '))
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
            capacidade = input('Capacidade do evento: ')
            opcoes_organizador = []
            if len(organizadores) > 0:
                print('Selecione um dos organizadores cadastrados:')

                for i, o in enumerate(organizadores):
                    print(f'[ {i + 1} ] CPF: {o.id}, Nome: {o.nome}')
                try:
                    continuar = False
                    while continuar:
                        opcao_organizador = int(input('Escolha uma opção: '))
                        while opcao_organizador > len(organizadores) or opcao_organizador < 1:
                            opcao_organizador = int(input('Escolha uma opção: '))
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

            return {'id': id, 'titulo': titulo, 'opcao_local': opcao_local, 'ano': ano, 'mes': mes, 'dia': dia,
                    'hora': hora, 'minuto': minuto, 'capacidade': capacidade, 'opcoes_organizador': opcoes_organizador}

        except ValueError:
            self.mostrar_mensagem('Valores de data/número devem ser inteiros')

    def mostrar_detalhes_evento(self, dados_evento):
        print('\nID DO EVENTO: ', dados_evento['id'])
        print('TÍTULO DO EVENTO: ', dados_evento['titulo'])
        print('LOCAL DO EVENTO: ', dados_evento['local'])
        print('DATA E HORÁRIO DO EVENTO: ', dados_evento['data_horario_evento'].strftime('%d/%m/%Y'))
        print('CAPACIDADE: ', dados_evento['capacidade'])

    def mostrar_organizadores(self, organizadores):
        print('ORGANIZADORES:')
        for o in organizadores:
            print(o['nome']) if o == organizadores[-1] else print(o['nome'], ', ')

    def mostrar_participantes(self, participantes):
        print('PARTICIPANTES: ', end='')
        if len(participantes) == 0:
            print('Não há participantes cadastrados')
        else:
            for p in participantes:
                print(p['nome']) if p == participantes[-1] else print(p['nome'], ', ')

    def mostrar_participacoes(self, participacoes):
        print('PARTICIPAÇÕES CONFIRMADAS: ', end='')
        if len(participacoes) == 0:
            print('Não há participações cadastradas')
        # else:
        #     for p in participacoes:
        #         print(p['participante']['nome']) if p == participacoes[-1] \
        #             else print(p['participante']['nome'], ', ')

        # Tirar os comentários após criar controlador de participações

    def mostrar_eventos_rankeados(self, eventos):
        print('EVENTOS RANKEADOS POR PÚBLICO: ', end='')
        if len(eventos) == 0:
            print('Não há eventos cadastrados')
        else:
            print('\nTítulo do evento : Público')
            for titulo, participacoes in eventos.items():
                print(titulo, ' : ', participacoes)

    def selecionar_evento(self):
        id_evento = input('\nId do evento que deseja selecionar: ')
        return id_evento

    def mostrar_mensagem(self, msg):
        print(msg)
