from datetime import datetime


class TelaEvento:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('\n-------- OPÇÕES ----------')
        print('1 - Adicionar evento')
        print('2 - Excluir evento')
        print('3 - Alterar evento')
        print('4 - Mostrar evento')
        print('5 - Listar eventos')
        print('6 - Listar eventos ocorridos')
        print('7 - Listar eventos futuros')
        print('8 - Ranking de eventos por público')

        print('9 - Listar organizadores do evento')
        print('10 - Listar participantes do evento')
        print('11 - Listar participantes com comprovante')
        print('12 - Listar participantes sem comprovante')
        print('13 - Listar participações do evento')

        print('14 - Adicionar organizador ao evento')
        print('15 - Excluir organizador do evento')
        print('16 - Adicionar participante ao evento')
        print('17 - Excluir participante do evento')
        print('18 - Adicionar participação ao evento')
        print('19 - Excluir participação do evento')
        print('0 - Retornar')
        print("-" * 40)

        opcao = int(input('Escolha uma opção: '))
        while opcao < 0 or opcao > 19:
            opcao = int(input('Escolha uma opção: '))
        return opcao

    def pegar_dados_evento(self, locais: list, organizadores: list):
        print('\n-------- CADASTRAR EVENTO ----------')
        id_evento = int(input('Id do evento: '))
        titulo = input('Título: ')
        if len(locais) > 0:
            print('Selecione um dos locais cadastrados:')

            for i, l in enumerate(locais):
                print(f'[ {i + 1} ] Id: {l.id}, Nome: {l.nome}')

            opcao_local = int(input('Escolha uma opção: '))
            while opcao_local > len(locais) or opcao_local < 1:
                opcao_local = int(input('Escolha uma opção: '))
        else:
            print('Não há locais cadastrados para listar.')
            print('Acesse a tela de locais para cadastrar um local.')
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

            continuar = True
            while continuar:
                opcao_organizador = int(input('Escolha uma opção: '))
                while opcao_organizador > len(organizadores) or opcao_organizador < 1:
                    opcao_organizador = int(input('Escolha uma opção: '))

                if opcao_organizador in opcoes_organizador:
                    print('O organizador já foi incluído na lista.')
                else:
                    opcoes_organizador.append(opcao_organizador)

                    if len(organizadores) > 1 and len(opcoes_organizador) < len(organizadores):
                        cont = input('Deseja incluir mais organizadores? [S/N]: ').upper().strip()[0]
                        while cont not in 'SN':
                            cont = input('Deseja incluir mais organizadores? [S/N]: ').upper().strip()[0]
                        continuar = True if cont == 'S' else False
                    else:
                        continuar = False
        else:
            print('Não há organizadores cadastrados para listar.')
            print('Acesse a tela de organizadores para cadastrar um organizador.')
            return

        return {'id_evento': id_evento, 'titulo': titulo, 'opcao_local': opcao_local, 'ano': ano,
                'mes': mes, 'dia': dia, 'hora': hora, 'minuto': minuto, 'capacidade': capacidade,
                'opcoes_organizador': opcoes_organizador}

    def mostrar_detalhes_evento(self, dados_evento):
        print("-" * 40)
        print('ID DO EVENTO: ', dados_evento['id_evento'])
        print('TÍTULO DO EVENTO: ', dados_evento['titulo'])
        print('LOCAL DO EVENTO: ', dados_evento['local'].nome)
        print('DATA E HORÁRIO DO EVENTO: ', dados_evento['data_horario_evento'].strftime('%d/%m/%Y, %H:%M'))
        print('CAPACIDADE: ', dados_evento['capacidade'])
        print("-" * 40)

    def mostrar_eventos_rankeados(self, eventos):
        print("-" * 40)
        if len(eventos) > 0:
            print('EVENTOS RANKEADOS POR PÚBLICO: ', end='')
            print('\nTítulo do evento : Público')
            for titulo, participacoes in eventos.items():
                print(titulo, ' : ', participacoes)
        else:
            print('Os eventos para listar não possuem participações cadastradas.')
        print("-" * 40)

    def mostrar_organizadores(self, organizadores):
        print('ORGANIZADORES:')
        if len(organizadores) == 0:
            print('Nenhum organizador inserido')
        else:
            for organizador in organizadores:
                print(organizador.nome) if organizador.cpf == organizadores[-1].cpf \
                    else print(organizador.nome, ', ', end='')

    def mostrar_participantes(self, participantes):
        print('PARTICIPANTES:')
        if len(participantes) == 0:
            print('Nenhum participante inserido')
        else:
            for participante in participantes:
                print(participante.nome) if participante.cpf == participantes[-1].cpf \
                    else print(participante.nome, ', ', end='')

    def mostrar_participacoes(self, participacoes, controlador_participantes):
        print('PARTICIPAÇÕES CONFIRMADAS:')
        if len(participacoes) == 0:
            print('Nenhuma participação inserida')
        else:
            for participacao in participacoes:
                participante = controlador_participantes.pegar_participante_por_cpf(participacao.cpf_participante)
                print(participante.nome) if participacao.id == participacoes[-1].id \
                    else print(participante.nome, ', ', end='')

    def selecionar_evento(self):
        id_evento = int(input('\nId do evento que deseja selecionar: '))
        return id_evento

    def mostrar_mensagem(self, msg):
        print(msg)
