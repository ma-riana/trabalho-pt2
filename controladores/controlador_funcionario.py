from abc import ABC, abstractmethod

class ControladorFuncionario(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def pega_fun_por_cep(self):
        pass

    @abstractmethod
    def demitir(self):
        pass

    @abstractmethod
    def transferir(self):
        pass

    @abstractmethod
    def mudar_cargo(self):
        pass


