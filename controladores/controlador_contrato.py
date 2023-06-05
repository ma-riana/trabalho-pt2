from entidade.contrato import Contrato
from telas.tela_contrato import TelaContrato


class ControladorContrato:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_cargo = self.__controlador_sistema.controlador_cargo
        self.__tela_contrato = TelaContrato()
        self.__contratos = []

    @property
    def tela_contrato(self):
        return self.__tela_contrato

    @property
    def contratos(self):
        return self.__contratos

    def inicializa_sistema(self, controlador_de_retorno, objeto):
        lista_opcoes = {1: self.listar_contrato, 2: self.excluir_contrato,
                        3: self.modificar_contrato,
                        0: controlador_de_retorno.inicializa_sistema}

        while True:
            opcao_escolhida = self.__tela_contrato.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if funcao_escolhida == lista_opcoes[1]:
                self.listar_contrato(objeto)
            if funcao_escolhida == lista_opcoes[2]:
                self.excluir_contrato(objeto)
            if funcao_escolhida == lista_opcoes[3]:
                self.modificar_contrato(objeto)
            else:
                controlador_de_retorno.inicializa_sistema()

    def incluir_contrato(self, dados_contrato):
        dados_contrato = dados_contrato
        id = self.gera_id()
        dados_contrato['empregado'].atividade = True

        novo_contrato = Contrato(id, dados_contrato['data_inicio'], dados_contrato['cargo'],
                                 dados_contrato['empregado'], dados_contrato['filial'],
                                 dados_contrato['empregador'])
        self.__contratos.append(novo_contrato)
        dados_contrato['empregador'].add_contrato(novo_contrato)

    def demitir(self, funcionario):
        contrato = self.pega_contrato_por_cpf_auto(funcionario.cpf)
        data_final = self.__tela_contrato.le_data("Digite a data de finalização do contrato: ")
        contrato.data_final = data_final
        funcionario.atividade = False

    def excluir_contrato(self, funcionario):
        contrato = self.pega_contrato_por_cpf_auto(funcionario.cpf)
        self.__contratos.remove(contrato)
        funcionario.atividade = False

    def modificar_contrato(self, funcionario):
        opcao = self.__tela_contrato.menu_modificacao()
        contrato = self.pega_contrato_por_cpf_auto(funcionario.cpf)
        if opcao == 1:
            nova_data_emissao = self.__tela_contrato.le_data('Digite a nova data de inicio: ')
            contrato.data_inicio = nova_data_emissao
        if opcao == 2:
            nova_data_final = self.__tela_contrato.le_data('Digite a nova data final: ')
            contrato.data_final = nova_data_final
            if funcionario.atividade is True:
                funcionario.atividade(False)
        if opcao == 3:
            nova_filial = self.__controlador_sistema.busca_por_cep('Digite a nova filial: ')
            contrato.filial = nova_filial
        if opcao == 4:
            cargo_novo = self.__controlador_cargo.selecionar_cargo()
            contrato.cargo = cargo_novo
        if opcao == 0:
            return


    def listar_contrato(self, objeto):
        cpf = objeto.cpf
        contrato = self.pega_contrato_por_cpf_auto(cpf)
        self.__tela_contrato.listar_contrato(contrato)

    def listar_contrato_auto(self, contrato):
        self.__tela_contrato.listar_contrato(contrato)

    def pega_contrato_por_cpf_auto(self, cpf):
        for contrato in self.__contratos:
            if contrato.empregado.cpf == cpf:
                return contrato

    def gera_id(self):
        if len(self.__contratos) > 0:
            return self.__contratos[-1].id + 1
        else:
            return 0
