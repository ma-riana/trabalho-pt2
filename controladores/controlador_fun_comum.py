from exception.repeticao_exp import Repeticao
from dao.fun_comum_dao import FunComumDAO


class ControladorFunComum:

    def __init__(self):
        self.__fun_comum_dao = FunComumDAO()

    @property
    def fun_comum_dao(self):
        return self.__fun_comum_dao

    def add_fun_comum(self, fun_comum):
        self.__fun_comum_dao.add(fun_comum)

    def checagem_repeticao(self, cpf):
        while True:
            try:
                if self.__fun_comum_dao.get(cpf) is not None:
                    raise Repeticao('CPF', cpf)
                return True
            except Repeticao:
                return False