from src.entidade.local import Local
from src.tela.tela_local import TelaLocal


class ControladorLocal:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__locais = []
        self.__tela_local = TelaLocal()

    def adiciona_local(self):
        dados_local = self.__tela_local.pegar_dados_local()
        local = Local(dados_local["id"], dados_local["nome"])
        self.__locais.append(local)
        self.__tela_local.mostrar_mensagem('Local adicionado na lista')

    def exclui_local(self):
        self.lista_locais()
        if len(self.__locais) > 0:
            id_local = self.__tela_local.selecionar_local()
            local = self.pega_local_por_id(id_local)

            if local is not None:
                self.__locais.remove(local)
                self.__tela_local.mostrar_mensagem('Local removido da lista')
            else:
                self.__tela_local.mostrar_mensagem("ATENÇÃO: Local não cadastrado")

    def altera_local(self):
        self.lista_locais()
        if len(self.__locais) > 0:
            id_local = self.__tela_local.selecionar_local()
            local = self.pega_local_por_id(id_local)

            if local is not None:
                novos_dados_local = self.__tela_local.pegar_dados_local()
                local.id = novos_dados_local["id"]
                local.nome = novos_dados_local["nome"]
                self.__tela_local.mostrar_mensagem('Dados do local alterados com sucesso')
            else:
                self.__tela_local.mostrar_mensagem("ATENÇÃO: Local não cadastrado")

    def mostra_local(self):
        if len(self.__locais) > 0:
            id_local = self.__tela_local.selecionar_local()
            local = self.pega_local_por_id(id_local)

            if local is not None:
                self.__tela_local.mostrar_local({'id': local.id, 'nome': local.nome})
            else:
                self.__tela_local.mostrar_mensagem('ATENÇÃO: Local não cadastrado')
        else:
            self.__tela_local.mostrar_mensagem('Não há locais cadastrados para listar')

    def pega_local_por_id(self, id_local):
        for local in self.__locais:
            if local.id == id_local:
                return local
        return None

    def lista_locais(self):
        if len(self.__locais) == 0:
            self.__tela_local.mostrar_mensagem('Não há locais cadastrados para listar')
        else:
            for local in self.__locais:
                self.__tela_local.mostrar_local({"id": local.id, "nome": local.nome})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_local, 2: self.exclui_local, 3: self.altera_local,
                        4: self.mostra_local, 5: self.lista_locais, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_local.tela_opcoes()]()
