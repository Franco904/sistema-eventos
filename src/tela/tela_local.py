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

        try:
            opcao = int(input('Escolha uma opção: '))
            while opcao not in [0, 1, 2, 3, 4, 5]:
                opcao = int(input('Escolha uma opção: '))
            return opcao
        except ValueError:
            self.mostrar_mensagem('Valores numéricos devem ser inteiros')

    def pegar_dados_local(self):
        print('\n-------- CADASTRAR LOCAL ----------')
        try:
            id = int(input('Id: '))
            nome = input('Nome: ')

            return {'id': id, 'nome': nome}
        except ValueError:
            self.mostrar_mensagem('Valores de numéricos devem ser inteiros')

    def mostrar_local(self, dados_local):
        print('\nID DO LOCAL: ', dados_local['id'])
        print('NOME DO LOCAL: ', dados_local['nome'])

    def selecionar_local(self):
        try:
            id_local = int(input('Id do local que deseja selecionar: '))
            return id_local
        except ValueError:
            self.mostrar_mensagem('Valores de numéricos devem ser inteiros')

    def mostrar_mensagem(self, msg):
        print(msg)
