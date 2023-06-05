from entidade.fun_comum import FunComum
from telas.tela_fun_comum import TelaFuncomum
from exception.repeticao import Repeticao
from exception.naoExistencia import NaoExistencia
from exception.filial_errada import FilialErrada


class ControladorFunComumEsp:

    def __init__(self, controlador_filial, funcionarios):
        self.__controlador_filial = controlador_filial
        self.__controlador_sistema = self.__controlador_filial.controlador_sistema
        self.__controlador_contrato = self.__controlador_sistema.controlador_contrato
        self.__controlador_cargo = self.__controlador_sistema.controlador_cargo
        self.__tela_fun_comum = TelaFuncomum()
        self.__funcionarios = funcionarios

    def inicializa_sistema(self):
        lista_opcoes = {1: self.modificar_dados, 2: self.add_fun_comum,
                        3: self.acessar_contrato, 4: self.listar_todos,
                        5: self.demitir, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_fun_comum.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def modificar_dados(self):
        funcionario = self.busca_fun_por_cpf("Digite o CPF do funcionário para modificação: ")
        opcao = self.__tela_fun_comum.menu_modificacao()
        if opcao == 1:
            novo_nome = self.__tela_fun_comum.pega_input("Digite o novo nome:")
            funcionario.nome = novo_nome
        if opcao == 2:
            novo_cpf = self.__tela_fun_comum.le_cpf("Digite o novo CPF: ")
            funcionario.cpf = novo_cpf
        if opcao == 3:
            nova_data_nasc = self.__tela_fun_comum.le_data("Digite a nova data de nascimento:")
            funcionario.data_nasc = nova_data_nasc
        if opcao == 0:
            return

    def add_fun_comum(self):
        self.__tela_fun_comum.mostra_mensagem("\n=== Cadastro de funcionario comum ===")
        # Realizando a checagem de repetição de CPF
        while True:
            novo_fun_comum = self.__tela_fun_comum.pega_dados_cadastro()
            if self.checagem_repeticao(novo_fun_comum['CPF']):
                break
            self.__tela_fun_comum.mostra_mensagem('CPF já cadastrado.')

        # Criação do funcionário
        novo_funcionario = FunComum(novo_fun_comum['nome'], novo_fun_comum['CPF'],
                                    novo_fun_comum['data_nasc'])
        self.__funcionarios.append(novo_funcionario)
        self.__controlador_sistema.controlador_fun_comum.add_fun_comum(novo_funcionario)

        # Definição das informações para o contrato
        data_inicio = novo_fun_comum['data_inicio']
        empregador = self.__controlador_filial.filial.gerente
        filial = self.__controlador_filial.filial
        cargo = self.__controlador_cargo.seleciona_cargo()

        dados_contrato = {'data_inicio': data_inicio, 'cargo': cargo, 'empregado': novo_funcionario,
                          'filial': filial, 'empregador': empregador}
        self.__controlador_contrato.incluir_contrato(dados_contrato)

    def demitir(self):
        fun_comum = self.busca_fun_por_cpf("Digite o CPF do funcionário para a demissão: ")
        self.__controlador_contrato.demitir(fun_comum)

    def acessar_contrato(self):
        fun_comum = self.busca_fun_por_cpf("Digite o CPF do funcionário para acessar o contrato: ")
        self.__controlador_contrato.inicializa_sistema(self, fun_comum)

    def listar_todos(self):
        lista = self.__funcionarios
        if len(lista) > 0:
            self.__tela_fun_comum.mostra_mensagem('\n=== Listagem de funcionários ===')
            for fun in lista:
                self.__tela_fun_comum.listagem(fun.nome, fun.cpf, fun.data_nasc)
        else:
            self.__tela_fun_comum.mostra_mensagem('Lista vazia.')

    def busca_fun_por_cpf(self, msg):
        while True:
            cpf_buscado = self.__tela_fun_comum.le_cpf(msg)
            lista_fun_geral = self.__controlador_sistema.controlador_fun_comum.fun_comuns
            try:
                for funcionario in self.__funcionarios:
                    if funcionario.cpf == cpf_buscado:
                        return funcionario
                for funcionario in lista_fun_geral:
                    if funcionario.cpf == cpf_buscado:
                        raise FilialErrada(cpf_buscado)
                raise NaoExistencia()
            except NaoExistencia:
                print('Funcionario não encontrado. Tente novamente.')
            except FilialErrada:
                FilialErrada(cpf_buscado).msg()

    def checagem_repeticao(self, cpf):
        while True:
            try:
                for _ in self.__funcionarios:
                    if _.cpf == cpf:
                        raise Repeticao('CPF', cpf)
                return True
            except Repeticao:
                return False

    def retornar(self):
        self.__controlador_filial.inicializa_sistema()
