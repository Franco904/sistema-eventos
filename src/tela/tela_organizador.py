class TelaOrganizador:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('-------- LOCAIS ----------')
        print('1 - Adicionar Organizador')
        print('2 - Excluir Organizador')
        print('3 - Alterar Organizador')
        print('4 - Consultar Organizador')
        print('5 - Listar Organizador')
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pegar_dados_organizador(self):
        print('-------- CADASTRAR ORGANIZADOR ----------')
        cpf = input('CPF: ')
        nome = input('Nome: ')
        dia_nascimento = input('Dia do Nascimento: ')
        mes_nascimento = input('Mês do Nascimento: ')
        ano_nascimento = input('Ano do Nascimento: ')

        return {'cpf': cpf, 'nome': nome, 'dia_nascimento': dia_nascimento, 'mes_nascimento': mes_nascimento,
                'ano_nascimento': ano_nascimento}

    def consultar_organizador(self, dados_organizador):
        print('CPF DO ORGANIZADOR: ', dados_organizador['cpf'])
        print('NOME DO ORGANIZADOR: ', dados_organizador['nome'])
        print('DATA DE NASCIMENTO DO ORGANIZADOR: {0}/{1}/{2}'.format(dados_organizador['dia_nascimento'],
                                                                      dados_organizador['mes_nascimento'],
                                                                      dados_organizador['ano_nascimento']))
        print('\n')

    def selecionar_organizador(self):
        cpf_organizador = input('CPF do Organizador que deseja selecionar: ')
        return cpf_organizador

    def mostrar_mensagem(self, msg):
        print(msg)
