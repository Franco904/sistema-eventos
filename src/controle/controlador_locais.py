from src.entidade.local import Local
from src.tela.tela_local import TelaLocal


class ControladorLocal:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__locais = []
        self.__tela_local = TelaLocal()

    @property
    def locais(self):
        return self.__locais

    def adicionar_local(self):
        dados_local = self.__tela_local.pegar_dados_local(False)

        if dados_local is None:
            return

        # Faz a verificação da existência do local na lista
        for local in self.__locais:
            if local.id == dados_local['id']:
                self.__tela_local.mostrar_mensagem('O id inserido já pertence a um local na lista.')
                return

        try:
            local = Local(dados_local['id'], dados_local['nome'])

            self.__locais.append(local)
            self.__tela_local.mostrar_mensagem('Local adicionado na lista.')

        except TypeError:
            self.__tela_local.mostrar_mensagem('Algum dado foi inserido incorretamente.')

    def excluir_local(self):
        self.listar_locais()

        if len(self.__locais) > 0:
            id_local = self.__tela_local.selecionar_local()
            local = self.pegar_local_por_id(id_local)

            if local is not None:
                self.__locais.remove(local)
                self.__tela_local.mostrar_mensagem('Local removido da lista.')

            else:
                self.__tela_local.mostrar_mensagem('ATENÇÃO: Local não cadastrado.')

    def alterar_local(self):
        self.listar_locais()

        if len(self.__locais) > 0:
            id_local = self.__tela_local.selecionar_local()
            local = self.pegar_local_por_id(id_local)

            if local is not None:
                novos_dados_local = self.__tela_local.pegar_dados_local(True)

                if novos_dados_local is None:
                    return

                try:
                    local.nome = novos_dados_local['nome']
                    self.__tela_local.mostrar_mensagem('Local alterado com sucesso.')

                except TypeError:
                    self.__tela_local.mostrar_mensagem('Algum dado foi inserido incorretamente.')

            else:
                self.__tela_local.mostrar_mensagem('ATENÇÃO: Local não cadastrado.')

    def mostrar_local(self):
        if len(self.__locais) > 0:
            id_local = self.__tela_local.selecionar_local()
            if id_local is None:
                return

            local = self.pegar_local_por_id(id_local)

            if local is not None:
                self.__tela_local.mostrar_local({'id': local.id, 'nome': local.nome})
            else:
                self.__tela_local.mostrar_mensagem('ATENÇÃO: Local não cadastrado.')
        else:
            self.__tela_local.mostrar_mensagem('Não há locais cadastrados para listar.')

    def pegar_local_por_id(self, id_local):
        for local in self.__locais:
            if local.id == id_local:
                return local
        return None

    def listar_locais(self):
        if len(self.__locais) > 0:
            for local in self.__locais:
                self.__tela_local.mostrar_local({'id': local.id, 'nome': local.nome})
        else:
            self.__tela_local.mostrar_mensagem('Não há locais cadastrados para listar.')

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.adicionar_local,
                        2: self.excluir_local,
                        3: self.alterar_local,
                        4: self.mostrar_local,
                        5: self.listar_locais,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_local.tela_opcoes()]()
