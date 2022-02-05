class TelaSistema:

    def tela_opcoes(self):
        print("-------- Sistema de Eventos ---------")
        print('1 - Tela de evento')
        print('2 - Tela de participante')
        print('3 - Tela de Organizador')
        print('0 - Finalizar Sistema')
        opcao = int(input("Escolha a opcao: "))
        return opcao
