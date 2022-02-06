from src.tela.tela_local import TelaLocal
from src.entidade.local import Local


class ControladorLocal:
<<<<<<< Updated upstream

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
=======
    def __init__(self, controlador_eventos):
        self.__controlador_eventos = controlador_eventos
>>>>>>> Stashed changes
        self.__locais = []
        self.__tela_local = TelaLocal()

    def adiciona_local(self):
        dados_local = self.__tela_local.pegar_dados_local()
        local = Local(dados_local["id"], dados_local["nome"])
        self.__locais.append(local)

    def exclui_local(self):
        self.lista_locais()
        nome_local = self.__tela_local.selecionar_local()
        local = self.pega_local_por_nome(nome_local)

        if(local is not None):
            self.__locais.remove(local)
            self.lista_locais()
        else:
            self.__tela_local.mostrar_mensagem("ATENÇÃO: Local não cadastrado")

    def altera_local(self):
        self.lista_locais()
        nome_local = self.__tela_local.selecionar_local()
        local = self.pega_local_por_nome(nome_local)

        if (local is not None):
            novos_dados_local = self.__tela_local.pegar_dados_local()
            local.id = novos_dados_local["id"]
            local.nome = novos_dados_local["nome"]
            self.lista_locais()
        else:
            self.__tela_local.mostrar_mensagem("ATENÇÃO: Local não cadastrado")

    def pega_local_por_nome(self, nome_local):
        for local in self.__locais:
            if local.nome == nome_local:
                return local
        return None

    def lista_locais(self):
        for local in self.__locais:
            self.__tela_local.consultar_local({"id": local.id, "nome": local.nome})

    def retornar(self):
        self.__controlador_eventos.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_local, 2: self.exclui_local, 3: self.altera_local, 4: self.pega_local_por_nome, 5: self.lista_locais, 0: self.retornar()}

        continua = True
        while continua:
            lista_opcoes[self.__tela_local.tela_opcoes()]()
