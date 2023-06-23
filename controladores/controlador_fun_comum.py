from exception.repeticao_exp import Repeticao
from controladores.controlador_funcionario import ControladorFuncionario


class ControladorFunComum(ControladorFuncionario):

    def __init__(self):
        super().__init__()
        self.__fun_comum_dao = super().fun_comum_dao

    def add_fun_comum(self, fun_comum):
        self.__fun_comum_dao.add(fun_comum)
