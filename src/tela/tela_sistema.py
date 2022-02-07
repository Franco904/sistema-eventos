class TelaSistema:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("\n-------- Sistema de Eventos ---------")
        print('1 - Abrir Opções')
        print('0 - Finalizar Sistema')
        print("-" * 40)

        try:
            opcao = int(input("Escolha a opcao: "))
            while opcao not in [0, 1, 2, 3]:
                opcao = int(input('Escolha uma opção: '))
            return opcao
        except ValueError:
            print('Valores numéricos devem ser inteiros')
