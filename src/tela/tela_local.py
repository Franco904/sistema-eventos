class TelaLocal:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('\n-------- LOCAIS ----------')
        print('1 - Adicionar local')
        print('2 - Excluir local')
        print('3 - Alterar local')
        print('4 - Mostrar local')
        print('5 - Listar locais')
        print('0 - Retornar')
        print("-" * 40)

        opcao = int(input('Escolha uma opção: '))
        while opcao not in [0, 1, 2, 3, 4, 5]:
            opcao = int(input('Escolha uma opção: '))
        return opcao

    def pegar_dados_local(self, editando: bool):
        if not editando:
            print('\n-------- CADASTRAR LOCAL ----------')
            id = int(input('Id: '))
        else:
            print('\n-------- ALTERAR LOCAL ----------')
            id = None

        nome = input('Nome: ')

        return {'id': id, 'nome': nome}

    def mostrar_local(self, dados_local):
        print("-" * 40)
        print('ID DO LOCAL: ', dados_local['id'])
        print('NOME DO LOCAL: ', dados_local['nome'])
        print("-" * 40)

    def selecionar_local(self):
        id_local = int(input('Id do local que deseja selecionar: '))
        return id_local

    def mostrar_mensagem(self, msg):
        print(msg)
