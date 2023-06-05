from telas.abstract_tela import AbstractTela


class TelaSistema(AbstractTela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        print("\nTELA PRINCIPAL: CONTROLE DE FILIAIS\n"
              + "O que deseja fazer?\n"
              + "1) Adicionar uma filial\n"
              + "2) Excluir uma filial\n"
              + "3) Modificar uma filial\n"
              + "4) Listar filiais\n"
              + "0) Sair\n")
        opcao = super().le_int_validos([0, 1, 2, 3, 4], "Escolha uma opção: ")
        return opcao

    def pega_dados_cadastro(self):
        cep = self.le_cep("Informe o CEP: ")
        cidade = input("Informe a cidade: ")
        nova_filial = {"cep": cep, "cidade": cidade}
        return nova_filial

    def pega_cep(self):
        cep = self.le_int_positivo("Informe o CEP: ")
        return cep

    def listagem(self, cep, cidade, gerente):
        print(f"CEP: {cep}\nCidade: {cidade}\nGerente: {gerente}\n")

    def mostra_mensagem(self, msg):
        return super().mostra_mensagem(msg)
