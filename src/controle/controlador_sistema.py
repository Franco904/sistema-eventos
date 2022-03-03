from src.controle.controlador_eventos import ControladorEvento
from src.controle.controlador_locais import ControladorLocal
from src.controle.controlador_organizadores import ControladorOrganizador
from src.controle.controlador_participacoes import ControladorParticipacao
from src.controle.controlador_participantes import ControladorParticipante
from src.tela.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controladores = {}
        self.__tela_sistema = TelaSistema()

    @property
    def controladores(self):
        return self.__controladores

    def inicializar_sistema(self):
        self.inicializar_controladores()
        self.abrir_tela()

    def inicializar_controladores(self):
        # Cria instâncias globais dos controladores
        self.__controladores = {
            'controlador_eventos': ControladorEvento(self),
            'controlador_locais': ControladorLocal(self),
            'controlador_organizadores': ControladorOrganizador(self),
            'controlador_participantes': ControladorParticipante(self),
            'controlador_participacoes': ControladorParticipacao(self)
        }

    def abrir_eventos(self):
        self.__controladores['controlador_eventos'].abrir_tela()

    def abrir_locais(self):
        self.__controladores['controlador_locais'].abrir_tela()

    def abrir_organizadores(self):
        self.__controladores['controlador_organizadores'].abrir_tela()

    def abrir_participantes(self):
        self.__controladores['controlador_participantes'].abrir_tela()

    def abrir_participacoes(self):
        self.__controladores['controlador_participacoes'].abrir_tela()

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self):
        lista_opcoes = {1: self.abrir_eventos,
                        2: self.abrir_locais,
                        3: self.abrir_organizadores,
                        4: self.abrir_participantes,
                        5: self.abrir_participacoes,
                        0: self.encerrar_sistema}

        while True:
            try:
                lista_opcoes[self.__tela_sistema.tela_opcoes()]()
            except (KeyError, ValueError):
                self.__tela_sistema.mostrar_mensagem('Valores numéricos devem ser inteiros.')
