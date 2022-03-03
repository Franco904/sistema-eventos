class TelaOrganizador:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('\n-------- ORGANIZADORES ----------')
        print('1 - Adicionar Organizador')
        print('2 - Excluir Organizador')
        print('3 - Alterar Organizador')
        print('4 - Mostrar Organizador')
        print('5 - Listar Organizador')
        print('0 - Retornar')
        print("-" * 40)

        opcao = int(input('Escolha uma opção: '))
        while opcao not in [0, 1, 2, 3, 4, 5]:
            opcao = int(input('Escolha uma opção: '))
        return opcao

    def pegar_dados_organizador(self):
        print('\n-------- CADASTRAR ORGANIZADOR ----------')
        cpf = input('CPF: ')
        nome = input('Nome: ')
        dia_nascimento = int(input('Dia de nascimento: '))
        mes_nascimento = int(input('Mês de nascimento: '))
        ano_nascimento = int(input('Ano de nascimento: '))

        return {'cpf': cpf, 'nome': nome, 'dia_nascimento': dia_nascimento, 'mes_nascimento': mes_nascimento,
                'ano_nascimento': ano_nascimento}

    def mostrar_organizador(self, dados_organizador):
        print("-" * 40)
        print('CPF DO ORGANIZADOR: ', dados_organizador['cpf'])
        print('NOME DO ORGANIZADOR: ', dados_organizador['nome'])
        print('DATA DE NASCIMENTO DO ORGANIZADOR: ', dados_organizador['data_nascimento'].strftime('%d/%m/%Y'))
        print("-" * 40)

    def selecionar_organizador(self):
        cpf_organizador = input('CPF do organizador que deseja selecionar: ')
        return cpf_organizador

    def mostrar_mensagem(self, msg):
        print(msg)
