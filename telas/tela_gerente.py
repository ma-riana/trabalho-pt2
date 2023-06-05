from telas.tela_funcionarios import TelaFuncionario


class TelaGerente(TelaFuncionario):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        print("\nTELA DE MODIFICAÇÃO: GERENTE\n"
              + "1) Modificar informações do gerente atual\n"
              + "2) Demitir \n"
              + "3) Listagem de contratos realizados\n"
              + "4) Acessar contrato\n"
              + "0) Retornar\n")
        opcao = super().le_int_validos([1, 2, 3, 4, 0], "Escolha uma opçao: ")
        return opcao
