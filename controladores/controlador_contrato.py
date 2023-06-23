from entidade.contrato import Contrato
from telas.tela_contrato import TelaContrato
from dao.contrato_dao import ContratoDAO
from entidade.fun_comum import FunComum
from entidade.gerente import Gerente


class ControladorContrato:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_gerente = self.__controlador_sistema.controlador_gerente
        self.__controlador_cargo = self.__controlador_sistema.controlador_cargo
        self.__tela_contrato = TelaContrato()
        self.__contrato_dao = ContratoDAO()

    @property
    def tela_contrato(self):
        return self.__tela_contrato

    @property
    def contrato_dao(self):
        return self.__contrato_dao

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
        # Recebendo as informações do contrato e montando o obj
        dados_contrato = dados_contrato
        dados_contrato['empregado'].atividade = True

        novo_contrato = Contrato(dados_contrato['data_inicio'], dados_contrato['cargo'],
                                 dados_contrato['empregado'], dados_contrato['filial'],
                                 dados_contrato['empregador'])

        # Incluindo informações DAO
        self.__contrato_dao.add(novo_contrato)

        # Adicionando o contrato na lista de contratos do gerente vigente
        if isinstance(dados_contrato['empregado'], FunComum):
            self.__controlador_sistema.filial_dao.update(dados_contrato['filial'])
            dados_contrato['empregador'].add_contrato(novo_contrato)
            self.__controlador_gerente.gerente_dao.update(dados_contrato['empregador'])

    def demitir(self, funcionario):
        # Procurando pelo contrato
        contrato = self.__contrato_dao.get(funcionario.cpf)
        data_final = self.__tela_contrato.pega_data("Digite a data de finalização do contrato: ")

        # Atualizando informações DAO
        contrato.data_final = data_final
        self.__contrato_dao.update(contrato)

    def excluir_contrato(self, funcionario):
        # Busca do contrato por cpf
        contrato = self.__contrato_dao.get(funcionario.cpf)
        # Removendo os funcionários: exclusão de contrato resulta na exclusão permanente,
        # já a demissão resulta somente no fim das atividades
        if isinstance(funcionario, Gerente):
            self.__controlador_sistema.controlador_gerente.subs_cargo(contrato.filial)
            self.__controlador_sistema.controlador_gerente.gerente_dao.remove(funcionario.cpf)
        if isinstance(funcionario, FunComum):
            self.__controlador_sistema.controlador_fun_comum.fun_comum_dao.remove(funcionario.cpf)
        self.__contrato_dao.remove(contrato.empregado.cpf)

    def modificar_contrato(self, funcionario):
        # Chamada do menu de modificação e definição do contrato a ser modificado
        opcao = self.__tela_contrato.menu_modificacao()
        contrato = self.__contrato_dao.get(funcionario.cpf)

        # Tratamento de cada uma das modificações
        if opcao == 1:
            nova_data_emissao = self.__tela_contrato.pega_data('Digite a nova data de inicio: ')
            contrato.data_inicio = nova_data_emissao
        if opcao == 2:
            # Ao adicionar uma data de finalização do contrato, o a atividade dele torna-se falsa
            nova_data_final = self.__tela_contrato.pega_data('Digite a nova data final: ')
            contrato.data_final = nova_data_final
            if funcionario.atividade is True:
                funcionario.atividade(False)
        if opcao == 3:
            # Utiliza-se da busca de filial do controlador do sistema
            nova_filial = self.__controlador_sistema.busca_por_cep('Digite a nova filial: ')
            contrato.filial = nova_filial
        if opcao == 4:
            # Utiliza-se do selecionador de cargos do controlador de cargos
            cargo_novo = self.__controlador_cargo.selecionar_cargo()
            contrato.cargo = cargo_novo
        if opcao != 0:
            # Atualização do DAO
            self.__contrato_dao.update(contrato)
        if opcao == 0:
            return

    def listar_contrato(self, objeto):
        # Realiza o acesso por uma lista de contratos
        if isinstance(objeto, list):
            lista = []
            for contrato in objeto:
                lista.append(self.__tela_contrato.formata_contrato(contrato))
        # Realiza p acesso por funcionário
        else:
            contrato = self.__contrato_dao.get(objeto.cpf)
            lista = [self.__tela_contrato.formata_contrato(contrato)]
            print(lista)
        # Faz a impressão final
        self.__tela_contrato.listagem('Lista de contrato(s)', lista)

    def pega_contrato_por_cpf(self, cpf):
        for contrato in self.__contrato_dao.get_all():
            if contrato.empregado.cpf == cpf:
                return contrato

    def gera_id(self):
        if len(self.__contrato_dao.get_all()) > 0:
            return self.__contrato_dao.get_all()[-1].id + 1
        else:
            return 0
