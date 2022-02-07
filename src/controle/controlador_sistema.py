from src.controle.controlador_eventos import ControladorEvento
from src.controle.controlador_locais import ControladorLocal
from src.controle.controlador_organizadores import ControladorOrganizador
from src.controle.controlador_participantes import ControladorParticipante
from src.controle.controlador_participacoes import ControladorParticipacao
from src.tela.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controladores = {}
        self.__tela_sistema = TelaSistema()

    @property
    def controladores(self):
        return self.__controladores

    def inicializa_sistema(self):
        self.abre_tela()

    def inicializa_controladores(self):
        # Cria as instâncias singleton dos controladores
        self.__controladores = {
            'controlador_eventos': ControladorEvento(self),
            'controlador_locais': ControladorLocal(self),
            'controlador_organizadores': ControladorOrganizador(self),
            'controlador_participantes': ControladorParticipante(self),
            'controlador_participacoes': ControladorParticipacao(self)
        }

    def opcoes(self):
        self.__controladores['controlador_eventos'].abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        self.inicializa_controladores()
        lista_opcoes = {1: self.opcoes, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
