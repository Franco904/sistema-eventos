class TelaLocal:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('-------- LOCAIS ----------')
        print('Escolha a opcao')
        print('1 - Adicionar local')
        print('2 - Excluir local')
        print('3 - Alterar local')
        print('4 - Consultar local')
        print('5 - Listar locais')
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pegar_dados_local(self):
        print('-------- CADASTRAR LOCAL ----------')
        id = input('Id: ')
        nome = input('Nome: ')

        return {'id': id, 'nome': nome}

    def consultar_local(self, dados_local):
        print('ID DO LOCAL: ', dados_local['id'])
        print('NOME DO LOCAL: ', dados_local['nome'])
        print('\n')

    def selecionar_local(self):
        nome_local = input('Nome do local que deseja selecionar: ')
        return nome_local

    def mostrar_mensagem(self, msg):
        print(msg)
