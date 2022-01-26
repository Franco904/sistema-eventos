from src.tela.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        # Controladores (...)
        self.__tela_sistema = TelaSistema()

    # TODO: Implementar métodos para o restante dos controladores

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        # TODO: Implementar lista de opções da tela inicial

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            print(opcao_escolhida)
            break
