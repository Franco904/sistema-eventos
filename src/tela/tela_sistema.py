class TelaSistema:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('\n-------- Sistema de Eventos ---------')
        print('1 - Opções de eventos')
        print('2 - Opções de locais')
        print('3 - Opções de organizadores')
        print('4 - Opções de participantes')
        print('5 - Opções de participações')
        print('0 - Finalizar Sistema')
        print("-" * 40)

        opcao = int(input("Escolha a opção: "))
        while opcao not in [0, 1, 2, 3, 4, 5]:
            opcao = int(input('Escolha uma opção: '))
        return opcao

    def mostrar_mensagem(self, msg):
        print(msg)
