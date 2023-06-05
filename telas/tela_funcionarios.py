from telas.abstract_tela import AbstractTela


class TelaFuncionario(AbstractTela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        pass

    def menu_modificacao(self):
        print("O que deseja modificar?\n"
              + "1) Nome\n"
              + "2) CPF\n"
              + "3) Data de nascimento\n"
              + "0) Retornar\n")
        opcao = super().le_int_validos([1, 2, 3, 0], "Escolha uma opçao: ")
        return opcao

    def pega_dados_cadastro(self):
        print("Regras: 1. É necessário ser maior de 18 anos\n"
              + "        2. Não é permitido contratar funcionários já demitidos\n")
        nome = input("Nome: ")
        cpf = self.le_cpf("CPF: ")
        data_nasc = self.le_data("Data de nascimento: ")
        data_inicio = self.le_data("Data de contratação: ")
        novo_funcionario = {'nome': nome, 'CPF': cpf, "data_nasc": data_nasc,
                            'data_inicio': data_inicio}
        return novo_funcionario
