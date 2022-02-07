from src.controle.controlador_eventos import ControladorEvento
from src.controle.controlador_participantes import ControladorParticipante
from src.controle.controlador_organizadores import ControladorOrganizador
from src.tela.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controlador_eventos = ControladorEvento(self)
        self.__controlador_participantes = ControladorParticipante(self)
        self.__controlador_organizadores = ControladorOrganizador(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def evento(self):
        self.__controlador_eventos.abre_tela()

    def participante(self):
        self.__controlador_participantes.abre_tela()

    def organizador(self):
        self.__controlador_organizadores.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.evento, 2: self.participante, 3: self.organizador, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
