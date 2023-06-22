from entidade.funcionario import Funcionario


class FunComum(Funcionario):
    def __init__(self, nome: str, cpf: str, data_nasc: str, atividade=False):
        super().__init__(nome, cpf, data_nasc, atividade)