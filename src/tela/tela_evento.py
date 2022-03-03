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
        print('11 - Listar participações do evento')
        print('12 - Listar participantes com comprovante')
        print('13 - Listar participantes sem comprovante')

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
            self.mostrar_mensagem('Não há locais cadastrados para listar')
            self.mostrar_mensagem('Acesse a tela de locais para cadastrar um local')
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
                    self.mostrar_mensagem('O organizador já foi incluído na lista')
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
            self.mostrar_mensagem('Não há organizadores cadastrados para listar')
            self.mostrar_mensagem('Acesse a tela de organizadores para cadastrar um organizador')
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
        print('EVENTOS RANKEADOS POR PÚBLICO: ', end='')
        if len(eventos) == 0:
            print('Não há eventos cadastrados.')
        else:
            print('\nTítulo do evento : Público')
            for titulo, participacoes in eventos.items():
                print(titulo, ' : ', participacoes)
        print("-" * 40)

    def mostrar_organizadores(self, organizadores):
        print('ORGANIZADORES:')
        if len(organizadores) == 0:
            print('Nenhum organizador inserido')
        else:
            for o in organizadores:
                print(o.nome) if o.cpf == organizadores[-1].cpf else print(o.nome, ', ', end='')

    def mostrar_participantes(self, participantes):
        print('PARTICIPANTES: ', end='')
        if len(participantes) == 0:
            print('Nenhum participante inserido')
        else:
            for p in participantes:
                print(p.nome) if p.cpf == participantes[-1].cpf else print(p.nome, ', ', end='')

    def mostrar_participacoes(self, participacoes):
        print('PARTICIPAÇÕES CONFIRMADAS: ', end='')
        if len(participacoes) == 0:
            print('Nenhuma participação inserida')
        else:
            for p in participacoes:
                print(p.participante.nome) if p.id == participacoes[-1].id \
                    else print(p.participante.nome, ', ', end='')

    def listar_organizadores_evento(self, organizadores):
        for organizador in organizadores:
            print('-' * 40)
            print('CPF DO ORGANIZADOR: ', organizador.cpf)
            print('NOME DO ORGANIZADOR: ', organizador.nome)
            print('DATA DE NASCIMENTO DO ORGANIZADOR: ', organizador.data_nascimento.strftime('%d/%m/%Y'))
            print('-' * 40)

    def listar_participantes_evento(self, participantes):
        for participante in participantes:
            print('-' * 40)
            print('CPF DO PARTICIPANTE: ', participante.cpf)
            print('NOME DO PARTICIPANTE: ', participante.nome)
            print('DATA DE NASCIMENTO DO PARTICIPANTE: ', participante.data_nascimento.strftime('%d/%m/%Y'))
            print('ENDEREÇO DO PARTICIPANTE: ')
            print('Logradouro: ', participante.endereco.logradouro)
            print('Número de endereço: ', participante.endereco.num_endereco)
            print('CEP: ', participante.endereco.cep)
            print('STATUS DO PARTICIPANTE: ', participante.status_participante.name)
            print('COMPROVANTE DE SAÚDE DO PARTICIPANTE: ', end='')
            if participante.comprovante_saude is None:
                print('Não cadastrado')
            else:
                print('\nTomou primeira dose vacinal? ',
                      'Sim' if participante.comprovante_saude.primeira_dose else 'Não')
                print('Tomou segunda dose vacinal? ',
                      'Sim' if participante.comprovante_saude.segunda_dose else 'Não')
                print('Data e horário do teste PCR: ', 'Não realizado'
                if participante.comprovante_saude.data_horario_teste == datetime(12, 12, 12, 12, 12)
                else participante.comprovante_saude.data_horario_teste.strftime('%d/%m/%Y, %H:%M'))
                print('Teste PCR: ', participante.comprovante_saude.resultado_pcr.name)
        print('-' * 40)

    def listar_participacoes_evento(self, participacoes):
        for participacao in participacoes:
            print('-' * 40)
            print('ID DA PARTICIPAÇÃO: ', participacao.id)
            print('ID DO EVENTO: ', participacao.id_evento)
            print('CPF DO PARTICIPANTE: ', participacao.cpf_participante)
            print('HORARIO DE ENTRADA DO PARTICIPANTE: {0}'.format(participacao.data_horario_entrada))
            print('HORARIO DE SAÍDA DO PARTICIPANTE: {0}'.format(participacao.data_horario_saida))
            print('-' * 40)

    def selecionar_evento(self):
        id_evento = int(input('\nId do evento que deseja selecionar: '))
        return id_evento

    def mostrar_mensagem(self, msg):
        print(msg)
