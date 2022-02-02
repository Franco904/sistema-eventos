class Local:

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError
