from entidade.gerente import Gerente

class Filial:
    def __init__(self, cep: str, cidade: str, gerente: Gerente):
        self.__cep = cep
        self.__cidade = cidade
        self.__gerente = gerente
        self.__funcionarios = []


    @property
    def cep(self):
        return self.__cep

    @property
    def cidade(self):
        return self.__cidade

    @property
    def gerente(self):
        return self.__gerente

    @property
    def funcionarios(self):
        return self.__funcionarios

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @gerente.setter
    def gerente(self, gerente):
        self.__gerente = gerente

    @funcionarios.setter
    def funcionarios(self, funcionarios: list):
        self.__funcionarios = funcionarios
