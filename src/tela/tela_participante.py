from datetime import datetime

from src.entidade.enums.resultado_pcr import ResultadoPcr


class TelaParticipante:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('\n-------- PARTICIPANTES ----------')
        print('1 - Adicionar participante')
        print('2 - Excluir participante')
        print('3 - Alterar participante')
        print('4 - Mostrar participante')
        print('5 - Listar participantes')
        print('6 - Salvar comprovante de saúde do participante')
        print('0 - Retornar')
        print("-" * 40)

        opcao = int(input('Escolha uma opção: '))
        while opcao not in [0, 1, 2, 3, 4, 5, 6]:
            opcao = int(input('Escolha uma opção: '))
        return opcao

    def pegar_dados_participante(self, editando: bool):
        if not editando:
            print('\n-------- CADASTRAR PARTICIPANTE ----------')
            cpf = input('CPF: ')
        else:
            print('\n-------- ALTERAR PARTICIPANTE ----------')
            cpf = None

        nome = input('Nome: ')
        dia = int(input('Dia de nascimento: '))
        mes = int(input('Mês de nascimento: '))
        ano = int(input('Ano de nascimento: '))
        logradouro = input('Logradouro (endereço): ')
        num_endereco = int(input('Número (endereço): '))
        cep = input('CEP (endereço): ')

        return {'cpf': cpf, 'nome': nome, 'dia': dia, 'mes': mes, 'ano': ano,
                'logradouro': logradouro, 'num_endereco': num_endereco, 'cep': cep}

    def pegar_dados_comprovante(self):
        segunda_dose = False
        print('\n-------- REGISTRAR COMPROVANTE DE SAÚDE DO PARTICIPANTE ----------')
        tomou_primeira = input('Tomou primeira dose vacinal? [S/N]: ').upper().strip()[0]
        while tomou_primeira not in 'SN':
            tomou_primeira = input('Tomou primeira dose vacinal? [S/N]: ').upper().strip()[0]
        primeira_dose = True if tomou_primeira == 'S' else False

        if primeira_dose:
            tomou_segunda = input('Tomou segunda dose vacinal? [S/N]: ').upper().strip()[0]
            while tomou_segunda not in 'SN':
                tomou_segunda = input('Tomou segunda dose vacinal? [S/N]: ').upper().strip()[0]
            segunda_dose = True if tomou_segunda == 'S' else False

        if not segunda_dose:
            resultado_pcr = ResultadoPcr.nao_realizado
            pcr = input('Realizou teste PCR? [S/N]: ').upper().strip()[0]
            while pcr not in 'SN':
                pcr = input('Realizou teste PCR? [S/N]: ').upper().strip()[0]

            if pcr == 'S':
                ano = int(input('Ano de realização do teste: '))
                mes = int(input('Mês de realização do teste: '))
                dia = int(input('Dia de realização do teste: '))
                hora = int(input('Hora de realização do teste: '))
                minuto = int(input('Minuto de realização do teste: '))

                print('Resultado do teste:')
                print('[ 1 ] Positivo')
                print('[ 2 ] Negativo')
                opcao_teste = int(input('Opção: '))
                while opcao_teste not in [1, 2]:
                    opcao_teste = int(input('Opção: '))

                if opcao_teste == 1:
                    resultado_pcr = ResultadoPcr.positivo
                elif opcao_teste == 2:
                    resultado_pcr = ResultadoPcr.negativo
            else:
                ano = mes = dia = hora = minuto = 12
                resultado_pcr = ResultadoPcr.nao_realizado
        else:
            ano = mes = dia = hora = minuto = 12
            resultado_pcr = ResultadoPcr.nao_realizado

        return {'primeira_dose': primeira_dose, 'segunda_dose': segunda_dose,
                'ano': ano, 'mes': mes, 'dia': dia, 'hora': hora, 'minuto': minuto,
                'resultado_pcr': resultado_pcr}

    def mostrar_participante(self, dados_participante):
        print("-" * 40)
        print('CPF DO PARTICIPANTE: ', dados_participante['cpf'])
        print('NOME DO PARTICIPANTE: ', dados_participante['nome'])
        print('DATA DE NASCIMENTO DO PARTICIPANTE: ', dados_participante['data_nascimento'].strftime('%d/%m/%Y'))
        print('ENDEREÇO DO PARTICIPANTE: ')
        print('Logradouro: ', dados_participante['endereco'].logradouro)
        print('Número de endereço: ', dados_participante['endereco'].num_endereco)
        print('CEP: ', dados_participante['endereco'].cep)
        print('STATUS DO PARTICIPANTE: ', dados_participante['status'].value)
        print('COMPROVANTE DE SAÚDE DO PARTICIPANTE: ', end='')
        if dados_participante['comprovante_saude'] is None:
            print('Não cadastrado')
        else:
            print('\nTomou primeira dose vacinal? ',
                  'Sim' if dados_participante['comprovante_saude'].primeira_dose else 'Não')
            print('Tomou segunda dose vacinal? ',
                  'Sim' if dados_participante['comprovante_saude'].segunda_dose else 'Não')
            print('Data e horário do teste PCR: ', 'Não realizado'
            if dados_participante['comprovante_saude'].data_horario_teste == datetime(12, 12, 12, 12, 12)
            else dados_participante['comprovante_saude'].data_horario_teste.strftime('%d/%m/%Y, %H:%M'))
            print('Teste PCR: ', dados_participante['comprovante_saude'].resultado_pcr.value)
        print("-" * 40)

    def selecionar_participante(self):
        cpf = input('\nCPF do participante que deseja selecionar: ')
        return cpf

    def mostrar_mensagem(self, msg):
        print(msg)
